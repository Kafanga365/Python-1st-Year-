from random import randint, random
from graphics import *

def tenCoinFlips():
    for i in range(10):
        randomNumber = randint(1, 2)
        if randomNumber == 1:
            print("Heads")
        else:
            print("Tails")


def tenDiceRolls():
    for i in range(10):
        diceRoll = randint(1, 6)
        print(diceRoll)


def tenBiasedCoinFlips():
    headsCount = 0
    totalFlips = 10
    for i in range(totalFlips):
        randomNumber = random()
        if randomNumber < 0.85:
            print("Heads")
            headsCount += 1
        else:
            print("Tails")
    print("Heads count: ", headsCount)
    # Every time we didn't have heads, we had tails
    print("Tails count: ", totalFlips - headsCount)



# Exercise 1
import random

def getInputs():
    num_flips = int(input("Enter the number of times to flip the coin: "))
    return num_flips

def simulateFlips(num_flips):
    heads_count = 0
    tails_count = 0
    
    for _ in range(num_flips):
        if random.random() < 0.5:
            heads_count += 1
        else:
            tails_count += 1
    
    return heads_count, tails_count

def displayResults(heads_count, tails_count):
    total_flips = heads_count + tails_count
    heads_proportion = heads_count / total_flips
    tails_proportion = tails_count / total_flips
    
    print(f"Heads {heads_proportion:.2f}, Tails {tails_proportion:.2f}")

def main():
    num_flips = getInputs()
    heads_count, tails_count = simulateFlips(num_flips)
    displayResults(heads_count, tails_count)

if __name__ == "__main__":
    main()
    

# Exercise 2
from graphics import *

def drawHouse2(doorColour, lightsOn, windowSize, doorNumber):
    win = GraphWin("House", windowSize, windowSize)
    win.setCoords(0, 0, windowSize, windowSize)

    roof = Polygon(Point(0.1*windowSize, 0.3*windowSize), Point(0.4*windowSize, 0.9*windowSize),
                   Point(0.6*windowSize, 0.9*windowSize), Point(0.9*windowSize, 0.3*windowSize))
    roof.setFill("pink")
    roof.draw(win)

    # draw wall and door
    drawRectangle(win, Point(0.1*windowSize, 0.3*windowSize), Point(0.9*windowSize, 0.9*windowSize), "brown")
    drawRectangle(win, Point(0.3*windowSize, 0.55*windowSize), Point(0.7*windowSize, 0.9*windowSize), doorColour)

    # draw window
    if lightsOn:
        windowColour = "yellow"
    else:
        windowColour = "black"
    drawRectangle(win, Point(0.55*windowSize, 0.55*windowSize), Point(0.85*windowSize, 0.75*windowSize), windowColour)

    # draw door number
    doorNumberText = Text(Point(0.5*windowSize, 0.725*windowSize), str(doorNumber))
    doorNumberText.setSize(20)
    doorNumberText.draw(win)

    win.getMouse()
    win.close()

def drawRectangle(win, p1, p2, colour):
    rectangle = Rectangle(p1, p2)
    rectangle.setFill(colour)
    rectangle.draw(win)

def main():
    doorColour = input("Enter the colour of the door: ")
    lightsOn = input("Are the lights on? (yes/no): ").lower() == "yes"
    windowSize = int(input("Enter the size of the graphics window: "))
    doorNumber = int(input("Enter the number displayed on the door: "))

    drawHouse2(doorColour, lightsOn, windowSize, doorNumber)

if __name__ == "__main__":
    main()
    
    
# Exercise 3
from random import choice

def main():
    numWalks, numSteps = getInputs()
    averageDistance = takeWalks(numWalks, numSteps)
    printExpectedDistance(averageDistance)

def getInputs():
    numWalks = int(input("How many random walks to take? "))
    numSteps = int(input("How many steps for each walk? "))
    return numWalks, numSteps

def takeWalks(numWalks, numSteps):
    totalDistance = 0
    for walk in range(numWalks):
        distance = takeAWalk(numSteps)
        totalDistance += distance
    return totalDistance / numWalks

def printExpectedDistance(averageDistance):
    print("The expected distance from the starting point is", averageDistance)

def takeAWalk(numSteps):
    x = 0
    y = 0
    for step in range(numSteps):
        direction = choice(["north", "east", "south", "west"])
        if direction == "north":
            y += 1
        elif direction == "east":
            x += 1
        elif direction == "south":
            y -= 1
        elif direction == "west":
            x -= 1
    return distanceBetweenPoints(0, x, 0, y)

