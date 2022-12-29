# instance methods
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_17(self):
        return self.age>17

p1 = Person('Harika', 'Pochimireddy', 18)
p2 = Person('Sai', 'Pochimireddy', 15)
print(p1.full_name())
print(p1.is_above_17())


l = [1,2,3]
# l.clear()
list.clear(l)
print(l)
# l.append(10)
list.append(l,10)
print(l)


