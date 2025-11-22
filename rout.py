#!/usr/bin/env python3
import os
import sys
import importlib.util
from pathlib import Path
from ui.motd.motd import display_welcome_message
from core.config.fConfig import setup_rout_directory

# Dictionary untuk menyimpan perintah yang ditemukan
commands = {}

def load_commands():
    """
    Memuat perintah secara dinamis dari direktori 'cmd'.
    """
    cmd_dir = Path(__file__).parent / 'cmd'
    if not cmd_dir.is_dir():
        print("Peringatan: Direktori 'cmd' tidak ditemukan.")
        return

    # Cari semua file .py di direktori cmd
    for file_path in cmd_dir.glob('*.py'):
        # Abaikan file seperti __init__.py
        if file_path.stem.startswith('__'):
            continue

        command_name = file_path.stem
        module_name = f"cmd.{command_name}"

        try:
            # Impor modul secara dinamis
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Cari fungsi 'execute' di dalam modul
            if hasattr(module, 'execute') and callable(module.execute):
                commands[command_name] = module.execute
            else:
                print(f"Peringatan: Perintah '{command_name}' tidak memiliki fungsi execute().")
        except Exception as e:
            print(f"Error saat memuat perintah '{command_name}': {e}")

def main():
    """
    Fungsi utama untuk CLI rout.
    Memuat perintah, dan menjalankan perintah yang diberikan atau membuka shell Zsh.
    """
    # Menyiapkan direktori dan memuat perintah
    setup_rout_directory()
    load_commands()

    # Memeriksa apakah ada argumen baris perintah yang diberikan
    if len(sys.argv) > 1:
                    command_name = sys.argv[1]
                    if command_name in commands:
                        # Jalankan fungsi execute() dari perintah yang sesuai, teruskan argumen
                        command_args = sys.argv[2:]
                        commands[command_name](*command_args)
                    else:
                        print(f"Error: Perintah tidak dikenal '{command_name}'")
                        print("Perintah yang tersedia:")
                        for cmd in sorted(commands):                print(f"  {cmd}")
    else:
        # Jika tidak ada argumen, tampilkan pesan selamat datang dan mulai shell Zsh
        display_welcome_message()
        home_dir = os.path.expanduser("~")
        zdotdir = os.path.join(home_dir, '.rout')
        os.system(f'ZDOTDIR="{zdotdir}" zsh')

if __name__ == "__main__":
    main()
