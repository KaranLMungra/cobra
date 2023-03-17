# Cobra

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/b70b09ffd45a47d78215d0e713db7855)](https://app.codacy.com/gh/KaranLMungra/cobra/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

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

![output.png](https://raw.githubusercontent.com/KaranLMungra/cobra/master/output.png)
