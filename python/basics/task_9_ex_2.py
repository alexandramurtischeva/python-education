def foo(a, b, c, *args) -> int:
    return len(args)


def bar(a, b, c, **kwargs) -> bool:
    if kwargs["magicnumber"] == 7:
        return True
    return False
