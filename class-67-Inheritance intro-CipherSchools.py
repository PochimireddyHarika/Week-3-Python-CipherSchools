class Phone:
    def __init__(self, brand, model_name, price):
        #instace variables
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
        
    def make_a_call(self, phone_number):
        print(f"calling{phone_number} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"
class Smartphone:
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # two ways
        Phone.__init__(self,brand,model_name, price)
        self.brand = brand
        self.name = model_name
        self._price = max(price,0)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera


phone = Phone('nokia', '1100', 1000)
smartphone = Smartphone('onePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
print(phone.full_name())
print(smartphone.full_name() + "and price is {}")
        


