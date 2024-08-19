from graphics import *

# List example:
def displayMonths():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for month in months:
        print(month)


# List example:
def displayTemperatureOfWeek():
    temperatures = [14.5, 8.0, -2.5, 15.0, 12.5, 9.0, -1.0]
    for temp in temperatures:
        print("It's {} degrees today".format(temp))
        if temp < 0:
            print("Brrrrr, that's freezing!")


# List example:
def processNumbers():
    numbers = [11, 28, 32, 34, 45, 67, 70, 89, 90, 99]
    for i in range(len(numbers)):
        if i % 2 == 0:  # Only process numbers at even indexes
            square = numbers[i] ** 2
            print("The square of {} is {}".format(numbers[i], square))


# List example:
def readPrime():
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    while True:
        num = int(input("Enter a prime number less than 20: "))
        if num in primes:
            break
    print(num, "is a prime number less than 20")


# List example:
def changeColours():
    win = GraphWin()
    circles = []
    for x in range(50, 200, 100):
        for y in range(50, 200, 100):
            circle = Circle(Point(x, y), 50)
            circle.setFill("red")
            circle.draw(win)
            circles.append(circle)  # Add the circle to the list

    for circle in circles:  # For each circle in the list
        win.getMouse()  # Wait for a mouse click
        circle.setFill("green")  # Change the colour of the circle


# List of tuples example:
def displayMenu():
    menu = [("Chicken Tikka Masala", 900, 8.95),
            ("Lamnb Rogan Josh", 700, 7.95),
            ("Vegetable Biryani", 600, 6.95),
            ("Portion of poppadoms", 100, 0.75)]
    for item in menu:
        name, calories, price = item
        print("{:20} {:5} calories, £{:4.2f}".format(name, calories, price))


# Set example:
def filterFruits():
    fruits = {"apple", "banana", "kiwi", "pear", "orange"}
    fruitsILike = set()  # Create an empty set
    for fruit in fruits:
        if fruit != "kiwi" and fruit != "pear":
            fruitsILike.add(fruit)
    print(fruitsILike)


# Dictionary example:
def iterateStudents():
    studnets = {
        3419903: "Lou",
        7470773: "Nannie",
        5285384: "Hester"
    }
    for upNum in studnets:
        name = studnets[upNum]
        print("UP{} is {}".format(upNum, name))


# Exercise 1

def displayDate(day, month, year):
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    return f"{day} {months[month - 1]} {year}"


# Exercise 2

def wordLengths(words):
    for word in words:
        print(word, len(word))

wordLengths(["bacon", "jam", "spam"])




# Exercise 3

from graphics import *

def drawHexagon():
    win = GraphWin("Hexagon", 500, 500)
    win.setBackground("white")


    vertices = []
    for _ in range(6):
        message = Text(Point(250, 250), "Click to set vertex")
        message.draw(win)
        clickPoint = win.getMouse()
        vertices.append(clickPoint)
        message.undraw()
    
    
    hexagon = Polygon(vertices)
    hexagon.setFill("red")
    hexagon.draw(win)


    win.getMouse()
    win.close()

drawHexagon()


# Exercise 4

def testMarks():
    marks = []
    while True:
        mark = input("Enter the module mark (or 'done' to finish): ")
        if mark.lower() == "done":
            break
        marks.append(int(mark))

    markCounts = {}
    for mark in marks:
        if mark in markCounts:
            markCounts[mark] += 1
        else:
            markCounts[mark] = 1

    for mark in range(6):
        count = markCounts.get(mark, 0)
        print(f"{count} student(s) got {mark} mark(s)")

testMarks()



# Exercise 5

def drawBarChart(data):
    # maximum value in the data
    maxValue = max(data)

    # Calculates the height of each bar based on the maximum value
    maxHeight = 5
    barHeights = [int((value / maxValue) * maxHeight) for value in data]

    # Draw the bar chart
    for row in range(maxHeight, 0, -1):
        rowSymbols = ['#' if height >= row else ' ' for height in barHeights]
        print(' '.join(rowSymbols))

