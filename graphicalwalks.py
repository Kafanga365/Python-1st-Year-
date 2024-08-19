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