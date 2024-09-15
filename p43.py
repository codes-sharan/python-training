
class vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_detail(self):
        print(f"The car is {self.make} and model is {self.model}")

vehicle1 = vehicle(make='Tesla', model='TeslaM1')
vehicle2 = vehicle(make='BMW', model='BMW_V5')

# vehicle1.get_detail()
# vehicle2.get_detail()

class car(vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def get_detail(self):
        super().get_detail()
        print(f"The manufacture year is {self.year}")
    

car1 = car(make='BYD', model='b1', year=2021)

car1.get_detail()