from graphics import *
import time
from random import randint
def countDown():
    i = 10
    while i > 0:
        print(i, "...", end=" ")
        i = i - 1
    print("Blast Off!")


# Note: msg == "" needs to appear twice here
def getString1():
    msg = ""
    while msg == "":
        msg = input("Enter a non-empty string: ")
        if msg == "":
            print("You didn't enter anything!")
    return msg


def getString2():
    while True:
        msg = input("Enter a non-empty string: ")
        if msg != "":
            break
        print("You didn't enter anything!")
    return msg


def addUpNumbers1():
    total = 0
    more = "y"
    while more == "y":  # The loop runs while `more` is "y"
        number = int(input("Enter a number "))
        total = total + number
        more = input("Any more numbers? ")
    print("The total is", total)


def addUpNumbers2():
    total = 0
    number = int(input("Number (0 to stop): "))
    while number != 0:  # The loop runs while `number` is not 0
        total = total + number
        number = int(input("Number (0 to stop): "))
    print("The total is", total)


def addUpNumbers3():
    total = 0
    nStr = input("Number (hit enter to stop): ")
    while nStr != "":  # The loop runs while `nStr` is not empty
        number = int(nStr)  # Assumes that `nStr` contains a number
        total = total + number
        nStr = input("Number (hit enter to stop): ")
    print("The total is", total)


def addUpNumbers4():
    total = 0
    while True:  # The loop runs until we break it
        nStr = input("Number (anything else to stop): ")
        if not nStr.isdigit():
            break  # Break the loop if `nStr` is not a number
        number = int(nStr)
        total = total + number
    print("The total is", total)

def canApplyForJob(degree, experience):
    if (degree == "1st" or degree == "2:1") and experience >= 1:
        return True
    elif degree == "2:2" and experience >= 2:
        return True
    else:
        return False


def getPositiveNumber1():
    number = 0
    while number <= 0:
        number = int(input("Enter a positive number: "))
    return number

def getPositiveNumber2():
    while True:
        number = int(input("Enter a positive number: "))
        if number > 0:
            break
    return number

# Exercise 1 
def getName():
    while True:
        name = input("Please enter a valid name: ")
    if name.isalpha():
        return name
    else:
        print("Invalid name. Please try again.")

# Exercise 2
def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        # Red light(stop)
        amber.setFill("black")
        red.setFill("red")
        green.setFill("black")
        time.sleep(5)
        
        # Red/Amber light
        amber.setFill("yellow")
        time.sleep(2)
        
        # Green light
        red.setFill("black")
        amber.setFill("black")
        green.setFill("green")
        time.sleep(5)
        
        # Amber light
        green.setFill("black")
        amber.setFill("yellow")
        time.sleep(2)
    
        if win.checkMouse():
            win.close()
            break

trafficLights()

# Exercise 3
def calculateGrade(mark):
    if mark >= 16:
        grade = 'A'
    elif mark >= 12:
        grade = 'B'
    elif mark >= 8:
        grade = 'C'
    else:
        grade = 'X'
        
    return grade

def gradeCoursework():
    while True:
        try:
            mark = float(input("Enter the mark: "))
            if 0 <= mark <= 20:
                break
            else:
                print("Invalid mark. Please enter a mark between 0 and 20.")
        except ValueError:
            print("Invalid input. Please enter a valid numerical mark.")
        except:
            print("An error occurred. Please try again.")

    grade = calculateGrade(mark)
    print("Grade: ", grade)

gradeCoursework()


# Exercise 4
def orderPrice():
    total_price = 0.0

    while True:
        try:
            unit_price = float(input("Enter the unit price of the product in pounds: "))
            quantity = int(input("Enter the quantity of the product: "))
            total_price += unit_price * quantity

            more_products = input("Are there any more products in the order? (yes/no): ")
            if more_products.lower() == "no":
                break
            elif more_products.lower() != "yes":
                print("Invalid input. Assuming no more products.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid unit price and quantity.")

    print("Total order price: £{:.2f}".format(total_price))

orderPrice()


# Exercise 5
def clickableEye():
    win = GraphWin("Clickable Eye", 500, 500)
    eye_center = Point(250, 250)
    eye_radius = 100
    
    # Brown eye
    eye = Circle(eye_center, eye_radius)
    eye.setFill("brown")
    eye.draw(win)
    
    # labels for the eye parts
    pupil_label = Text(Point(250, 400), "Pupil")
    iris_label = Text(Point(150, 400), "Iris")
    sclera_label = Text(Point(350, 400), "Sclera")
    labels = [pupil_label, iris_label, sclera_label]
    
    for label in labels:
        label.draw(win)
    
    while True:
        # User click
        click_point = win.getMouse()
        
        # if click is outside the eye
        if not (click_point.getX() >= (eye_center.getX() - eye_radius) and
                click_point.getX() <= (eye_center.getX() + eye_radius) and
                click_point.getY() >= (eye_center.getY() - eye_radius) and
                click_point.getY() <= (eye_center.getY() + eye_radius)):
            break
        

        if click_point.getX() >= (eye_center.getX() - eye_radius/2) and \
                click_point.getX() <= (eye_center.getX() + eye_radius/2) and \
                click_point.getY() >= (eye_center.getY() - eye_radius/2) and \
                click_point.getY() <= (eye_center.getY() + eye_radius/2):
            part_name = "Pupil"
        elif click_point.getX() >= (eye_center.getX() - eye_radius/1.5) and \
                click_point.getX() <= (eye_center.getX() + eye_radius/1.5) and \
                click_point.getY() >= (eye_center.getY() - eye_radius/1.5) and \
                click_point.getY() <= (eye_center.getY() + eye_radius/1.5):
            part_name = "Iris"
        else:
            part_name = "Sclera"
        
        # Displays clicked part below the eye
        label_text = Text(Point(250, 450), part_name)
        label_text.setSize(14)
        label_text.draw(win)
        
        # click removes the label
        win.getMouse()
        label_text.undraw()
    
    # Close the window 
    win.close()