drawBarChart([3, 1, 2])




# Exercise 6

def uniqueModules(moduleNames):
    uniqueModules = list(set(moduleNames))
    for module in uniqueModules:
        print(module)

uniqueModules(['Programming', 'Databases', 'Programming', 'Networks'])



# Exercise 7
from graphics import GraphWin, Point, Rectangle, Text, Circle
import random

def drawHouse(win, x, y, width, height, doorColor, doorNumber, isLightOn):
    # Draw house walls
    house = Rectangle(Point(x, y), Point(x + width, y + height))
    house.setFill("gray")
    house.draw(win)

    # Draw door
    doorWidth = width / 5
    doorHeight = height / 2
    doorX = x + (width - doorWidth) / 2
    doorY = y
    door = Rectangle(Point(doorX, doorY), Point(doorX + doorWidth, doorY + doorHeight))
    door.setFill(doorColor)
    door.draw(win)

    # Draw door number
    numberX = doorX + doorWidth / 2
    numberY = doorY + doorHeight / 2
    number = Text(Point(numberX, numberY), str(doorNumber))
    number.setSize(12)
    number.setStyle("bold")
    number.draw(win)

    # Draw light
    if isLightOn:
        lightX = doorX + doorWidth / 2
        lightY = doorY - doorHeight / 2
        light = Circle(Point(lightX, lightY), doorWidth / 6)
        light.setFill("yellow")
        light.draw(win)

def drawStreet(numHouses, windowHeight):
    win = GraphWin("Street", numHouses * 100, windowHeight)
    win.setBackground("white")

    houseWidth = 100
    houseHeight = windowHeight

    for i in range(numHouses):
        x = i * houseWidth
        y = 0

        doorColor = input("Enter the door color for house " + str(i + 1) + ": ")
        doorNumber = i + 1
        isLightOn = random.random() < 0.5

        drawHouse(win, x, y, houseWidth, houseHeight, doorColor, doorNumber, isLightOn)

    win.getMouse()
    win.close()

# Example usage
numHouses = int(input("Enter the number of houses: "))
windowHeight = int(input("Enter the height of the graphics window: "))

drawStreet(numHouses, windowHeight)



# Exercise 8

from math import sqrt

def distanceBetweenPoints(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Example usage
point1 = (1, 2)
point2 = (4, 6)
distance = distanceBetweenPoints(point1, point2)
print(distance)



# Exercise 9

def countCharacters():
    string = input("Enter a string: ")
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        print(f"{count} occurrences of '{char}'")

countCharacters()



# Exercise 10

import random

def tracedwalk():
    n = int(input("Enter the length of the pavement: "))
    start_position = n // 2
    position = start_position
    steps_count = {i: 0 for i in range(1, n+1)}
    
    print("Square Steps")
    print(f"{position} 0")
    
    while 1 <= position <= n:
        step = random.choice([-1, 1])
        position += step
        if 1 <= position <= n:
            steps_count[position] += 1
            print(f"{position} {steps_count[position]}")
    
tracedwalk()

# Example Output
Enter the length of the pavement: 5
Square Steps
2 0
3 1
4 2
5 1



# Exercise 11

def recommendFriends():
    yourFriends = input("Enter your friends (separated by commas): ").split(", ")
    
    # set to store names of friends
    recommendedFriends = set()
    
    for friend in yourFriends:
        friendFriends = input(f"Enter {friend}'s friends (separated by commas): ").split(", ")
        if not recommendedFriends:
            recommendedFriends.update(friendFriends)
        else:
            recommendedFriends.intersection_update(friendFriends)
    
    recommendedFriends.difference_update(yourFriends)
    
    if recommendedFriends:
        recommendedFriendsStr = ", ".join(recommendedFriends)
        print(f"Recommended new friends for you: {recommendedFriendsStr}")
    else:
        print("No new friends to recommend.")

recommendFriends()
