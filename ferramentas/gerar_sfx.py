"""Efeitos sonoros sintetizados (numpy/scipy, sem API, sem licença de terceiros) → sfx/<tipo>-<n>.wav, 48 kHz.
Tipos: whoosh, swoosh (curto), impacto, boom, braam, riser, pop, clique, glitch, ding, tick, swell.
Uso: python3 gerar_sfx.py   (determinístico: mesma semente, mesmos arquivos)"""
import os
import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 48000
AQUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(AQUI, 'sfx')
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(7)


def t_(d):
    return np.arange(int(SR * d)) / SR


def env(n, a, r, curva=3.0):
    e = np.ones(n)
    na, nr = max(1, int(a * SR)), max(1, int(r * SR))
    e[:na] = np.linspace(0, 1, na) ** 2
    e[-nr:] *= np.linspace(1, 0, nr) ** curva
    return e


def bp_sweep(x, f0, f1, q=2.0):
    """passa-faixa que varre de f0 a f1 (bloco a bloco)."""
    y = np.zeros_like(x)
    blocos = 64
    L = len(x) // blocos + 1
    zi = None
    for i in range(blocos):
        f = f0 * (f1 / f0) ** (i / (blocos - 1))
        b, a = signal.iirpeak(min(f, SR / 2 - 100), q, SR)
        seg = x[i * L:(i + 1) * L]
        if not len(seg):
            break
        if zi is None:
            zi = signal.lfilter_zi(b, a) * 0
        y[i * L:(i + 1) * L], zi = signal.lfilter(b, a, seg, zi=zi)
    return y


def reverb(x, tempo=0.6, mix=0.25):
    n = int(SR * tempo)
    ir = rng.standard_normal(n) * np.exp(-np.linspace(0, 6, n))
    w = signal.fftconvolve(x, ir)[:len(x) + n]
    w = np.pad(w, (0, len(x) + n - len(w)))
    w /= np.abs(w).max() + 1e-9
    y = np.concatenate([x, np.zeros(n)])
    return (1 - mix) * y + mix * w * np.abs(x).max()


def estereo(x, larg=0.3):
    d = int(SR * 0.012 * larg)
    return np.stack([x, np.concatenate([np.zeros(d), x[:-d]]) if d else x], 1)


def salvar(nome, x, pan=True):
    x = x / (np.abs(x).max() + 1e-9) * 0.89
    s = estereo(x) if pan else np.stack([x, x], 1)
    wavfile.write(os.path.join(OUT, nome + '.wav'), SR, (s * 32767).astype(np.int16))


def whoosh(d, f0, f1, nome):
    n = int(SR * d)
    x = rng.standard_normal(n)
    y = bp_sweep(x, f0, f1, q=1.4) + 0.3 * bp_sweep(x, f0 * 2, f1 * 2, q=2)
    e = np.sin(np.linspace(0, np.pi, n)) ** 1.6
    salvar(nome, reverb(y * e, 0.35, 0.2))


def impacto(nome, f0=55, d=1.2, ruido=0.6, bright=4000):
    t = t_(d)
    f = f0 * (1 + 2.5 * np.exp(-t * 18))
    tom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 3.2)
    nz = rng.standard_normal(len(t)) * np.exp(-t * 28)
    b, a = signal.butter(2, bright / (SR / 2))
    nz = signal.lfilter(b, a, nz)
    x = tom + ruido * nz
    salvar(nome, reverb(np.tanh(x * 2.2), 0.9, 0.3))


def braam(nome, f0=43.65, d=2.6):
    t = t_(d)
    x = sum(np.sign(np.sin(2 * np.pi * f0 * k * t * (1 + 0.003 * np.sin(2 * np.pi * 0.7 * t)))) / k for k in (1, 1.5, 2, 3))
    b, a = signal.butter(4, 900 / (SR / 2))
    x = signal.lfilter(b, a, x) * env(len(t), 0.04, 1.6, 2)
    salvar(nome, reverb(np.tanh(x * 1.5), 1.2, 0.35))


