import typing


def __color_factory(code: str) -> typing.Callable:
    def inner(s: str) -> str:
        return f"\033[{code}{s}\033[0m"

    return inner


Red = __color_factory('31m')
Green = __color_factory('32m')
Yellow = __color_factory('33m')
Blue = __color_factory('34m')
Pink = __color_factory('35m')
Cyan = __color_factory('36m')
