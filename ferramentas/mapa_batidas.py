#!/usr/bin/env python3
"""Mede o andamento de uma trilha e acha a maior subida de energia.

Uso: python3 ferramentas/mapa_batidas.py trilha.wav [--saida mapa.json]

Saída: BPM estimado, duraçêo de uma batida, primeira batida e os momentos em que a
energia mais sobe. Esses momentos sêo os candidatos para a entrada do logo.
"""
import argparse
import json

import numpy as np
from scipy.io import wavfile
from scipy.signal import find_peaks, stft

BPM_MIN, BPM_MAX = 70, 170


def carregar(caminho):
    taxa, dados = wavfile.read(caminho)
    dados = dados.astype(np.float64)
    if dados.ndim > 1:
        dados = dados.mean(axis=1)
    pico = np.max(np.abs(dados)) or 1.0
    return taxa, dados / pico


def novidade(taxa, x, salto=512):
    """Curva de ataques: quanto o espectro cresce de um quadro para o outro."""
    _, _, z = stft(x, fs=taxa, nperseg=2048, noverlap=2048 - salto, boundary=None)
    mag = np.log1p(np.abs(z))
    fluxo = np.maximum(np.diff(mag, axis=1), 0).sum(axis=0)
    fluxo -= np.convolve(fluxo, np.ones(43) / 43, mode="same")
    return np.maximum(fluxo, 0), taxa / salto


def andamento(curva, fps):
    ac = np.correlate(curva, curva, mode="full")[len(curva) - 1:]
    ini, fim = int(fps * 60 / BPM_MAX), int(fps * 60 / BPM_MIN)
    atraso = ini + int(np.argmax(ac[ini:fim]))
    return 60 * fps / atraso, atraso


def fase(curva, atraso):
    somas = [curva[i::atraso].sum() for i in range(atraso)]
    return int(np.argmax(somas))


def subidas(taxa, x, janela=0.5, n=3):
    passo = int(taxa * janela)
    energia = np.array([np.sqrt(np.mean(x[i:i + passo] ** 2)) for i in range(0, len(x) - passo, passo)])
    db = 20 * np.log10(energia + 1e-6)
    salto = db[2:] - db[:-2]
    picos, _ = find_peaks(salto, distance=4)
    melhores = sorted(picos, key=lambda p: salto[p], reverse=True)[:n]
    return [{"t": round((p + 2) * janela, 2), "sobe_db": round(float(salto[p]), 1)} for p in sorted(melhores)]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("trilha")
    ap.add_argument("--saida")
    a = ap.parse_args()
    taxa, x = carregar(a.trilha)
    curva, fps = novidade(taxa, x)
    bpm, atraso = andamento(curva, fps)
    r = {
        "duracao": round(len(x) / taxa, 3),
        "bpm": round(bpm, 1),
        "batida_s": round(60 / bpm, 4),
        "primeira_batida_s": round(fase(curva, atraso) / fps, 3),
        "subidas": subidas(taxa, x),
    }
    texto = json.dumps(r, ensure_ascii=False, indent=2)
    print(texto)
    if a.saida:
        with open(a.saida, "w", encoding="utf-8") as f:
            f.write(texto + "\n")


if __name__ == "__main__":
    main()
