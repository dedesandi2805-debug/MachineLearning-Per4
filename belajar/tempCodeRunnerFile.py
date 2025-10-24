import time
import sys
import os

# Definisikan lirik lagu
lirik_lagu = "Melihatmu bersemi dan bermekaran, Tawa candamu berikan kekuatan, Sisa hariku pagi berganti waktu, Memelukmu, Kita kan tua dan kehilangan pegangan, Lihat senyummu memberikan kekuatan, Sisa nafasku cinta tak kenal waktu, Menjagamu "

try:
    lebar_terminal = os.get_terminal_size().columns
except OSError:
    lebar_terminal = 80

spasi_awal = lebar_terminal // 2
teks_geser = " " * spasi_awal + lirik_lagu + " " * lebar_terminal

while True:
    for i in range(len(teks_geser) - lebar_terminal):
        # Ambil bagian teks yang akan ditampilkan
        teks_tampil = teks_geser[i:i + lebar_terminal]
        
        sys.stdout.write('\r' + teks_tampil)
        sys.stdout.flush()
        
        time.sleep(0.55)