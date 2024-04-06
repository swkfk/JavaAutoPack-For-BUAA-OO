import subprocess
from pathlib import Path


class CompileErrorException(Exception):
    def __init__(self, return_code: int, stderr: str | bytes):
        if type(stderr) == str:
            self.stderr = stderr
        else:
            self.stderr = stderr.decode('utf-8', errors='replace')
        self.return_code = return_code

    def __str__(self):
        return f"编译错误，编译器返回值：{self.return_code}\n{self.stderr}"


def __list_java(src_path: Path) -> [str]:
    return [str(item) for item in src_path.rglob('*.java')]


def __gen_list(root_path: Path):
    (root_path / "sources.list").write_text("\n".join(__list_java(root_path / "src")))


def compile_java(root_path: Path):
    __gen_list(root_path)
    try:
        subprocess.check_output([
            'javac',
            '-d', str(root_path / 'build'),
            '-sourcepath', str(root_path / 'src'),
            f"@{root_path / 'sources.list'}"
        ], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise CompileErrorException(e.returncode, e.stdout)


if __name__ == '__main__':
    compile_java(Path('tests/WithPackage'))
    try:
        compile_java(Path('tests/CompileError'))
    except CompileErrorException as e:
        print(e)
