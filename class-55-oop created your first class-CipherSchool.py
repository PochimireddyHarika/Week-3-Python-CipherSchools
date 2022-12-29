class Person:
    def __init__(self,first_name, last_name, age):
        # instace variables
        print('init method // constructor get called')
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Harika', 'pochimireddy', 18)
p2 = Person('Sai', 'pochimireddy', 15)

print(p1.first_name)
print(p2.first_name)
