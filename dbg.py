from typing import Callable
import inspect
import sys
import os


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

kwargs_output = ', {kwarg} = {}{kwarg_value}{}'
args_output = '{arg} = {}{value}{}'
dbg_output ='{}[{filename}]{}({lineno}){}{name}{}({args}{kwargs})->{}{result}{}'
def supports_color(color: str) -> str:
    """
    Returns True if the running system's terminal supports color, and False
    otherwise.
    """
    plat = sys.platform
    supported_platform = plat != 'Pocket PC' and (plat != 'win32' or
                                                  'ANSICON' in os.environ)
    is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    return color if supported_platform and is_a_tty else ''


def __kwargs_str(**kwargs) -> str:
    return ''.join(map(lambda x:
                       kwargs_output.format(supports_color(__MONOKAI_COLOR_PALLETE["Green"]),
                                            supports_color(__MONOKAI_COLOR_PALLETE["White"]), kwarg=x[0],
                                                      kwarg_value=x[1].__repr__()), kwargs.items()))


def __args_str(args: list[str], *values) -> str:
    return ''.join(map(lambda arg: ', ' +
                       args_output.format(__MONOKAI_COLOR_PALLETE["Blue"],
                                          __MONOKAI_COLOR_PALLETE["White"], arg=arg[1],
                                                      value=values[arg[0]]) if arg[0] else
                       args_output.format(__MONOKAI_COLOR_PALLETE["Blue"],
                                         __MONOKAI_COLOR_PALLETE["White"],
                                          arg=arg[1], value=values[arg[0]]),
                       enumerate(args)))


def Dbg(f: Callable):
    fnargs = list(f.__annotations__.keys())[:-1]

    def wrapper(*args, **kwargs):
        stack = inspect.stack()
        result = f(*args, **kwargs)
        print(dbg_output.format(__MONOKAI_COLOR_PALLETE['Yellow'],
                                 __MONOKAI_COLOR_PALLETE['Pink'],
                                 __MONOKAI_COLOR_PALLETE['Blue'],
                                 __MONOKAI_COLOR_PALLETE['White'],
                                 __MONOKAI_COLOR_PALLETE['Green'],
                                 __MONOKAI_COLOR_PALLETE['White'],
                                 filename=stack[1].filename,
                                 lineno=stack[1].lineno, name=f.__qualname__,
                                 args=__args_str(fnargs, *args),
                                 kwargs=__kwargs_str(**kwargs),
                                result=result.__repr__()))
        return result
    return wrapper