def distanceBetweenPoints(x1, x2, y1, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if __name__ == "__main__":
    main()
    
    
# Exercise 4
from graphics import *
from random import choice

def main():
    distance = float(input("Enter the distance from the start point: "))
    numWalks = int(input("Enter the number of walks to simulate: "))

    windowSize = 600
    win = GraphWin("Random Walks", windowSize, windowSize)
    win.setCoords(-windowSize/2, -windowSize/2, windowSize/2, windowSize/2)

    drawBoundary(win, distance)

    for walk in range(numWalks):
        traceWalk(win, distance)

    win.getMouse()
    win.close()

def drawBoundary(win, distance):
    boundary = Circle(Point(0, 0), distance)
    boundary.setOutline("black")
    boundary.setWidth(2)
    boundary.draw(win)

def traceWalk(win, distance):
    walker = Point(0, 0)
    walker.setFill("black")
    walker.draw(win)

    while distanceFromOrigin(walker) < distance:
        direction = choice(["north", "east", "south", "west"])
        moveWalker(walker, direction, 5)

def distanceFromOrigin(point):
    x = point.getX()
    y = point.getY()
    return ((x ** 2) + (y ** 2)) ** 0.5

def moveWalker(point, direction, stepSize):
    x = point.getX()
    y = point.getY()

    if direction == "north":
        point.move(0, stepSize)
    elif direction == "east":
        point.move(stepSize, 0)
    elif direction == "south":
        point.move(0, -stepSize)
    elif direction == "west":
        point.move(-stepSize, 0)

def createCircle(center, radius, color):
    circle = Circle(center, radius)
    circle.setFill(color)
    return circle

if __name__ == "__main__":
    main()




# Exercise 5
def main():
    prWinPt, numSets = getInputs()
    winsPl, winsOp = simulateNSets(prWinPt, numSets)
    printSummary(winsPl, winsOp, numSets)


def getInputs():
    prWinPt = float(input("Probability of winning a point (a float between 0 and 1): "))
    numSets = int(input("Number of sets to simulate (a positive integer): "))
    return prWinPt, numSets


def simulateNSets(prWinPt, numSets):
    winsPl, winsOp = 0, 0
    for _ in range(numSets):
        gamesPl, gamesOp = simulateSet(prWinPt)
        if gamesPl > gamesOp:
            winsPl += 1
        else:
            winsOp += 1
    return winsPl, winsOp


def simulateSet(prWinPt):
    gamesPl, gamesOp = 0, 0
    while not gameOver(gamesPl, gamesOp):
        pointsPl, pointsOp = simulateGame(prWinPt)
        if pointsPl > pointsOp:
            gamesPl += 1
        else:
            gamesOp += 1
    return gamesPl, gamesOp


def simulateGame(prWinPt):
    from random import random
    pointsPl, pointsOp = 0, 0
    while not gameOver(pointsPl, pointsOp):
        if random() < prWinPt:
            pointsPl += 1
        else:
            pointsOp += 1
    return pointsPl, pointsOp


def gameOver(pointsPl, pointsOp):
    return (pointsPl >= 4 or pointsOp >= 4) and abs(pointsPl - pointsOp) >= 2


def printSummary(winsPl, winsOp, numSets):
    proportionPl = winsPl / numSets
    proportionOp = winsOp / numSets
    print("Player wins:", winsPl, " Proportion: {0:0.2f}".format(proportionPl))
    print("Opponent wins:", winsOp, " Proportion: {0:0.2f}".format(proportionOp))


if __name__ == "__main__":
    main()




# Exercise 6
from graphics import *
from random import random

def main():
    numHouses, windowHeight, doorColor, lightProb = getInputs()

    windowWidth = numHouses * 100
    win = GraphWin("Street", windowWidth, windowHeight)
    win.setBackground("white")

    drawStreet(win, numHouses, doorColor, lightProb)

    win.getMouse()
    win.close()

def getInputs():
    numHouses = int(input("Enter the number of houses: "))
    windowHeight = int(input("Enter the height of the graphics window: "))
    doorColor = input("Enter the shared door color: ")
    lightProb = float(input("Enter the probability that any light is on (a float between 0 and 1): "))
    return numHouses, windowHeight, doorColor, lightProb

def drawStreet(win, numHouses, doorColor, lightProb):
    houseWidth = 100
    houseHeight = win.getHeight() - 50
    housePadding = 20

    for i in range(numHouses):
        x = (i * houseWidth) + (housePadding * (i + 1))
        house = drawHouse(win, Point(x, houseHeight), doorColor, lightProb)
        drawHouseNumber(win, house, i + 1)

def drawHouse(win, position, doorColor, lightProb):
    houseWidth = 100
    houseHeight = 150

    house = Rectangle(Point(position.getX() - houseWidth/2, position.getY() - houseHeight),
                      Point(position.getX() + houseWidth/2, position.getY()))
    house.setFill("lightgray")
    house.draw(win)

    door = Rectangle(Point(position.getX() - 20, position.getY() - houseHeight),
                     Point(position.getX() + 20, position.getY()))
    door.setFill(doorColor)
    door.draw(win)

    if random() < lightProb:
        light = Circle(Point(position.getX(), position.getY() - 75), 10)
        light.setFill("yellow")
        light.setOutline("yellow")
        light.draw(win)

    return house

def drawHouseNumber(win, house, number):
    position = house.getCenter()
    text = Text(Point(position.getX(), position.getY() - 120), str(number))
    text.setSize(20)
    text.setTextColor("black")
    text.draw(win)

if __name__ == "__main__":
    main()