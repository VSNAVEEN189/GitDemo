# A class a is inherited by b and c is inherited from b  automatically c inherits from a parent class.

class Vehicle:
    company = "XYZ Motors"

    def __init__(self, n_wheels, n_seats, mileage):
        print("init of Vehicle")
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage

    def get_details(self):
        return f"This vehicle has {self.n_wheels} wheels, {self.n_seats} seats and provides a mileage of {self.mileage}"

class Car(Vehicle):
    model = "ABC123"

    def __init__(self, car_type, drive_type, wheels, seats, mileage):
        print("init of Car")
        self.car_type = car_type
        self.drive_type = drive_type

        # Calling parent class constructor
        super().__init__(wheels, seats, mileage)

    def dispaly_info(self):
        print(f"Car type: {self.car_type}, Drive type: {self.drive_type}")


class ElectricCar(Car):  
    def __init__(self, car_type, drive_type, wheels, seats, mileage, battery_capacity, distance_range):
        self.battery_capacity = battery_capacity
        self.distance_range = distance_range
        super().__init__(car_type, drive_type, wheels, seats, mileage)

    def charge(self):
           print("Charging the to {self.battery_capacity}")

ec1 = ElectricCar("Sedan", "Manual", 4, 5, 35, 100, 400)

print(ec1.__dict__)

help(ElectricCar)

# Car is a parent of a Electric car and Vehicle is the parent of Car know as multilevel relationship.

# Multiple inheritance is when a single child class gets features 
# (attributes and methods) from more than one parent class