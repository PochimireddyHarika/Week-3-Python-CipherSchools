def square(a):
    return a**2

s = square(7)
print(s)

s = square
print(s(7))
print(s.__name__)
print(s)
