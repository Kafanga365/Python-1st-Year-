from graphics import *
from time import *



#### CORE FUNCTIONS TO BE USED IN CAR
def drawRectangle(win, tl, br, colour):
    rectangle = Rectangle(tl,br)
    rectangle.setFill(colour)
    rectangle.draw(win)
    return rectangle

def drawCircle(win, center, radius, colour):
    circle = Circle(center,radius)
    circle.setFill(colour)
    circle.draw(win)
    return circle


#### CAR PARTS
def buildCarTop(topLeftX, topLeftY, widthCarTop, heightCarTop, carColour, win, car):
    topLeftPoint = Point(topLeftX, topLeftY)
    bottomRightPoint = Point(topLeftX + widthCarTop, topLeftY + heightCarTop)
    carTop = drawRectangle(win, topLeftPoint, bottomRightPoint, carColour)
    car.append(carTop)

def buildCarBody(topLeftX, topLeftY, widthCarTop, heightCarTop, diff, carColour, win, car):
    topLeftPoint = Point(topLeftX-diff, topLeftY+heightCarTop)
    bottomRightPoint = Point(topLeftX + widthCarTop + diff, topLeftY + heightCarTop + heightCarTop)
    carBody = drawRectangle(win, topLeftPoint, bottomRightPoint, carColour)
    car.append(carBody)

def buildLeftWheel(topLeftX, topLeftY, heightCarTop, carColour, win, car):
    center = Point(topLeftX, topLeftY + heightCarTop + heightCarTop )
    radius = heightCarTop/2   
    blackCircle = drawCircle(win, center, radius, "black")
    car.append(blackCircle)
    radius = radius - 10   
    whiteCircle = drawCircle(win, center, radius, "white")
    car.append(whiteCircle)    

def buildRightWheel(topLeftX, topLeftY, widthCarTop, heightCarTop, carColour, win, car):
    center = Point(topLeftX + widthCarTop, topLeftY + heightCarTop + heightCarTop )
    radius = heightCarTop/2 
    blackCircle = drawCircle(win, center, radius, "black")  
    car.append(blackCircle)
    radius = radius - 10
    whiteCircle = drawCircle(win, center, radius, "white")
    car.append(whiteCircle)


def buildCar(topLeftX, topLeftY, widthCarTop, heightCarTop, diff, carColour, win, car):
    buildCarTop(topLeftX, topLeftY, widthCarTop, heightCarTop, carColour, win, car)
    buildCarBody(topLeftX, topLeftY, widthCarTop, heightCarTop, diff, carColour, win, car)
    buildLeftWheel(topLeftX, topLeftY, heightCarTop, carColour, win, car)
    buildRightWheel(topLeftX, topLeftY, widthCarTop, heightCarTop, carColour, win, car)

##### PROGRAM
def main():
    win = GraphWin('',800,500)
    car = []
    #intial values to wset up car
    topLeftX = 100
    topLeftY = 130
    widthCarTop = 150
    heightCarTop = 70
    diff = 30
    buildCar(topLeftX, topLeftY, widthCarTop, heightCarTop, diff, 'blue', win, car)
    win.getMouse()
    for _ in range(1000):
        sleep(.01)
        for carPart in car:
            carPart.move(1,0)
    win.getMouse()


main()



