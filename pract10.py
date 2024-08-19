from graphics import *


class MyPoint:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        output = f"MyPoint({self.x}, {self.y})"
        return output


class Square():

    def __init__(self, p1, side):
        self.p1 = p1
        self.side = side
        self.p2 = MyPoint(p1.getX() + side, p1.getY() + side)
        self.fillColour = "black"

    def getP1(self):
        return self.p1

    def getP2(self):
        return self.p2

    def getSide(self):
        return self.side

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def __str__(self):
        output = f"Square({self.p1}, {self.p2})"
        return output

    def setFillColour(self, colour):
        colours = ["red", "green", "blue", "yellow", "purple"]
        if colour in colours:
            self.fillColour = colour


def testMyPoint():
    myPoint = MyPoint(100, 50)
    print("myPoint's x coordinate is", myPoint.getX())  # 100
    print("myPoint's y coordinate is", myPoint.getY())  # 50

    myPoint.move(10, -20)

    print("myPoint's x coordinate is", myPoint.getX())  # 110
    print("myPoint's y coordinate is", myPoint.getY())  # 30

    print("myPoint is:", myPoint)  # myPoint is: MyPoint(110, 30)


def testPoint():
    p = Point(100, 50)

    print("p is of type:", type(p))  # <class 'graphics.Point'>

    print("p's x coordinate is", p.getX())  # 100.0
    print("p's y coordinate is", p.getY())  # 50.0

    p.move(10, -20)

    print("p's x coordinate is", p.getX())  # 110.0
    print("p's y coordinate is", p.getY())  # 30.0

    print("p is:", p)  # p is: Point(110.0, 30.0)


def testSquare():
    p1 = MyPoint(100, 50)
    square = Square(p1, 50)
    print("square's side length is", square.getSide())  # 50
    print("square's p1 is", square.getP1())  # MyPoint(100, 50)
    print("square's p2 is", square.getP2())  # MyPoint(150, 100)

    square.move(10, -20)
    print("After the move ...")
    print("square's side length is", square.getSide())  # 50
    print("square's p1 is", square.getP1())  # MyPoint(110, 30)
    print("square's p2 is", square.getP2())  # MyPoint(160, 80)

    print(square)  # Square(MyPoint(110, 30), MyPoint(160, 80))

    print("Changing square's fill colour to red")
    square.setFillColour("red")
    print("square's fill colour is", square.fillColour)  # red
    print("Changing square's fill colour to leopard print!")
    square.setFillColour("leopard print")
    print("square's fill colour is", square.fillColour)  # red
    

#Exercise 1 & Exercise 2

class Square:
    def __init__(self, sideLength):
        self.sideLength = sideLength
        self.fillColour = "black"
        self.outlineColour = "black"

    def setOutlineColour(self, colour):
        validColours = ["black", "red", "green", "blue"]
        if colour in validColours:
            self.outlineColour = colour
        else:
            print("Invalid outline colour!")

    def printOutlineColour(self):
        print("Outline colour:", self.outlineColour)

    def getPerimeter(self):
        return 4 * self.sideLength

    def getArea(self):
        return self.sideLength ** 2


def testSquare():
    square = Square(5)
    square.printOutlineColour()  

    square.setOutlineColour("red")
    square.printOutlineColour()  

    perimeter = square.getPerimeter()
    print("Perimeter:", perimeter)  

    area = square.getArea()
    print("Area:", area)  


testSquare()



# Exercise 3

class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "MyPoint({}, {})".format(self.x, self.y)


class Square:
    def __init__(self, corner, length):
        self.corner = corner
        self.length = length

    def getCenter(self):
        x = self.corner.x + self.length / 2
        y = self.corner.y + self.length / 2
        return MyPoint(x, y)


# Square class
corner = MyPoint(100, 50)
length = 70

square = Square(corner, length)
center = square.getCenter()

print(center)



# Exercise 4

class MyPoint:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class MyCircle:
    def __init__(self, centre: MyPoint, radius: float):
        self.centre = centre
        self.radius = radius

    def getCentre(self) -> MyPoint:
        return self.centre

    def move(self, dx: float, dy: float):
        self.centre.x += dx
        self.centre.y += dy

    def __str__(self) -> str:
        return f"Circle: Centre({self.centre.x}, {self.centre.y}), Radius: {self.radius}"

def testCircle():
    # Circle with centre at (0, 0) and radius 5
    centre = MyPoint(0, 0)
    circle = MyCircle(centre, 5)

    
    print(circle)

    # Moves the circle by (2, 3)
    circle.move(2, 3)

    
    print(circle)

testCircle()



# Exercise 5

class BankAccount:
    def __init__(self, accountNumber, accountHolder, initialBalance, interestRate):
        self.accountNumber = accountNumber
        self.accountHolder = accountHolder
        self.balance = initialBalance
        self.interestRate = interestRate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def applyInterest(self):
        interestAmount = self.balance * (self.interestRate / 100)
        self.balance += interestAmount

    def getBalance(self):
        return self.balance


def testBankAccount():
    account = BankAccount(123456789, "John Doe", 1000, 5)

    # account holder's name
    print("Account Holder:", account.accountHolder)

    # deposit
    account.deposit(500)
    assert account.getBalance() == 1500

    # withdrawal
    account.withdraw(200)
    assert account.getBalance() == 1300

    # withdrawal with insufficient funds
    account.withdraw(2000)
    assert account.getBalance() == 1300

    # applying interest
    account.applyInterest()
    assert account.getBalance() == 1365

    print("All tests passed.")


testBankAccount()



# Exercise 6

class Square:
    def __init__(self, x, y, sideLength):
        self.x = x
        self.y = y
        self.sideLength = sideLength

    def scale(self, factor):
        center_x = self.x + (self.sideLength / 2)
        center_y = self.y + (self.sideLength / 2)

        new_side_length = self.sideLength * factor

        new_x = center_x - (new_side_length / 2)
        new_y = center_y - (new_side_length / 2)

        self.x = new_x
        self.y = new_y
        self.sideLength = new_side_length
        
        
# Exercise 7

class Aeroplane:
    def __init__(self):
        self.fuel = 0
        self.altitude = 0
        self.departure = ""
        self.destination = ""

    def setFuel(self, fuel):
        if fuel <= 150000:
            self.fuel = fuel
        else:
            self.fuel = 150000

    def increaseAltitude(self):
        self.altitude += 1

    def decreaseAltitude(self):
        if self.altitude > 0:
            self.altitude -= 1

    def setDeparture(self, departure):
        self.departure = departure

    def setDestination(self, destination):
        self.destination = destination

    def getDeparture(self):
        return self.departure

    def getDestination(self):
        return self.destination

    def getAltitude(self):
        return self.altitude

    def __str__(self):
        return f"Fuel: {self.fuel} litres, Altitude: {self.altitude} ft, Departure: {self.departure}, Destination: {self.destination}"


def testAeroplane():
    departure = input("Enter departure: ")
    destination = input("Enter destination: ")

    plane = Aeroplane()
    plane.setFuel(150000)
    plane.setDeparture(departure)
    plane.setDestination(destination)

    print(plane)

    choice = input("Increase altitude? (y/n): ")
    if choice == "y":
        plane.increaseAltitude()
        print(plane)

    choice = input("Decrease altitude? (y/n): ")
    if choice == "y":
        plane.decreaseAltitude()
        print(plane)


testAeroplane()




