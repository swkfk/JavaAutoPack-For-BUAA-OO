from .exception import CompileErrorException
from .executable_path import get_javac

import subprocess
from pathlib import Path


def list_java(src_path: Path) -> [str]:
    return [str(item) for item in src_path.rglob('*.java')]


def __gen_list(root_path: Path):
    (root_path / "sources.list").write_text("\n".join(list_java(root_path / "src")))


def compile_java(root_path: Path, deps: str):
    deps_list = '.' if deps == "" else f'.;{deps}'
    __gen_list(root_path)
    try:
        subprocess.check_output([
            get_javac(),
            '-d', str(root_path / 'build'),
            '-encoding', 'UTF-8',
            '-g',
            '-classpath', deps_list,
            '-sourcepath', str(root_path / 'src'),
            f"@{root_path / 'sources.list'}"
        ], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise CompileErrorException(e.returncode, e.stdout)


if __name__ == '__main__':
    compile_java(Path('tests/WithPackage'), "")
    try:
        compile_java(Path('tests/CompileError'), "")
    except CompileErrorException as e:
        print(e)
