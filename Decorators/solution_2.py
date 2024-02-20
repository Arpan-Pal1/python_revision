# Problem 2

def debug(fx):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(i) for i in args)
        kwargs_value = ', '.join(f'{k}, {v}'for k, v in kwargs.items())
        print(f'calling: {fx.__name__} with args {args_value} and kwargs {kwargs_value}')
        return fx(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting):
    print(f'{name}, {greeting}')

@debug
def f(n):
    pass

@debug
def next_greet(name="Jhon Doe"):
    pass


greet("arpan", "Hello")
f(5)
next_greet(name="Arpan")