import re
import inspect

from .colors import orange, blue


def escape_ansi(string):
    regex = r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]'
    return re.compile(regex).sub(
        '', string,
    )


def represent_params(args, kwargs):
    kwargs = ', '.join([
        '{k}{eq}{v}'.format(
            k=orange(k),
            eq=blue('='),
            v=orange(v))
        for k, v in kwargs.items()]
    )
    args = ', '.join([orange(str(arg)) for arg in args])

    return args, kwargs


def get_line(fn):
    return inspect.getsourcelines(fn)[1] + 1


def get_module_name(fn):
    return inspect.getmodule(fn).__file__[:-1]


def shortened(seq, max_len=10):
    copy, sw, ew = None, '', ''

    if len(seq) > max_len and seq:
        if isinstance(seq, dict):
            copy = {}
            for key in list(seq.keys())[:max_len]:
                copy[key] = seq[key]
            sw, ew = '{', '}'
        elif isinstance(seq, list):
            copy = seq[:max_len]
            sw, ew = '[', ']'
        elif isinstance(seq, tuple):
            copy = seq[:max_len]
            sw, ew = '(', ')'

        sstr = str(copy)[1:-1]

        return '{sw}{sstr}, ...{ew}'.format(
            sw=sw,
            sstr=sstr,
            ew=ew,
        )
    else:
        return str(seq)
