import shutil
from pathlib import Path


def copy_jar(root_path: Path, ident: str):
    shutil.copy(str(root_path / f'{ident}.jar'), str(root_path.parent / f'{ident}.jar'))
