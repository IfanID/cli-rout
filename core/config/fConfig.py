#!/usr/bin/env python3
"""
Modul untuk konfigurasi dan pengaturan awal CLI rout.
"""
import os
import shutil
from pathlib import Path

def setup_rout_directory() -> None:
    """
    Memeriksa dan membuat direktori ~/.rout jika belum ada.
    Juga menyalin konfigurasi default .zshrc jika belum ada.
    """
    try:
        home_dir = Path.home()
        rout_dir = home_dir / '.rout'
        zshrc_dest = rout_dir / '.zshrc'

        # Membuat direktori .rout jika belum ada
        if not rout_dir.is_dir():
            if rout_dir.exists():
                print(f"Error: Terdapat file bernama '.rout' di home direktori Anda, bukan folder.")
                print("Harap hapus atau pindahkan file tersebut.")
                return
            print(f"Membuat direktori konfigurasi di: {rout_dir}")
            rout_dir.mkdir()

        # Menyalin file .zshrc default jika di tujuan belum ada
        if not zshrc_dest.exists():
            # Menentukan path sumber zshrc.txt relatif terhadap file ini
            script_dir = Path(__file__).parent
            project_root = script_dir.parent.parent # Mundur dua kali dari core/config ke root
            zshrc_source = project_root / 'config' / 'zshrc.txt'
            
            if zshrc_source.exists():
                print(f"Membuat konfigurasi default zshrc di {zshrc_dest}")
                shutil.copy(zshrc_source, zshrc_dest)
            else:
                print(f"Peringatan: File konfigurasi sumber 'config/zshrc.txt' tidak ditemukan.")

    except Exception as e:
        print(f"Error: Gagal menyiapkan direktori atau file konfigurasi: {e}")

if __name__ == '__main__':
    # Untuk pengujian langsung
    setup_rout_directory()
