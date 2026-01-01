# --------INHERIT PARENT CLASS------------

class Vehicle:
    company = "XYZ Motors"

    def __init__(self, n_wheels, n_seats, mileage):
        print("init of Vehicle")
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage

    def get_details(self):
        return f"This vehicle has {self.n_wheels} wheels, {self.n_seats} seats and provides a mileage of {self.mileage}"


# --------CHILD CLASS--------

class Car(Vehicle):
    model = "ABC123"

    def __init__(self, car_type, drive_type, wheels, seats, mileage):
        print("init of Car")
        self.car_type = car_type
        self.drive_type = drive_type

        # Calling parent class constructor
        super().__init__(wheels, seats, mileage)


print("--------CALLING THE CHILD CLASS--------")
c1 = Car("SUV", "Manual", 4, 7, 20)

print(c1.mileage)
print(c1.company)
print(c1.get_details())
print(c1)

print("--------OBJECT DETAILS--------")
print(c1.__dict__)

print("--------CLASS INFORMATION--------")
help(Car)
