from .exception import MainClassDuplicatedException, MainClassNotFoundException

import itertools
import pathlib


def __check__entry(java_file: str) -> bool:
    def line_checker(line: str):
        return line.find("public static void main") != -1

    with open(java_file, 'r') as f:
        return any(map(line_checker, f.readlines()))


def __find_entry(java_list: [str]) -> str:
    checked = list(filter(__check__entry, java_list))
    if len(checked) == 0:
        raise MainClassNotFoundException
    if len(checked) > 1:
        raise MainClassDuplicatedException
    return checked[0]


def __parse_package(java_file: str) -> str:
    class_name = pathlib.Path(java_file).stem

    with open(java_file, "r") as f:
        iterator = itertools.dropwhile(lambda s: not s.strip().startswith('package '), f.readlines())
    try:
        line = next(iterator)
        stmt = "".join(itertools.takewhile(lambda c: not c == ';', line.strip()))
        package = stmt.removeprefix('package ')
        return package + "." + class_name
    except StopIteration:
        return class_name


def get_main_class(java_list: [str]) -> str:
    entry_file = __find_entry(java_list)
    return __parse_package(entry_file)


if __name__ == '__main__':
    print(get_main_class(["tests/NoPackage/Main.java"]))
    print(get_main_class(["tests/WithPackage/src/MainClass.java", "tests/WithPackage/src/Tools.java"]))
    try:
        print(get_main_class(["tests/NoMainClass/Main.java"]))
    except MainClassNotFoundException as e:
        print(e)
    try:
        print(get_main_class(["tests/DuplicatedMainClass/Main1.java", "tests/DuplicatedMainClass/Main2.java"]))
    except MainClassDuplicatedException as e:
        print(e)
