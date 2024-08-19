from graphics import *

def TableTennisScorer():
    win = GraphWin("Table Tennis Scorer", 500, 300)
    win.setBackground("white")

    # Set up the left and right sides for Player 1 and Player 2
    leftSide = Rectangle(Point(0, 0), Point(250, 300))
    rightSide = Rectangle(Point(250, 0), Point(500, 300))
    leftSide.setFill("lightgray")
    rightSide.setFill("lightgray")
    leftSide.draw(win)
    rightSide.draw(win)

    # Set up the labels for Player 1 and Player 2
    player1Label = Text(Point(125, 150), "Player 1")
    player2Label = Text(Point(375, 150), "Player 2")
    player1Label.setSize(20)
    player2Label.setSize(20)
    player1Label.draw(win)
    player2Label.draw(win)

    # Set up the initial scores for Player 1 and Player 2
    player1Score = 0
    player2Score = 0

    # Set up the score labels for Player 1 and Player 2
    player1ScoreLabel = Text(Point(125, 200), str(player1Score))
    player2ScoreLabel = Text(Point(375, 200), str(player2Score))
    player1ScoreLabel.setSize(14)
    player2ScoreLabel.setSize(14)
    player1ScoreLabel.draw(win)
    player2ScoreLabel.draw(win)

    while True:
        # Wait for a user click
        clickPoint = win.getMouse()

        # Check if the click is on the left side
        if clickPoint.getX() <= 250:
            player1Score += 1
            player1ScoreLabel.setText(str(player1Score))

            # Check if Player 1 has won
            if player1Score >= 11 and player1Score - player2Score >= 2:
                winnerLabel = Text(Point(125, 250), "Player 1 wins!")
                winnerLabel.setSize(14)
                winnerLabel.setTextColor("green")
                winnerLabel.draw(win)
                break

        # Check if the click is on the right side
        elif clickPoint.getX() > 250:
            player2Score += 1
            player2ScoreLabel.setText(str(player2Score))

            # Check if Player 2 has won
            if player2Score >= 11 and player2Score - player1Score >= 2:
                winnerLabel = Text(Point(375, 250), "Player 2 wins!")
                winnerLabel.setSize(14)
                winnerLabel.setTextColor("green")
                winnerLabel.draw(win)
                break

    # Close the window when finished
    win.getMouse()
    win.close()

# Call the TableTennisScorer function to start keeping track of the points
TableTennisScorer()