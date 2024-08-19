import math
from graphics import *


def greet(name):
    return f"Hello, {name}!"


def product(a, b):
    return a * b


def divide(a, b):
    return a / b


def divdeAndProduct(a, b):
    productResult = product(a, b)
    divideResult = divide(a, b)
    return productResult, divideResult


def main():
    myName = input("What is your name? ")
    greeting = greet(myName)
    print(greeting)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    productResult, divideResult = divdeAndProduct(num1, num2)
    print(f"{num1} * {num2} = {productResult}")
    print(f"{num1} / {num2} = {divideResult}")


def calcFutureValue(amount, years):
    interestRate = 0.065
    for year in range(years):
        amount = amount * (1 + interestRate)
    return amount


def futureValue():
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    final = calcFutureValue(amount, years)

    output = f"Investing £{amount:0.2f} for {years} years "
    output += f"results in £{final:0.2f}."
    print(output)


# exercise 1 and 2
def circleInfo():
    radius = float(input("Enter the radius of the circle: "))

    area = areaOfCircle(radius)
    circumference = circumferenceOfCircle(radius)

    print(f"The area is {area:.3f} and the circumference is {circumference:.3f}")


def areaOfCircle(radius):
    return math.pi * radius ** 2

def circumferenceOfCircle(radius):
    circumference = 2 * math.pi * radius
    return round(circumference, 3)


# Exercise 3
def drawCircle(center, radius, color, win):
    circle = Circle(center, radius)
    circle.setFill(color)
    circle.draw(win)

def drawBrownEyeInCentre():
    win = GraphWin("Brown Eye", 400, 400)
    win.setBackground("white")

    center = Point(200, 200)
    radius_large = 60
    radius_medium = 30
    radius_small = 15

    # large circle in brown color
    drawCircle(center, radius_large, "brown", win)

    # medium circle in white color
    drawCircle(center, radius_medium, "white", win)

    # small circle in brown color
    drawCircle(center, radius_small, "brown", win)

    win.getMouse()
    win.close()

drawBrownEyeInCentre()




