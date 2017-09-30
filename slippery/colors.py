"""Ansi color codes."""
RESET = '\033[0m'
BOLD = '\033[1m'
GREEN = '\033[92m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[96m'


COLORS = {
    'bold': BOLD,
    'reset': RESET,
    'green': GREEN,
    'orange': ORANGE,
    'blue': BLUE,
    'cyan': CYAN,
}


def color(msg, clr):
    return '{}{}{}'.format(COLORS[clr], msg, RESET)


# TODO: Change color schema for messages and simplify format.
# TODO: Should be: clr(message, 'g') where g is green
def bold(st):
    return '{}{}{}'.format(BOLD, st, RESET)


def green(st):
    return '{}{}{}'.format(GREEN, st, RESET)


def orange(st):
    return '{}{}{}'.format(ORANGE, st, RESET)


def blue(st):
    return '{}{}{}'.format(BLUE, st, RESET)


def cyan(st):
    return '{}{}{}'.format(CYAN, st, RESET)
