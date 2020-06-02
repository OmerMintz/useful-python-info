

def decorator(*decorator_optional_args, **decorator_keyword_args):

    def inner_decorator(function):

        def inner_function(*function_optional_args, **function_keyword_args):

            # use decorator arguments and add custom behavior here

            function(*function_optional_args, **function_keyword_args)

            # use decorator arguments and add custom behavior here

        return inner_function

    return inner_decorator
