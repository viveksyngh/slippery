<a href="https://github.com/lk-geimfari/slippery/">
    <p align="center">
      <img src="https://raw.githubusercontent.com/lk-geimfari/slippery/master/media/logo.png">
    </p>
</a>


**Slippery** - collections of useful decorators for different phases of development software. 
Your code seems works slowly and you have not any idea why it's happen and how to check it? Function returns crazily structured data and you can't find what you need? So, Slippery Stair help with all this problems and another ones. Just decorate function which you need and take a look at result.

## Installation

```
➜  pip install slippery
```

## Usage

For using this library you need to pay 25 schmeckles.

```bash
export SCHMECKLES=25
```

Actually you can use it without paying schmeckles, but... come on! 25 schmeckles for Slippery Stair? Easily!


## Now, seriously

Sometime we need to check out execution time of some function. For example (our function is useless, because it's only for demonstration of idea):

```python
import slippery

@slippery.execution_time
def generator(no=True, maximum=100, registry=None):
    if True:
        do_something()

    if not registry:
        update_something()

    result = [
        k for k in [
            i for i in range(maximum)
        ]
    ]

    return result
    
if __name__ == '__main__':
    generator(True, 100, [1, 2, 3])
```
Result:

![](media/exe_time_dec_screen.png)



When you need more information than returns `@execution_time` decorator, then you should use decorator `@efficiency`:

```python
@slippery.efficiency
def generator(*args, **kwargs):
    # ...

```

Result:

![](media/efficiency_screen.png)


Also you can disassemble function using decorator `@disassemble`:

```python
@slippery.disassemble
def generator():
    result = [
        k for k in [
            i for i in range(20)
        ]
    ]
    result.append([x for x in 'SMAP'])

    return result
```
Result:
```
  7           0 LOAD_CONST               1 (<code object <listcomp> at 0x7ffa622b0a50, file "/home/likid/slippery/example.py", line 7>)
              3 LOAD_CONST               2 ('generator.<locals>.<listcomp>')
              6 MAKE_FUNCTION            0

  8           9 LOAD_CONST               3 (<code object <listcomp> at 0x7ffa622b0d20, file "/home/likid/slippery/example.py", line 8>)
             12 LOAD_CONST               2 ('generator.<locals>.<listcomp>')
             15 MAKE_FUNCTION            0
             18 LOAD_GLOBAL              0 (range)
             21 LOAD_CONST               4 (20)
             24 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             27 GET_ITER
             28 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             31 GET_ITER
             32 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             35 STORE_FAST               0 (result)

 11          38 LOAD_FAST                0 (result)
             41 LOAD_ATTR                1 (append)
             44 LOAD_CONST               5 (<code object <listcomp> at 0x7ffa622bd660, file "/home/likid/slippery/example.py", line 11>)
             47 LOAD_CONST               2 ('generator.<locals>.<listcomp>')
             50 MAKE_FUNCTION            0
             53 LOAD_CONST               6 ('SMAP')
             56 GET_ITER
             57 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             60 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             63 POP_TOP

 13          64 LOAD_FAST                0 (result)
             67 RETURN_VALUE
```

## Disclaimer
Slippery is developed only for developers and only for debugging and testing phases. This library should not used in production, if you don't want unacceptable behaviour of your application.

## Thanks

This library is originally inspired by character (*Slippery Stair*) from `Rick and Morty`. Special thanks for `Mark Lutz` and `Luciano Romalho` for great books about Python.
