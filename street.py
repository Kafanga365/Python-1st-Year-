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

def drawStreet(numHouses, windowHeight, doorColor, lightProbability):
    win = GraphWin("Street", numHouses * 100, windowHeight)
    win.setBackground("white")

    houseWidth = 100
    houseHeight = windowHeight

    for i in range(numHouses):
        x = i * houseWidth
        y = 0

        doorNumber = i + 1
        isLightOn = random.random() < lightProbability

        drawHouse(win, x, y, houseWidth, houseHeight, doorColor, doorNumber, isLightOn)

    win.getMouse()
    win.close()

# Example usage
numHouses = int(input("Enter the number of houses: "))
windowHeight = int(input("Enter the height of the graphics window: "))
doorColor = input("Enter the shared door color: ")
lightProbability = float(input("Enter the probability that any light is on: "))

drawStreet(numHouses, windowHeight, doorColor, lightProbability)