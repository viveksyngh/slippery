from string import Template

BOLD = '\033[1m'
RESET = "\033[0m"
GREEN = '\033[92m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[96m'


class LinesPrinter:
    """
        Prints colored lines before and after what you want.
        
        Usage:
        >>> with LinesPrinter() as lp:
        >>>     print("Lorem ipsum...")
        
        Will print a line before and after "Lorem ipsum...".
        Use the "line()" method to print another line inside.
    """
    
    def __init__(self, color='b', end='\n'):
        # TODO : Modify with "clr(message, 'g')" (WIP).
        self.color = {
            'B': BOLD,
            'b': BLUE,
            'g': GREEN,
            'o': ORANGE,
            'b': BLUE,
            'c': CYAN,
        }.get(color)
        self.reset = RESET
        self.end = end
    
    def __enter__(self):
        self.line(self.end)
        return self
    
    def __exit__(self, type, value, traceback):
        self.line(self.end)
    
    def line(self, end='\n'):
        # TODO : Modify with "clr(message, 'g')" (WIP).
        print('{}{}{}'.format(self.color, LINES, self.reset), end=end)


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

EFF_TEMPLATE = Template(
    '''
   ${GREEN}Function${RESET}: ${BOLD}{func}${RESET} at line {line}.
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

# EFF_TEMPLATE = """
# \033[92mFunction\033[0m: \033[1m{func}\033[0m at line {line}.
# \033[92mPositional arguments    \033[0m: {args}
# \033[92mKeyword arguments\033[0m: {kwargs}
# """

