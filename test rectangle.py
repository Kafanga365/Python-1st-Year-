from graphics import *

def finalPatch():
    win = GraphWin("final patch only", 100, 100)
    gap = 20  # Gap between the squares
    
    # Define the rectangles for the final patch one by one
    rect1 = Rectangle(Point(0, 0), Point(100, 100))
    rect1.setFill("red")
    rect1.draw(win)

    rect2 = Rectangle(Point(gap, gap), Point(100 - gap, 100 - gap))
    rect2.setFill("white")
    rect2.draw(win)

    rect3 = Rectangle(Point(gap * 2, gap * 2), Point(100 - gap * 2, 100 - gap * 2))
    rect3.setFill("red")
    rect3.draw(win)

    rect4 = Rectangle(Point(gap * 3, gap * 3), Point(100 - gap * 3, 100 - gap * 3))
    rect4.setFill("white")
    rect4.draw(win)

    rect5 = Rectangle(Point(gap * 4, gap * 4), Point(100 - gap * 4, 100 - gap * 4))
    rect5.setFill("red")
    rect5.draw(win)

    rect6 = Rectangle(Point(gap * 5, gap * 5), Point(100 - gap * 5, 100 - gap * 5))
    rect6.setFill("white")
    rect6.draw(win)

    rect7 = Rectangle(Point(gap * 6, gap * 6), Point(100 - gap * 6, 100 - gap * 6))
    rect7.setFill("red")
    rect7.draw(win)

    rect8 = Rectangle(Point(gap * 7, gap * 7), Point(100 - gap * 7, 100 - gap * 7))
    rect8.setFill("white")
    rect8.draw(win)

    rect9 = Rectangle(Point(gap * 8, gap * 8), Point(100 - gap * 8, 100 - gap * 8))
    rect9.setFill("white")
    rect9.draw(win)

    rect10 = Rectangle(Point(gap * 9, gap * 9), Point(100 - gap * 9, 100 - gap * 9))
    rect10.setFill("red")
    rect10.draw(win)

    win.getMouse()
    win.close()

finalPatch()