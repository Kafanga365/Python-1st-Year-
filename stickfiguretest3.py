from graphics import *

def theBoxer():
    win = GraphWin("Stick figure", 300, 200)
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arms = Line(Point(60, 90), Point(140, 90))
    arms.draw(win)
    leg1 = Line(Point(100, 120), Point(70, 170))
    leg1.draw(win)
    leg2 = Line(Point(100, 120), Point(130, 170))
    leg2.draw(win)
    
# left glove
    leftGlove = Circle(Point(40, 90), 20)
    leftGlove.draw(win)
    leftGlove.setFill("Red")
    
# right glove
    rightGlove = Circle(Point(160, 90), 20)
    rightGlove.draw(win)
    rightGlove.setFill("Red")
    
# eye 1
    eye1 = Circle(Point(90, 60), 3)
    eye1.draw(win)
    
# eye 2
    eye2 = Circle(Point(110, 60), 3)
    eye2.draw(win)
    
# display 'punch me' on the diagram
    message = Text(Point(230, 50), "punch me!")
    message.draw(win)
    
    # Initialize punch count and shout
    punch_count = 0
    shout = "ow"
    
    def punch(event):
        nonlocal punch_count, shout
        
        if punch_count < 9:
            # Increment punch count and update shout
            punch_count += 1
            shout += "o"
            
            # Update boxer's shout
            message.setText(shout)
        elif punch_count == 9:
            # Increment punch count and update shout
            punch_count += 1
            shout += "o"
            
            # Update boxer's shout and give a black eye
            message.setText("OK, that's enough!")
            eye1.setFill("black")
            eye2.setFill("black")
            
        # Move the gloves to simulate a punch
        leftGlove.move(10, 0)
        rightGlove.move(-10, 0)

    # Bind the punch function to the mouse click event
    win.bind("<Button-1>", punch)

    # Run the graphics main loop
    win.mainloop()

# Call the theBoxer function to start the game
theBoxer()