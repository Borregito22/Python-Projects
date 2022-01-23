# Parent class
class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print("Details:", self.name, self.color, self.price)

    def max_speed(self):
        print("Vehicle max speed is 155 mph")

    def gears(self):
        print("Vehicle has an 8-speed automatic")

    def horsepower(self):
        print("Vehicle has 563 hp")

    def fuel(self):
        print("Vehicle gets 12 city / 20 highway mpg")

# First child class
# Both child classes inherit from vehicle class
class Car1(Vehicle):
    # max_speed() and gears() overriden by interpreter and uses the one defined in child class
    # show() osn't overridden so it's used from Parent class
    def max_speed(self):
        print("Car1 max speed is 190 mph")

    def gears(self):
        print("Car1 has an 8-speed automatic")

    def engine(self):
        print("Car1 has a V8")

    def seats(self):
        print("Car1 has four seats\n")

# Second child class
class Car2(Vehicle):
    def max_speed(self):
        print("Car2 max speed is 137 mph")

    def gears(self):
        print("Car2 has 9-speed automatic")

    def weight(self):
        print("Car2 weighs 5845 lbs")

    def displacement(self):
        print("Car2 has a 4.0L\n")

# Car1 Object
car1 = Car1("Urus", "White", "218009")
car1.show()
# Calls methods from Car1 child class
car1.max_speed()
car1.gears()
car1.engine()
car1.seats()

# Car2 Object
car2 = Car2("G-Class", "Black", "156450")
car2.show()
# Calls methods from Car2 child class
car2.max_speed()
car2.gears()
car2.weight()
car2.displacement()

# Vehicle Object
vehicle = Vehicle("Cullinan", "Black", "330000")
vehicle.show()
# Calls methods from Vehicle parent class
vehicle.max_speed()
vehicle.gears()
vehicle.horsepower()
vehicle.fuel()
