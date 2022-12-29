def multiply_num(num1,num2, *args):
    multiply = 1
    print(multiply_num)
    print(args)
    for i in args:
        multiply *= i
    return multiply

print(multiply_num(2,4,3,4))
