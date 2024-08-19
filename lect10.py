class Car:

    def __init__(self, colour, engine):
        self.colour = colour
        self.engine = engine
        self.speed = 0

    def getEngine(self):
        return self.engine

    def getColour(self):
        return self.colour

    def getSpeed(self):
        return self.speed

    def setColour(self, colour):
        if colour in ["red", "green", "blue", "yellow"]:
            self.colour = colour

    def brake(self):
        self.speed = 0

    def accelerate(self):
        if self.speed <= 60:
            self.speed += 10

    def __str__(self):
        output = f"{self.colour} {self.engine} car"
        output += f"travelling at {self.speed} mph"
        return output


def testCar():
    myCar = Car("red", "electric")
    print("My car's engine is", myCar.getEngine())
    print("And it's colour is", myCar.getColour())

    myCar.setColour("blue")
    print("My car's colour is now", myCar.getColour())

    print("My car is going", myCar.getSpeed(), "mph")
    myCar.accelerate()
    print("My car is now going", myCar.getSpeed(), "mph")
    myCar.brake()
    print("After braking, my car's speed is", myCar.getSpeed(), "mph")

    print(myCar)
