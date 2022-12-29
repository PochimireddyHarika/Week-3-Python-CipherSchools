class Phone:
    def __init__(self, brand, model_name, price):
        #instace variables
        self.brand = brand
        self.name = model_name
        self._price = price
        
    @property
    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self.price = max(new_price, 0)

    def make_a_call(self, phone_number):
        print(f"calling{phone_number} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"
phone1 = Phone('Nokia', '1100', 1000)
print(phone1.brand)
print(phone1._price)

