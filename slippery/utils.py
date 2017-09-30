from slippery import output as o


# TODO: Refactoring.

def represent_params(args, kwargs):
    kwargs = ', '.join(
        ['{k}{t}{v}'.format(
            k=o.orange(k),
            v=o.orange(v),
            t=o.blue('='),
        ) for k, v in kwargs.items()]
    )
    args = ', '.join([o.orange(str(arg)) for arg in args])

    return args, kwargs


def get_line(fn):
    string = str(fn.__code__).split(' ')[-1::][0]
    string = string.replace('>', '')
    return int(string) + 1


def get_module_name(fn):
    mod = str(fn.__code__).split(' ')[-3::][0]
    return mod.replace(',', '')


# TODO: This function should short big list, tuple, set, dict.
# TODO: This function is internal for decorator @prettify
# Examples:
#    {x for x in range(1000)} should be: {1, 2, 3, ...}
#    [x for x in range(1000)] should be: [1, 2, 3, ...]
def shortened():
    pass