clickableEye()


# Exercise 6
def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32

def temperatureConverter():
    while True:
        conversionType = input("Please choose the conversion type: 1. Fahrenheit to Celsius, 2. Celsius to Fahrenheit, 3. Quit\n")

        if conversionType == "1":
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            celsius = fahrenheit2Celsius(fahrenheit)
            print("Temperature in Celsius: {:.2f}".format(celsius))
        elif conversionType == "2":
            celsius = float(input("Enter the temperature in Celsius: "))
            fahrenheit = celsius2Fahrenheit(celsius)
            print("Temperature in Fahrenheit: {:.2f}".format(fahrenheit))
        elif conversionType == "3":
            print("Quitting the temperature converter.")
            break
        else:
            print("Invalid input. Please enter a valid option.")

temperatureConverter()



# Exercise 7
def TableTennisScorer():
    win = GraphWin("Table Tennis Scorer", 500, 300)
    win.setBackground("white")

    # Left and right sides for Player 1 and Player 2
    leftSide = Rectangle(Point(0, 0), Point(250, 300))
    rightSide = Rectangle(Point(250, 0), Point(500, 300))
    leftSide.setFill("lightgray")
    rightSide.setFill("lightgray")
    leftSide.draw(win)
    rightSide.draw(win)

    # Labels for Player 1 and Player 2
    player1Label = Text(Point(125, 150), "Player 1")
    player2Label = Text(Point(375, 150), "Player 2")
    player1Label.setSize(20)
    player2Label.setSize(20)
    player1Label.draw(win)
    player2Label.draw(win)

    # Initial scores for Player 1 and Player 2
    player1Score = 0
    player2Score = 0

    # Score labels for Player 1 and Player 2
    player1ScoreLabel = Text(Point(125, 200), str(player1Score))
    player2ScoreLabel = Text(Point(375, 200), str(player2Score))
    player1ScoreLabel.setSize(14)
    player2ScoreLabel.setSize(14)
    player1ScoreLabel.draw(win)
    player2ScoreLabel.draw(win)

    while True:
        # User click
        clickPoint = win.getMouse()

        # if the click is on the left side
        if clickPoint.getX() <= 250:
            player1Score += 1
            player1ScoreLabel.setText(str(player1Score))

            # if Player 1 has won
            if player1Score >= 11 and player1Score - player2Score >= 2:
                winnerLabel = Text(Point(125, 250), "Player 1 wins!")
                winnerLabel.setSize(14)
                winnerLabel.setTextColor("green")
                winnerLabel.draw(win)
                break

        # if the click is on the right side
        elif clickPoint.getX() > 250:
            player2Score += 1
            player2ScoreLabel.setText(str(player2Score))

            # if Player 2 has won
            if player2Score >= 11 and player2Score - player1Score >= 2:
                winnerLabel = Text(Point(375, 250), "Player 2 wins!")
                winnerLabel.setSize(14)
                winnerLabel.setTextColor("green")
                winnerLabel.draw(win)
                break

    # Close the window 
    win.getMouse()
    win.close()

# Call the TableTennisScorer function 
TableTennisScorer()



# Exercise 8
from random import randint

def guessTheNumber():
    numberToGuess = randint(1, 100)
    numGuesses = 0

    while numGuesses < 7:
        userGuess = int(input("Enter your guess: "))

        if userGuess < numberToGuess:
            print("Too low")
        elif userGuess > numberToGuess:
            print("Too high")
        else:
            print("You win! - It took you", numGuesses + 1, "guess(es).")
            return

        numGuesses += 1

    print("You lose! - The number was", numberToGuess)

# Call the game
guessTheNumber()





# Exercise 9
def clickableBoxOfEyes(rows, columns):
    eyeRadius = 50
    padding = 50
    eyeSpacing = 2 * eyeRadius + padding

    winWidth = columns * eyeSpacing + padding
    winHeight = rows * eyeSpacing + padding

    win = GraphWin("Clickable Box of Eyes", winWidth, winHeight)
    box = Rectangle(Point(padding, padding), Point(winWidth - padding, winHeight - padding))
    box.draw(win)

    eyes = [[Circle(Point(padding + (col + 0.5) * eyeSpacing, padding + (row + 0.5) * eyeSpacing), eyeRadius)
             .setFill("blue").draw(win) for col in range(columns)] for row in range(rows)]

    while True:
        clickPoint = win.getMouse()
        if not (padding < clickPoint.getX() < winWidth - padding and padding < clickPoint.getY() < winHeight - padding):
            break

        clickedRow = int((clickPoint.getY() - padding) / eyeSpacing) + 1
        clickedCol = int((clickPoint.getX() - padding) / eyeSpacing) + 1

        message = (f"Clicked on eye at row {clickedRow}, column {clickedCol}"
                   if 1 <= clickedRow <= rows and 1 <= clickedCol <= columns else "Between eyes")

        Text(Point(winWidth // 2, winHeight - 20), message).setSize(16).draw(win)

    win.close()

clickableBoxOfEyes(4, 3)
