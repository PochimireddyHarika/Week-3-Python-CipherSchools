class Phone:
    def __init__(self, brand, model_name, price):
        #instace variables
        self.brand = brand
        self.name = model_name
        self.__price = price

    def make_a_call(self, phone_number):
        print(f"calling{phone_number} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass # twilio


phone1 = Phone('nokia', '1100', 1000)
print(phone1._Phone__price)

# _name # conversion of private name
# __name__ # dunder/magic methods

l = [3,4,1,2]
l.sort() # tim sort
print(l)
