from string import Template

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

OUTPUT_TEMPLATE = Template(
    '''
    ${BLUE_LINE}
    ${BOLD}Total time${RESET}: ${GREEN}{time:0.8f} Sec${RESET}.
    ${BOLD}Called function${RESET}: ${GREEN}{func}({args}, {kwargs}${GREEN})${RESET}\n
    ${BOLD}Result${RESET}: ${GREEN}{result}${RESET}.
    ${BLUE_LINE}
    '''
).safe_substitute(
    BLUE_LINE=BLUE_LINES,
    BOLD=BOLD,
    RESET=RESET,
    GREEN=GREEN,
    ORANGE=ORANGE,
    BLUE=BLUE,
    CYAN=CYAN
)

DIS_TEMPLATE = Template(
    '''
    ${GREEN}Function${RESET}: ${BOLD}{func}(${RESET}{arguments}${BOLD})${RESET} at line {line}.
    ${GREEN}Positional arguments    ${RESET}: {args}
    ${GREEN}Keyword arguments${RESET}: {kwargs}
    '''
).safe_substitute(
    BLUE_LINE=BLUE_LINES,
    BOLD=BOLD,
    RESET=RESET,
    GREEN=GREEN,
    ORANGE=ORANGE,
    BLUE=BLUE,
    CYAN=CYAN
)
