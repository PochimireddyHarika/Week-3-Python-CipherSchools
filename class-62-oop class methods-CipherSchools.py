class Person:
    count_instance = 0
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instance(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} of Person class"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_17(self):
        return self.age>17

p1 = Person('Harika', 'Pochimireddy', 18)
p2 = Person('Sai', 'Pochimireddy', 15)
print(Person.count_instance())