from dbg import Dbg


@Dbg
def pow(x: int, y: int, **kwargs) -> int:
    _ = kwargs
    result = x ** y
    return result


if __name__ == '__main__':
    print(pow(pow(pow(2, 2, a='2'), 3), 5))
