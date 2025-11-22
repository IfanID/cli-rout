#!/usr/bin/env python3
"""
Modul untuk konfigurasi dan pengaturan awal CLI rout.
"""
import os
from pathlib import Path

def setup_rout_directory() -> None:
    """
    Memeriksa dan membuat direktori ~/.rout jika belum ada.

    Direktori ini digunakan untuk menyimpan konfigurasi atau data lain
    yang dibutuhkan oleh CLI rout.
    """
    try:
        home_dir = Path.home()
        rout_dir = home_dir / '.rout'

        if not rout_dir.is_dir():
            if rout_dir.exists():
                # Jika ada file dengan nama .rout, hapus atau beri pesan error
                print(f"Error: Terdapat file bernama '.rout' di home direktori Anda, bukan folder.")
                print("Harap hapus atau pindahkan file tersebut.")
                return

            print(f"Membuat direktori konfigurasi di: {rout_dir}")
            rout_dir.mkdir()
        # Jika direktori sudah ada, tidak perlu melakukan apa-apa.
        # Pesan bisa ditambahkan di sini jika perlu.

    except Exception as e:
        print(f"Error: Gagal membuat direktori ~/.rout: {e}")

if __name__ == '__main__':
    # Untuk pengujian langsung
    setup_rout_directory()
