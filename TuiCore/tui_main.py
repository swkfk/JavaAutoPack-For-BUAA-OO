import shutil

from AutoPackCore import get_main_class, make_jar, compile_java, unzip, list_java, copy_jar
from AutoPackCore import MainClassDuplicatedException, MainClassNotFoundException, CompileErrorException
from .colorize import *

from pathlib import Path

def __retry(fn, check):
    ret = fn()
    while not check(ret):
        print(Red("似乎不太对哦~"))
        ret = fn()
    return ret

def __starter():
    print(f'{Cyan("JavaAutoPack Made by ")}{Blue("kai_Ker")}')
    print()
    print(f'{Yellow("请确保 ")}{Pink("javac")}{Yellow(" 与 ")}{Pink("jar")}{Yellow(" 命令可用，当前版本不支持定制")}')
    print(f'{Yellow("打包完成后，相关文件将会存放在 ")}{Pink("Generated")}{Yellow(" 文件夹中")}')
    print()

def __input_hint():
    print(f'{Yellow("下面，你只需要提供从网站上下载的")}{Pink("压缩包")}{Yellow("就行，直接拖过来！")}')
    print(f'{Yellow("遇到你自己怎么办？直接")}{Pink("回车")}{Yellow("就行！")}')
    print(f'{Yellow("想结束怎么办？直接 ")}{Pink("Ctrl-D")} {Yellow(" 或者 ")}{Pink("Ctrl-Z Enter")}{Yellow(" 就行！")}')
    print()

def __get_zip(nick: str):
    print()
    return input(f'{Cyan(nick)}: ')

def TuiMain(names: [str, str]):
    root_path = Path('Generated')
    root_path.mkdir(exist_ok=True)

    __starter()

    __input_hint()

    for ident, nick in names:
        try:
            zip_file = __retry(lambda: __get_zip(nick), lambda x: x.strip() == "" or Path(x).is_file())
        except EOFError:
            break

        if zip_file.strip() == "":
            print(Pink("Skipped!"))
            continue

        person_root_path = root_path / ident
        if person_root_path.exists():
            print(f'{Yellow("  清空目标文件夹：")}{Pink(str(person_root_path))}')
            shutil.rmtree(str(person_root_path))
        person_root_path.mkdir(exist_ok=False)

        (person_root_path / 'src').mkdir(exist_ok=False)
        try:
            unzip(zip_file, person_root_path / 'src')
        except Exception as e:
            print(Red(repr(e)), Pink("Skip!"))
            continue

        try:
            main_class = get_main_class(list_java(person_root_path / 'src'))
            print(f'{Yellow("  主类：")}{Pink(main_class)}')
        except MainClassNotFoundException as e:
            print(Red(str(e)))
            main_class = input(Cyan("  主类："))
        except MainClassDuplicatedException as e:
            print(Red(str(e)))
            main_class = input(Cyan("  主类："))

        try:
            (person_root_path / 'build').mkdir(exist_ok=False)
            compile_java(person_root_path)
            make_jar(person_root_path, ident, main_class)
        except CompileErrorException as e:
            print(Red(str(e)), Pink("Skip!"))
            continue

        try:
            copy_jar(person_root_path, ident)
            print(f'{Yellow("  已生成：")}{Pink(str(root_path / ident) + ".jar")}')
        except Exception as e:
            print(Red(repr(e)), Pink("Skip!"))
            continue
