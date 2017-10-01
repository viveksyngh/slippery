"""Handling of output formatting."""
from string import Template
from pprint import pformat
from inspect import signature

from .colors import *
from .utils import represent_params, get_line, get_module_name


LINES = '-' * 80
BLUE_LINES = blue(LINES)
ORANGE_LINES = orange(LINES)
CYAN_LINES = cyan(LINES)
GREEN_LINES = green(LINES)


class LinesPrinter(object):
    """Print colored lines before and after what you want.

    Usage:
        >>> with LinesPrinter('blue'):
        >>>     print("Lorem ipsum...")

        Will print a line before and after "Lorem ipsum...".
        Use the "line()" method to print another line inside.
    """

    def __init__(self, color='blue', end='\n'):
        self.color = color
        self.end = end

    def __enter__(self):
        self.line(self.end)
        return self

    def __exit__(self, type, value, traceback):
        self.line(self.end)

    def line(self, end='\n'):
        print(color_line(LINES, self.color), end=end)


FUNC_HEADER_TEMPLATE = Template(BLUE_LINES + """
${green}File${reset}: {file} [line {line}]: 
${green}Function${reset}: ${bold}{func}(${reset}{signature}${bold})${reset}
${green}Positional arguments${reset}: {args}
${green}Keyword arguments${reset}: {kwargs}
""" + LINES).safe_substitute(**COLORS)


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

    return FUNC_HEADER_TEMPLATE.format(**info)


RETURN_VALUE_TEMPLATE = Template(
    "${bold}Return Value${reset}: ${green}{result}${reset}"
).safe_substitute(**COLORS)


def format_return_value(result, indent=0, width=80, compact=True):
    result = pformat(result, indent=indent, width=width, compact=compact)

    if len(result.split('\n')) > 1:
        result = '\n{}'.format(result)

    return RETURN_VALUE_TEMPLATE.format(result=result)


EXEC_TIME_TEMPLATE = Template("""
{header}
${bold}Total execution time${reset}: ${green}{time:0.8f} Seconds${reset}
${underline}
{result}
""" + BLUE_LINES).safe_substitute(underline=LINES, **COLORS)


def format_exec_time(time, func, args, kwargs, result):
    info = {
        'header': format_function_header(func, args, kwargs),
        'time': time,
        'result': format_return_value(result),
    }

    return EXEC_TIME_TEMPLATE.format(**info)
