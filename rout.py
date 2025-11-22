#!/usr/bin/env python3
import os
from ui.motd.motd import display_welcome_message
from core.config.fConfig import setup_rout_directory

def main():
    """
    Fungsi utama untuk CLI rout.
    Menampilkan pesan selamat datang dan membuka shell Zsh.
    """
    # Menyiapkan direktori konfigurasi terlebih dahulu
    setup_rout_directory()

    display_welcome_message()
    # Memulai sesi shell Zsh
    os.system('zsh')

if __name__ == "__main__":
    main()
