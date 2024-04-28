import zipfile
from pathlib import Path

from GuiCore.settings import get_default_ignore_test


def unzip(zip_file: str, target_path: Path):
    zf = zipfile.ZipFile(zip_file, 'r')
    if not get_default_ignore_test():
        zf.extractall(str(target_path))
    else:
        for item in zf.filelist:
            if item.filename.startswith('test/'):
                continue
            zf.extract(item, str(target_path))
    zf.close()
