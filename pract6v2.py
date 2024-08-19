from graphics import *
import math 


def greet(name):
    print("Hello", name + ".")
    if len(name) > 20:
        print("That's a long name!")


def canYouVote(age):
    if age >= 18:
        print("You can vote")
    else:
        print("Sorry, you can't vote")


def getDegreeClass(mark):
    if mark >= 70:
        return "1st"
    elif mark >= 60:
        return "2:1"
    elif mark >= 50:
        return "2:2"
    elif mark >= 40:
        return "3rd"
    else:
        return "Fail"


# We will simplify this function later in the term
def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def daysInMonth(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        return 31


def overlyComplexDaysInMonth(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif isLeapYear(year):
        return 29
    else:
        return 28


def countDown():
    for i in range(10, 0, -1):
        print(i, "...", end=" ")
    print("Blast Off!")


def numberedTriangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


# For exercise 8

def drawColouredEye(win, centre, radius, colour):
    eye = turtle.Turtle()
    eye.penup()
    eye.goto(centre)
    eye.pendown()

    # outer circle of the eye
    eye.color(colour)
    eye.begin_fill()
    eye.circle(radius)
    eye.end_fill()

    # inner circle of the eye
    eye.penup()
    eye.goto(centre[0], centre[1] + radius * 0.4)
    eye.pendown()
    eye.color("black")
    eye.begin_fill()
    eye.circle(radius * 0.4)
    eye.end_fill()

    win.exitonclick()    

# Exercise 1
def FastFoodOrderPrice():
    order_price = float(input("Enter the basic price of your order: £"))
    delivery_charge = 2.50
    
    if order_price >= 20:
        delivery_charge = 0
        
        totalPrice = order_price + delivery_charge
        print("The total price of your order is £" + str(totalPrice))
        
# Exercise 2
def whatToDoToday():
    temperature = float(input("Enter today's temperature: "))
    
    if temperature > 25:
        recommendation = "You should go swimming in the sea."
    elif temperature >= 10:
        recommendation = "You should stay at home and watch a film."
        
        print(recommendation)
        
# Exercise 3
def displaySquareRoots(start, end):
    for number in range(start, end +1):
        squareRoot = math.sqrt(number)
        print(f"The square root of {number} is {squareRoot:.3f}")

# Exercise 4
def calculateGrade(mark):
    if mark >= 16:
        grade = 'A'
    elif mark >= 12:
        grade = 'B'
    elif mark >= 8:
        grade = 'C'
    else:
        grade = 'X'
        
    return grade


# Exercise 5
import turtle


def peasInAPod():
    numberPeas = int(input("Enter the number of peas: "))
    
    windowWidth = numberPeas * 100
    windowHeight = 100
    
    window = turtle.Screen()
    window.setup(windowWidth, windowHeight)
    turtle.speed(5)
    
    for _ in range(numberPeas):
        turtle.penup()
        turtle.goto(-windowWidth/2 + 50, 0)
        
        turtle.pendown()
        turtle.fillcolor("green")
        turtle.beginFill()
        turtle.endFill()
        turtle.penup()
        turtle.forward(100)
        
    turtle.done()

# Exercise 6
def ticketPrice(distance, age):
    basePrice = 10  
    perKilometrePrice = 0.15   
    discountPercentage = 0.4 

    # total price based on distance
    totalPrice = basePrice + (distance * perKilometrePrice)

    # Discount for senior citizens and children
    if age >= 60 or age <= 15:
        discountAmount = totalPrice * discountPercentage
        totalPrice -= discountAmount

    return totalPrice

# Exercise 7
def numberedSquare(n):
    for i in range(n, 0, -1):  # from n to 1 in descending order
        for j in range(i, i + n): # from i to i + n
            print(j, end=" ")
        print() 


# Exercise 8 
from graphics import *

def eyePicker():
    win = GraphWin("Eye Picker", 400, 400)

    # Asks the user for eye coordinates, radius, and color
    x = int(input("Enter the x-coordinate of the eye center: "))
    y = int(input("Enter the y-coordinate of the eye center: "))
    radius = int(input("Enter the radius of the eye: "))
    color = input("Enter the color of the eye (blue, grey, green, or brown): ")

    # eye center is within the window
    if x < radius or x > 400 - radius or y < radius or y > 400 - radius:
        print("Eye center not in window")
        win.close()
        return

    # Check if the color is valid
    if color not in ["blue", "grey", "green", "brown"]:
        print("Not a valid eye color")
        win.close()
        return

    # Draw the eye
    eye = Circle(Point(x, y), radius)
    eye.setFill(color)
    eye.draw(win)

    # for the window to be closed
    win.getMouse()
    win.close()


# Exercise 9
from graphics import *

def drawPatchWindow():
    win = GraphWin("Patch Design", 200, 200)

    # background color of the window
    win.setBackground("white")

    # final digit of your student number
    studentNumber = 2198300  
    finalDigit = studentNumber % 10

    # Draw the patch design in the top-left quarter
    if finalDigit == 0:
        drawPatch0(win)
    elif finalDigit == 1:
        drawPatch1(win)
    elif finalDigit == 2:
        drawPatch2(win)
    elif finalDigit == 3:
        drawPatch3(win)
    elif finalDigit == 4:
        drawPatch4(win)
    elif finalDigit == 5:
        drawPatch5(win)
    elif finalDigit == 6:
        drawPatch6(win)
    elif finalDigit == 7:
        drawPatch7(win)
    elif finalDigit == 8:
        drawPatch8(win)
    elif finalDigit == 9:
        drawPatch9(win)

    # Wait for the window to be closed
    win.getMouse()
    win.close()

# Patch design functions
def drawPatch0(win):
    # Design for patch 0
    pass

def drawPatch1(win):
    # Design for patch 1
    pass

def drawPatch2(win):
    # Design for patch 2
    pass

def drawPatch3(win):
    # Design for patch 3
    pass

def drawPatch4(win):
    # Design for patch 4
    pass

def drawPatch5(win):
    # Design for patch 5
    pass

def drawPatch6(win):
    # Design for patch 6
    pass

def drawPatch7(win):
    # Design for patch 7
    pass

def drawPatch8(win):
    # Design for patch 8
    pass

def drawPatch9(win):
    # Design for patch 9
    pass

# Example usage
drawPatchWindow()


# for exercise 11
from graphics import *

def drawColouredEye(win, centre, radius, colour):
    eye = Circle(Point(centre[0], centre[1]), radius)
    eye.setFill(colour)
    eye.draw(win)

def eyesAllAround():
    win = GraphWin("Eyes All Around", 500, 500)

    colours = ["blue", "grey", "green", "brown"]
    colour_index = 0

    for _ in range(30):
        # center point from the user
        click_point = win.getMouse()
        center_x, center_y = click_point.getX(), click_point.getY()

        # eye with the current color
        drawColouredEye(win, (center_x, center_y), 30, colours[colour_index])

        # Cycle to the next color
        colour_index = (colour_index + 1) % 4

    # for the window to be closed
    win.getMouse()
    win.close()

# Example usage
eyesAllAround()






