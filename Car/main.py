from car import Car

car1 = Car("Skoda", 2022, "blue", False)
car2 = Car("Octavia", 2021, "silver", True)
car3 = Car("Superb", 1998, "gold", False)

print(f"This is your car of choice {car1.model} with {car1.color} color.")
car1.drive()
car2.stop()
car3.describe()


