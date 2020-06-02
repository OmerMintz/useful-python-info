

def decorator(*decorator_optional_args, **decorator_keyword_args):

    # this section runs once, when a function is decorated by '@decorator(*args, **kwargs)'

    def inner_decorator(function):

        # this section runs once, when a function is decorated by '@decorator(*args, **kwargs)'

        def inner_function(*function_optional_args, **function_keyword_args):

            # this section runs every time 'function' is called
            # here you should use 'decorator_optional_args' and 'decorator_keyword_args'

            # example
            print(f"\ninvoking {function.__name__}")
            if 'symbol' in decorator_keyword_args and len(decorator_optional_args) > 0:
                print(decorator_optional_args[0] * decorator_keyword_args['symbol'])

            # this is the call to function. it should be left untouched.
            function(*function_optional_args, **function_keyword_args)

            # example - continued
            if 'symbol' in decorator_keyword_args and len(decorator_optional_args) > 0:
                print(decorator_optional_args[0] * decorator_keyword_args['symbol'])

        return inner_function

    return inner_decorator


@decorator(50, symbol='=')
def function1(arg, *args, **kwargs):
    print(f"arg: {arg}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


@decorator(100, symbol='.')
def function2(arg, *args, **kwargs):
    print(f"arg: {arg}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


@decorator()
def function3(arg, *args, **kwargs):
    print(f"arg: {arg}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


# calling the functions to see what happens
function1(1, 2, a=3)
function2(8)
function3(6, 7, 9)


# this is the result
"""

invoking function1
==================================================
arg: 1
args: (2,)
kwargs: {'a': 3}
==================================================

invoking function2
....................................................................................................
arg: 8
args: ()
kwargs: {}
....................................................................................................

invoking function3
arg: 6
args: (7, 9)
kwargs: {}
"""