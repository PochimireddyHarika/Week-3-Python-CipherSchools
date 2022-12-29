squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)


square2 = [i**2 for i in range(1,11)]
print(square2)

negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)

new_negative = [-i for i in range(1,11)]
print(new_negative)

names = ['Harika', 'Sai', 'Radha']
new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)

new_list2 = [name[0] for name in names]
print(new_list2)