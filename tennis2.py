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