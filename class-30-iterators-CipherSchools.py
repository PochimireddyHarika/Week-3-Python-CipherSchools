numbers = [1,2,3,4]
squares = map(lambda a:a**2, numbers)

for i in numbers:
    print(i)
number_iter = iter(numbers)
print(next(number_iter))

