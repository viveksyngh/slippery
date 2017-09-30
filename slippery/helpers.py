"""Here we modify some objects (which originally written by James Roskind)
from standard library for support colored output.
"""
from pstats import Stats, func_get_function_name
import slippery.output as o


# TODO: Awful! Refactor it all


def f8(x):
    return "\033[34m%8.3f\033[0m" % x


def func_std_string(func_name):
    if func_name[:2] == ('~', 0):
        name = func_name[2]
        if name.startswith('<') and name.endswith('>'):
            return '{%s}' % o.blue(name[1:-1])
        else:
            return name
    else:
        return o.blue("%s:%d(%s)") % func_name


class CustomStats(Stats):
    def print_title(self):
        row = 'ncalls  tottime  percall  cumtime  percall'
        print(o.green('   ' + row), end=' ', file=self.stream)
        print(o.green('filename:line(function)'), file=self.stream)

    def print_line(self, func):
        cc, nc, tt, ct, callers = self.stats[func]
        c = str(nc)

        if nc != cc:
            c = c + '/' + str(cc)
        print(c.rjust(9), end=' ', file=self.stream)
        print(f8(tt), end=' ', file=self.stream)

        if nc == 0:
            print(' ' * 8, end=' ', file=self.stream)
        else:
            print(f8(tt / nc), end=' ', file=self.stream)
        print(f8(ct), end=' ', file=self.stream)

        if cc == 0:
            print(' ' * 8, end=' ', file=self.stream)
        else:
            print(f8(ct / cc), end=' ', file=self.stream)
        print(func_std_string(func), file=self.stream)

    def print_stats(self, *amount):
        for filename in self.files:
            print(filename, file=self.stream)
        if self.files:
            print(file=self.stream)
        indent = ' ' * 2
        for func in self.top_level:
            print(indent, func_get_function_name(func), file=self.stream)

        print(indent, o.green('{} function calls'.format(self.total_calls)),
              end=' ', file=self.stream)
        if self.total_calls != self.prim_calls:
            print("(%d primitive calls)" % self.prim_calls, end=' ', file=self.stream)
        print("in \033[33m{:.8f} \033[92mseconds\033[0m.".format(self.total_tt), file=self.stream)
        print(file=self.stream)
        width, list = self.get_print_list(amount)
        if list:
            self.print_title()
            for func in list:
                self.print_line(func)
            print(file=self.stream)
            print(file=self.stream)
        return self
