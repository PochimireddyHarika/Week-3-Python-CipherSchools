numbers = [1,2,4,5,7]
print(min(numbers))

names = ['Harika', 'Sai', 'ab']
print(max(names,key = lambda item : len(item)))


students = {
    'harika' : {'score': 100, 'age':18},
    'sai' : {'score': 99, 'age':16},
    'ab' : {'score': 99, 'age':13}
}
print(max(students, key = lambda item:item.get('score'))['name'])

