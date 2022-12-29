def print_function_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are calling{function.__name__}")
        return function(*args, **kwargs)
    return wrapper



def add(a,b):
    return a + b

print(add(4,5))