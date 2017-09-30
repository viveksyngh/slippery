BOLD = '\033[1m'
RESET = "\033[0m"
GREEN = '\033[92m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[96m'


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


LINES = '------' * 14

BLUE_LINES = blue(LINES)
ORANGE_LINES = orange(LINES)
CYAN_LINES = cyan(LINES)
GREEN_LINES = green(LINES)

# TODO: Simplify it. It's looks unreadable.
OUTPUT_TEMPLATE = BLUE_LINES + '''
\033[1mTotal time\033[0m: \033[92m{time:0.8f} Sec\033[0m.
\033[1mCalled function\033[0m: \033[92m{func}({args}, {kwargs}\033[92m)\033[0m\n
\033[1mResult\033[0m: \033[92m{result}\033[0m.
''' + BLUE_LINES

# TODO: It's too.
DIS_TEMPLATE = """
\033[92mFunction\033[0m: \033[1m{func}(\033[0m{arguments}\033[1m)\033[0m at line {line}.
\033[92mPositional arguments    \033[0m: {args}
\033[92mKeyword arguments\033[0m: {kwargs}
"""

EFF_TEMPLATE = """
\033[92mFunction\033[0m: \033[1m{func}\033[0m at line {line}.
\033[92mPositional arguments    \033[0m: {args}
\033[92mKeyword arguments\033[0m: {kwargs}
"""