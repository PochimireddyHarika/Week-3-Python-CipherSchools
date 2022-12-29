def func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")
    print(kwargs)
    print(type(kwargs))


d = {'name': 'haika', 'age' : 18}
func(**d)


