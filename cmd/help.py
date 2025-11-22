from pathlib import Path

def execute(*args):
    """
    Menampilkan daftar semua perintah yang tersedia di direktori 'cmd'.
    """
    print("Selamat datang di rout CLI!")
    print("Berikut adalah daftar perintah yang tersedia:")

    try:
        # Path ke direktori 'cmd' relatif terhadap file ini
        cmd_dir = Path(__file__).parent
        
        commands = []
        for file_path in cmd_dir.glob('*.py'):
            # Abaikan file seperti __init__.py
            if not file_path.stem.startswith('__'):
                commands.append(file_path.stem)
        
        # Cetak daftar perintah yang telah diurutkan
        if commands:
            for command_name in sorted(commands):
                print(f"  - {command_name}")
        else:
            print("  (Tidak ada perintah yang ditemukan)")
            
    except Exception as e:
        print(f"Error saat mencari perintah: {e}")
