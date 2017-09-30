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


# TODO: Write unittest
def shortened(fn):
	number_of_elements = 3
	if isinstance(fn, dict):
		print_copy = dict()
		length = len(fn.keys())
		for key in list(fn.keys())[:number_of_elements]:
			print_copy[key] = fn[key]
		startwith, endwith = '{', '}'

	else:
		length = len(fn)
		print_copy = list(fn)[:number_of_elements]
		if isinstance(fn, list):
			startwith, endwith = '[', ']'
		elif isinstance(fn, tuple):
			startwith, endwith = '(', ')'
		elif isinstance(fn, set):
			startwith, endwith = '{', '}'
		elif not inspect.isfunction(fn):
			raise TypeError("Input is not a function.")

	if length > number_of_elements:
		return startwith +  str(print_copy)[1:-1] + ", ..." + endwith
	else:
		return startwith + str(print_copy)[1:-1] + endwith
