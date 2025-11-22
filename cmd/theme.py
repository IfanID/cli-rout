import os
from pathlib import Path

VALID_THEMES = [
    "af-magic", "afowler", "agnoster", "alanpeabody", "amuse", "apple", "arrow",
    "aussiegeek", "avit", "awesomepanda", "bira", "blinks", "bureau", "candy",
    "clean", "cloud", "crcandy", "crunch", "cypher", "dallas", "darkblood",
    "daveverwer", "dieter", "dogenpunk", "dpoggi", "dst", "dstufft", "duellj",
    "eastwood", "edvardm", "emotty", "essembeh", "evan", "fino-time", "fino",
    "fishy", "flazz", "fletcherm", "fox", "frisk", "frontcube", "funky",
    "fwalch", "gallifrey", "gallois", "garyblessington", "gentoo",
    "geoffgarside", "gianu", "gnzh", "gozilla", "half-life", "humza", "imajes",
    "intheloop", "itchy", "jaischeema", "jbergantine", "jispwoso", "jnrowe",
    "jonathan", "josh", "jreese", "jtriley", "juanghurtado", "junkfood",
    "kafeitu", "kardan", "kennethreitz", "kolo", "kphoen", "lambda",
    "linuxonly", "lukerandall", "macovsky", "maran", "mgutz", "mh",
    "michelebologna", "mikeh", "miloshadzic", "minimal", "mortalscumbag",
    "mrtazz", "murilasso", "muse", "nanotech", "nebirhos", "nicoulaj", "norm",
    "obraun", "peepcode", "philips", "pmcgee", "pygmalion", "re5et", "refined",
    "rgm", "risto", "rixius", "rkj", "sammy", "simonoff", "simple", "skaro",
    "smt", "Soliah", "sonicradish", "sorin", "sporty_256", "steeef", "strug",
    "sunaku", "sunrise", "superjarin", "suvash", "takashiyoshida",
    "terminalparty", "theunraveler", "tjkirch", "tonotdo", "trapd00r",
    "wedisagree", "wezm", "wezm+", "wuffers", "xiong-chiamiov",
    "xiong-chiamiov-plus", "ys", "zhann"
]

def execute(*args):
    """
    Mengubah tema Zsh atau menampilkan daftar tema yang tersedia.
    """
    if args and args[0] == 'list':
        print("Daftar tema Zsh yang tersedia:")
        
        # Kelompokkan tema berdasarkan huruf pertama
        themed_dict = {}
        for theme in sorted(VALID_THEMES):
            first_letter = theme[0].upper()
            if first_letter not in themed_dict:
                themed_dict[first_letter] = []
            themed_dict[first_letter].append(theme)
            
        # Cetak tema yang dikelompokkan dan diurutkan berdasarkan abjad
        for letter, themes in sorted(themed_dict.items()):
            print(f"\n--- {letter} ---")
            # Mencetak tema dalam beberapa kolom untuk keterbacaan
            try:
                col_width = max(len(theme) for theme in themes) + 4
                term_width = os.get_terminal_size().columns
                cols = max(1, term_width // col_width)
            except OSError: # Gagal mendapatkan ukuran terminal (misalnya, dalam non-interaktif)
                cols = 3

            for i in range(0, len(themes), cols):
                line = "".join(f"{theme:<{col_width}}" for theme in themes[i:i+cols])
                print(line)
        return

    if args:
        print(f"Error: Sub-perintah tidak dikenal '{args[0]}'")
        print("Penggunaan: rout theme [list]")
        return

    home_dir = Path.home()
    zshrc_path = home_dir / '.rout' / '.zshrc'

    if not zshrc_path.is_file():
        print(f"Error: File konfigurasi '{zshrc_path}' tidak ditemukan.")
        return

    try:
        # Baca tema saat ini dari file .zshrc
        current_theme = "tidak diketahui"
        with open(zshrc_path, 'r') as f:
            for line in f:
                if line.strip().startswith('ZSH_THEME='):
                    current_theme = line.split('=')[1].strip().strip('"')
                    break
        
        print(f"Info: Tema saat ini adalah '{current_theme}'.")
        
        theme_name = input("Tema baru (kosongkan untuk batal): ").strip()

        if not theme_name:
            print("Dibatalkan.")
            return

        if theme_name not in VALID_THEMES:
            print(f"Error: Tema '{theme_name}' tidak valid.")
            print("Gunakan 'rout theme list' untuk melihat daftar tema yang tersedia.")
            return

        with open(zshrc_path, 'r') as f:
            lines = f.readlines()

        new_lines = []
        theme_updated = False
        for line in lines:
            if line.strip().startswith('ZSH_THEME='):
                new_lines.append(f'ZSH_THEME="{theme_name}"\n')
                theme_updated = True
            else:
                new_lines.append(line)

        if not theme_updated:
            # Jika ZSH_THEME tidak ada, tambahkan di awal
            new_lines.insert(0, f'ZSH_THEME="{theme_name}"\n')

        with open(zshrc_path, 'w') as f:
            f.writelines(new_lines)

        print(f"Tema Zsh telah diubah menjadi '{theme_name}'.")
        print("Silakan mulai ulang shell Anda agar perubahan diterapkan.")

    except Exception as e:
        print(f"Terjadi error saat mengubah tema: {e}")
