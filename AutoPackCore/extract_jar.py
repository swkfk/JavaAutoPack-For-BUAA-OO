import os
import shutil
import subprocess
from pathlib import Path

from .executable_path import get_jar


def extract_jar(jar_file: str, target_path: Path):
    shutil.copy(jar_file, str(target_path / 'deps.jar'))

    old_dir = os.getcwd()
    os.chdir(str(target_path))
    subprocess.check_output([
        get_jar(), 'xf', 'deps.jar'
    ], stderr=subprocess.STDOUT)
    os.chdir(old_dir)
