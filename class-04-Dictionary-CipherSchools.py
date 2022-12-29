d1 = {'name' : 'harika', 'age' : 18 }

d1 = dict(name = 'harika', age = 18)

d2 = {
    'name' : 'harika',
    'age' : 18,

}

print(d2['name'])

empty_dict = {}
empty_dict['key1']= 'value1'
empty_dict['key2']= 'value2'

print(d2.get('name'))

popped = d2.pop('name')
print(popped)
popped = d2.popitem()
print(popped)