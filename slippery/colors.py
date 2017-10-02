from .constants import *

COLORS = {
    'bold': BOLD,
    'reset': RESET,
    'green': GREEN,
    'orange': ORANGE,
    'blue': BLUE,
    'cyan': CYAN,
}

def color_line(msg, clr):
    return '{}{}{}'.format(COLORS[clr], msg, RESET)


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
