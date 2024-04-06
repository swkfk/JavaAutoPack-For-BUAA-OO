import os
import shutil
import subprocess
from pathlib import Path


def extract_jar(jar_file: str, target_path: Path):
    shutil.copy(jar_file, str(target_path / 'deps.jar'))

    old_dir = os.getcwd()
    os.chdir(str(target_path))
    subprocess.check_output([
        'jar',
        'xf', 'deps.jar'
    ], stderr=subprocess.STDOUT)
    os.chdir(old_dir)