def riser(nome, d=1.6, f0=200, f1=2400):
    t = t_(d)
    f = f0 * (f1 / f0) ** (t / d)
    tom = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.4
    nz = bp_sweep(rng.standard_normal(len(t)), 400, 6000, 1.0)
    e = (t / d) ** 2.2
    salvar(nome, (tom + nz) * e)


def pop(nome, f=900, d=0.12):
    t = t_(d)
    x = np.sin(2 * np.pi * f * (1 + 0.8 * np.exp(-t * 60)) * t) * np.exp(-t * 45)
    salvar(nome, x, pan=False)


def clique(nome, f=3200):
    t = t_(0.05)
    x = rng.standard_normal(len(t)) * np.exp(-t * 220) + np.sin(2 * np.pi * f * t) * np.exp(-t * 160)
    salvar(nome, x, pan=False)


def glitch(nome, d=0.35):
    n = int(SR * d)
    x = np.zeros(n)
    i = 0
    while i < n:
        L = int(rng.integers(300, 2400))
        f = rng.choice([180, 440, 880, 1760, 3520])
        seg = np.sign(np.sin(2 * np.pi * f * np.arange(L) / SR)) * rng.uniform(0.3, 1)
        if rng.random() < 0.3:
            seg = rng.standard_normal(L) * 0.6
        x[i:i + L] = seg[:len(x[i:i + L])]
        i += L + int(rng.integers(0, 800))
    salvar(nome, x * env(n, 0.005, 0.05))


def ding(nome, f=1318.5, d=1.4):
    t = t_(d)
    x = sum(np.sin(2 * np.pi * f * k * t) * np.exp(-t * (2.5 + k)) / k for k in (1, 2.76, 5.4))
    salvar(nome, reverb(x * env(len(t), 0.002, 0.3), 0.8, 0.25))


def tick(nome):
    t = t_(0.03)
    salvar(nome, np.sin(2 * np.pi * 2200 * t) * np.exp(-t * 300), pan=False)


def swell(nome, d=1.8):
    t = t_(d)
    x = sum(np.sin(2 * np.pi * f * t) for f in (220, 277.2, 329.6, 440)) * (t / d) ** 1.5
    b, a = signal.butter(2, 2500 / (SR / 2))
    salvar(nome, signal.lfilter(b, a, x) * env(len(t), 0.01, 0.15))


for i, (d, a, b) in enumerate([(0.55, 300, 3500), (0.7, 200, 2500), (0.45, 600, 6000), (0.9, 150, 1800)], 1):
    whoosh(d, a, b, f'whoosh-{i}')
for i, (d, a, b) in enumerate([(0.22, 1200, 7000), (0.28, 800, 5000), (0.2, 2000, 9000)], 1):
    whoosh(d, a, b, f'swoosh-{i}')
for i, (f0, d, r, br) in enumerate([(55, 1.2, 0.6, 4000), (48, 1.5, 0.8, 3000), (62, 1.0, 0.5, 6000), (41, 1.8, 0.9, 2500)], 1):
    impacto(f'impacto-{i}', f0, d, r, br)
for i, (f0, d) in enumerate([(36, 1.6), (32, 2.0)], 1):
    impacto(f'boom-{i}', f0, d, 0.3, 1500)
for i, f0 in enumerate([43.65, 49.0], 1):
    braam(f'braam-{i}', f0)
for i, (d, a, b) in enumerate([(1.6, 200, 2400), (1.0, 300, 3000), (2.2, 120, 1800)], 1):
    riser(f'riser-{i}', d, a, b)
for i, f in enumerate([900, 1200, 700], 1):
    pop(f'pop-{i}', f)
for i, f in enumerate([3200, 4200], 1):
    clique(f'clique-{i}', f)
for i in range(1, 4):
    glitch(f'glitch-{i}', 0.25 + 0.1 * i)
for i, f in enumerate([1318.5, 1760], 1):
    ding(f'ding-{i}', f)
tick('tick-1')
swell('swell-1')
print(len(os.listdir(OUT)), 'efeitos em', OUT)
