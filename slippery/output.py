"""Handling of output formatting."""

from pprint import pformat
from inspect import signature

from .colors import *
from .utils import represent_params, get_line, get_module_name

LINES = '-' * 80
BLUE_LINES = blue(LINES)
ORANGE_LINES = orange(LINES)
CYAN_LINES = cyan(LINES)
GREEN_LINES = green(LINES)


FUNC_HEADER_TEMPLATE = BLUE_LINES + """
{green}File{reset}: {file} [line {line}]: 
{green}Function{reset}: {bold}{func}({reset}{signature}{bold}){reset}
{green}Positional arguments{reset}: {args}
{green}Keyword arguments{reset}: {kwargs}
""" + LINES


def format_function_header(func, args, kwargs):
    args, kwargs = represent_params(args, kwargs)

    info = {
        'file': get_module_name(func),
        'func': func.__name__,
        'line': get_line(func),
        'signature': str(signature(func))[1:-1],  # Strip the parentheses.
        'args': args or '[]',
        'kwargs': kwargs or '[]',
    }

    info.update(**COLORS)

    return FUNC_HEADER_TEMPLATE.format(**info)


RETURN_VALUE_TEMPLATE = "{bold}Return Value{reset}: {green}{result}{reset}"


def format_return_value(result, indent=0, width=80, compact=True):
    result = pformat(result, indent=indent, width=width, compact=compact)

    if len(result.split('\n')) > 1:
        result = '\n{}'.format(result)

    info = {'result': result}
    info.update(**COLORS)

    return RETURN_VALUE_TEMPLATE.format(**info)


EXEC_TIME_TEMPLATE = """
{header}
{bold}Total execution time{reset}: {green}{time:0.8f} Seconds{reset}
{underline}
{result}
""" + BLUE_LINES


def format_exec_time(time, func, args, kwargs, result):
    info = {
        'header': format_function_header(func, args, kwargs),
        'time': time,
        'underline': LINES,
        'result': format_return_value(result),
    }

    info.update(**COLORS)

    return EXEC_TIME_TEMPLATE.format(**info)
