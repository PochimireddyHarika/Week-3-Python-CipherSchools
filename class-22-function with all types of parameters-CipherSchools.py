def func(name = 'unknown', age = 18):
    print(name)
    print(age)

def func(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('harika', 1,2,3, a = 1, b = 2)
