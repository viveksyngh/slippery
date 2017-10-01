"""Function decorators implementation."""
import dis
import sys
import time
import cProfile
import functools

import slippery.templates as t
from .helpers import CustomStats

__all__ = [
    'efficiency',
    'execution_time',
    'disassemble',
    'prettify'
]


def execution_time(func):
    """Measure execution time for the decorated function."""

    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        run_time = time.time() - start_time

        printo(t.format_exec_time(run_time,
                                 func,
                                 args,
                                 kwargs,
                                 result))

        return result

    return inner


def disassemble(func):
    """Print the decorated's function disassembly."""

    @functools.wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)

        print(t.format_function_header(func, args, kwargs))
        dis.dis(func)
        print(t.BLUE_LINES)

        return result

    return inner


def efficiency(func):
    """Run the decorated function within a cProfile measurement."""

    @functools.wraps(func)
    def inner(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        try:
            result = func(*args, **kwargs)
        finally:
            profiler.disable()

            print(t.format_function_header(func, args, kwargs))
            stats = CustomStats(profiler, stream=sys.stdout)
            stats.print_stats()
            print(t.BLUE_LINES)

        return result

    return inner


def prettify(indent=0, width=80, compact=True):
    """Return a decorator that prints the function call nicely.

    The values of `indent`, `width` and `compact` are taking effect only on the
    function's return value.
    """

    def decorate(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)

            print(t.format_function_header(func, args, kwargs))
            print(t.format_return_value(result, indent, width, compact))
            print(t.BLUE_LINES)

            return result

        return inner

    return decorate
