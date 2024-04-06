from .exception import CompileErrorException

import subprocess
from pathlib import Path


def __write_manifest(root_path: Path, main_class: str):
    meta_path = root_path / 'build' / 'META-INF'
    meta_path.mkdir(exist_ok=True)
    (meta_path / 'MANIFEST.MF').write_text(f'Manifest-Version: 1.0\nMain-Class: {main_class}\nCreated-By: kai_Ker')

def make_jar(root_path: Path, ident: str, main_class: str):
    __write_manifest(root_path, main_class)
    try:
        subprocess.check_output([
            'jar', 'cvfm',
            str(root_path / f'{ident}.jar'),
            str(root_path / 'build' / 'META-INF' / 'MANIFEST.MF'),
            '-C', str(root_path / 'build'), '.'
        ], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise CompileErrorException(e.returncode, e.stdout)


if __name__ == '__main__':
    make_jar(Path('tests/WithPackage'), 'WithPackage', 'src.MainClass')
