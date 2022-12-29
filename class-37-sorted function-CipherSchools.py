fruits = ['grapes', 'mango', 'apple']
fruits.sort()
print(fruits)

fruits2 = ('grapes', 'mango', 'apple')
print(sorted(fruits))

fruits3 = {'grapes', 'mango', 'apple'}
print(sorted(fruits))

guitars = [
    {'model': 'yamaha f310', 'price':8400},
    {'model': 'faith naptune', 'price':5000}
]

sorted_guitars = sorted(guitars, key = lambda d:d['price'], reverse = True)
print(sorted_guitars)
