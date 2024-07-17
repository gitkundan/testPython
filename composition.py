class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started"

class Wheel:
    def __init__(self, size):
        self.size = size

    def roll(self):
        return "Wheel rolling"

class Car:
    def __init__(self, engine, wheels):
        self.engine = engine
        self.wheels = wheels

    def start(self):
        return self.engine.start()

    def drive(self):
        return [wheel.roll() for wheel in self.wheels]

# Creating objects
engine = Engine(horsepower=150)
wheels = [Wheel(size=15) for _ in range(4)]

# Composing a Car object with Engine and Wheels
car = Car(engine=engine, wheels=wheels)

# Using the composed Car object
print(car.start())  # Output: Engine started
print(car.drive())  # Output: ['Wheel rolling', 'Wheel rolling', 'Wheel rolling', 'Wheel rolling']
