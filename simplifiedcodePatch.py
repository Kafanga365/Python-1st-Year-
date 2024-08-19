from graphics import *

def drawSquare(win, center, size, color):
    square = Rectangle(Point(center.getX() - size / 2, center.getY() - size / 2),
                       Point(center.getX() + size / 2, center.getY() + size / 2))
    square.setFill(color)
    square.draw(win)
    
    if size > 10:  # conditional statement  
        new_size = size - 10
        new_color = "red" if color == "white" else "white"  # Alternate the color
        drawSquare(win, center, new_size, new_color)

def finalPatch():
    win = GraphWin("Final Patch Only", 300, 300)
    
    rect1Center = Point(50, 50)  # Center point of the initial square
    rect1Size = 100  # Size of the first square
    rect1Color = "red"  # First color
    drawSquare(win, rect1Center, rect1Size, rect1Color)
    
    rect2Center = Point(50, 50)  
    rect2Size = 90  
    rect2Color = "white"  
    drawSquare(win, rect2Center, rect2Size, rect2Color)
    
    rect3Center = Point(50, 50)  
    rect3Size = 80  
    rect3Color = "red"  
    drawSquare(win, rect3Center, rect3Size, rect3Color)
    
    rect4Center = Point(50, 50)  
    rect4Size = 70  
    rect4Color = "white"  
    drawSquare(win, rect4Center, rect4Size, rect4Color)
    
    rect5Center = Point(50, 50)  
    rect5Size = 60  
    rect5Color = "red"  
    drawSquare(win, rect5Center, rect5Size, rect5Color)
    
    rect6Center = Point(50, 50)  
    rect6Size = 50  
    rect6Color = "white"  
    drawSquare(win, rect6Center, rect6Size, rect6Color)
    
    rect7Center = Point(50, 50)  
    rect7Size = 40  
    rect7Color = "red"  
    drawSquare(win, rect7Center, rect7Size, rect7Color)
    
    rect8Center = Point(50, 50)  
    rect8Size = 30
    rect8Color = "white"  
    drawSquare(win, rect8Center, rect8Size, rect8Color)
    
    rect9Center = Point(50, 50)  
    rect9Size = 20  
    rect9Color = "red"  
    drawSquare(win, rect9Center, rect9Size, rect9Color)
    
    rect10Center = Point(50, 50)  
    rect10Size = 10  
    rect10Color = "white"  
    drawSquare(win, rect10Center, rect10Size, rect10Color)
    
    win.getMouse()
    win.close()


finalPatch()