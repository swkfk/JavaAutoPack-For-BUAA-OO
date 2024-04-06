import zipfile
from pathlib import Path


def unzip(zip_file: str, target_path: Path):
    zf = zipfile.ZipFile(zip_file, 'r')
    zf.extractall(str(target_path))
    zf.close()
