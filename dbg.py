from typing import Callable
import inspect


def __rgb(r: int = 255, b: int = 255, g: int = 255, mode=False):
    return f'\x1b[{48 if mode else 38};2;{r};{g};{b}m'


__MONOKAI_COLOR_PALLETE = {
    'Background': __rgb(46, 46, 46),  # 2e2e2e
    'Comments': __rgb(121, 121, 121),  # 797979
    'White': __rgb(255, 255, 255),  # fffff only color changed
    'Yellow': __rgb(229, 181, 103),  # e5b567
    'Green': __rgb(180, 210, 115),  # b4d273
    'Orange': __rgb(232, 125, 62),  # e87d3e
    'Purple': __rgb(158, 134, 200),  # 9e86c8
    'Pink': __rgb(176, 82, 121),  # b05279
    'Blue': __rgb(108, 153, 187),  # 6c99bb
}


def __kwargs_str(**kwargs) -> str:
    return ''.join(map(lambda kwarg: f', {kwarg[0]} = {__MONOKAI_COLOR_PALLETE["Green"]}{kwarg[1].__repr__()}{__MONOKAI_COLOR_PALLETE["White"]}', kwargs.items()))


def __args_str(args: list[str], *values) -> str:
    return ''.join(map(lambda arg: f', {arg[1]} = {__MONOKAI_COLOR_PALLETE["Green"]}{values[arg[0]].__repr__()}{__MONOKAI_COLOR_PALLETE["White"]}' if arg[0] else
                       f'{arg[1]} = {__MONOKAI_COLOR_PALLETE["Green"]}{values[arg[0]]}{__MONOKAI_COLOR_PALLETE["White"]}', enumerate(args)))


def Dbg(f: Callable):
    fnargs = list(f.__annotations__.keys())[:-1]

    def wrapper(*args, **kwargs):
        stack = inspect.stack()
        result = f(*args, **kwargs)
        print(
            f'{__MONOKAI_COLOR_PALLETE["Yellow"]}[{stack[1].filename}]{__MONOKAI_COLOR_PALLETE["Pink"]}({stack[1].lineno}){__MONOKAI_COLOR_PALLETE["Blue"]}{f.__qualname__}{__MONOKAI_COLOR_PALLETE["White"]}({__args_str(fnargs,*args)}{__kwargs_str(**kwargs)})-> {__MONOKAI_COLOR_PALLETE["Green"]}{result.__repr__()}{__MONOKAI_COLOR_PALLETE["White"]}')
        return result
    return wrapper
