import os
import stat
from pathlib import Path

def generate_command_wrappers(rout_dir: Path, project_root: Path):
    """
    Membuat skrip wrapper yang dapat dieksekusi untuk setiap perintah di direktori 'cmd'.
    """
    cmd_dir = project_root / 'cmd'
    bin_dir = rout_dir / 'bin'
    rout_py_path = project_root / 'rout.py'

    bin_dir.mkdir(exist_ok=True)

    if not cmd_dir.is_dir():
        return

    for file_path in cmd_dir.glob('*.py'):
        if file_path.stem.startswith('__'):
            continue
        
        command_name = file_path.stem
        wrapper_path = bin_dir / command_name
        
        wrapper_content = f"""#!/bin/sh
# Wrapper untuk perintah rout: {command_name}
python3 "{rout_py_path.resolve()}" {command_name} "$@"
"""
        
        with open(wrapper_path, 'w') as f:
            f.write(wrapper_content)
        
        # Membuat file dapat dieksekusi (chmod +x)
        st = os.stat(wrapper_path)
        os.chmod(wrapper_path, st.st_mode | stat.S_IEXEC)
