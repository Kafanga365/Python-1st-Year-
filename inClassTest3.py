from graphics import *

def drawCircles():
    # Create the graphics window
    win = GraphWin("Circles", 400, 400)

    # Loop to draw 15 circles
    for _ in range(15):
        # Wait for a mouse click
        clickPoint = win.getMouse()

        # Calculate the circle's center coordinates
        centerX = clickPoint.getX()
        centerY = clickPoint.getY()

        # Determine the circle's color based on the y-coordinate
        if centerY < 100:
            color = "blue"
        elif centerY < 200:
            color = "green"
        elif centerY < 300:
            color = "red"
        else:
            color = "yellow"

        # Create the circle shape
        circle = Circle(Point(centerX, centerY), 20)
        circle.setOutline(color)
        circle.setFill(color)

        # Draw the circle on the graphics window
        circle.draw(win)

    # Close the graphics window when finished
    win.close()

# Call the drawCircles function
drawCircles()




from graphics import *

def drawCircles2():
    # Create the graphics window
    win = GraphWin("Circles", 400, 400)

    # Define the colors based on y-coordinate
    color_map = {0: "blue", 1: "green", 2: "red", 3: "yellow"}

    # Calculate the starting x and y coordinates for the circles
    start_x = 280
    start_y = 40

    # Loop to draw 30 circles
    for i in range(30):
        # Calculate the row and column indices for the circle
        row = i // 3
        col = i % 3

        # Calculate the center coordinates for the circle
        centerX = start_x + col * 40
        centerY = start_y + row * 80

        # Determine the circle's color based on the row index
        color_index = row % 4
        color = color_map[color_index]

        # Create the circle shape
        circle = Circle(Point(centerX, centerY), 20)
        circle.setOutline(color)
        circle.setFill(color)

        # Draw the circle on the graphics window
        circle.draw(win)

    # Wait for a mouse click to close the window
    win.getMouse()

    # Close the graphics window
    win.close()

# Call the drawCircles2 function
drawCircles2()

