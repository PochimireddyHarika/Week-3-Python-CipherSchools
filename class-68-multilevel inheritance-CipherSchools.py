class Phone:
    def __init__(self, brand, model_name, price):
        #instace variables
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
        
        
        
    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self, number):
        return f"calling{number} ..."


class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # two ways
        # Phone.__init__(self,brand,model_name, price)

        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

class FlagshipPhone(Smartphone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price} and front_camera = {self.front_camera}"


# phone = Phone('nokia', '1100', 1000)
smartphone = Smartphone('onePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
oneplus5 = FlagshipPhone('onePlus', '5t', 30000, '6 GB', '64 GB', '20 MP', '16 MP')
print(oneplus5.full_name())
print(help(FlagshipPhone))
print(issubclass(Smartphone,FlagshipPhone))


