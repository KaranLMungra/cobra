# Cobra

An easy-to-use and powerful debug/logger library. Still in development phase but
hopefully will be ready soon enough for usage.

```python
@Dbg
def pow(x: int, y: int, **kwargs) -> int:
    _ = kwargs
    result = x ** y
    return result


if __name__ == '__main__':
    print(pow(pow(pow(2, 2, a='2'), 3), 5))
```

[output.png](/output.png)
