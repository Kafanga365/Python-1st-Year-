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