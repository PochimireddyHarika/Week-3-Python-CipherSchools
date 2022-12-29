class Person:
    count_instance = 0
    def __init__(self,first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first, last, age)


    @classmethod
    def count_instance(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} of Person class"
    @staticmethod
    def hello():
        print('hello, static method called')
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18

p1 = Person('Harika', 'Pochimireddy', 19)
p2 = Person('Sai', 'Pochimireddy', 15)

p3 = Person.from_string('Harika', 'Pochimireddy', 17)
Person.hello()