class Car:
    car_count = 0

    def __init__(self, model):
        self.__brand = ''  # private variable
        self.__model = model
        Car.car_count += 1 
    
    def full_name(self):
        return f'full name {self.__brand} {self.__model}'

    # getter implemented
    def get_brand(self):
        return self.__brand
    
    # setter implemented
    def set_brand(self, brand):
        self.__brand = brand

    # Polymorphism implemented
    def fuel_type(self):
        return 'Petrol'

    # Static Method implemented (instance can't access)
    @staticmethod
    def car_description():
        return 'Cars can move'

    # @property decorator
    @property
    def model(self):
        return self.__model



class ElectricCar(Car):

    def __init__(self, model, battery_size):
        super().__init__(model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric"


# tata_car = Car("Tata", "safari")
# print(tata_car.brand)

# print(tata_car.full_name())


# my_tesla = ElectricCar('Model S', '80kwh')

# print(my_tesla.__brand)
# print(my_tesla.full_name())


# my_safari = Car('Safari')
# my_safari.set_brand('Tata')
# print(my_safari.get_brand())


# polymorphism test
safari = Car('Safari')
# print(safari.fuel_type())

nexon_ev = ElectricCar('Nexon ev', '5000mah')
# print(nexon_ev.fuel_type())

# print(Car.car_count)


# static method test (Associated with class not instance)
# print(Car.car_description())



# Changing car model
# my_car = Car('Safari')
# print(my_car.model)
# my_car.model = 'train'
# print(my_car.model)

# to stop this @property decorator 
my_car = Car('Safari')
# print(my_car.model())
# print(my_car.model)




# Problem 9

# tesla = ElectricCar('Model S', '5000k')

# print(isinstance(tesla, Car))
# print(isinstance(tesla, ElectricCar))



# Problem 10

class Battey():
    def battery_info(self):
        return 'This is battery'

class Engine():
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battey, Engine):
    def electricCar_info(self):
        print('This is electric car')

    

tesla = ElectricCarTwo()

tesla.electricCar_info()
print(tesla.engine_info())

