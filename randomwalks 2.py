from random import choice

def main():
    numWalks, numSteps = getInputs()
    averageDistance = takeWalks(numWalks, numSteps)
    printExpectedDistance(averageDistance)

def getInputs():
    numWalks = int(input("How many random walks to take? "))
    numSteps = int(input("How many steps for each walk? "))
    return numWalks, numSteps

def takeWalks(numWalks, numSteps):
    totalDistance = 0
    for walk in range(numWalks):
        distance = takeAWalk(numSteps)
        totalDistance += distance
    return totalDistance / numWalks

def printExpectedDistance(averageDistance):
    print("The expected distance from the starting point is", averageDistance)

def takeAWalk(numSteps):
    x = 0
    y = 0
    for step in range(numSteps):
        direction = choice(["north", "east", "south", "west"])
        if direction == "north":
            y += 1
        elif direction == "east":
            x += 1
        elif direction == "south":
            y -= 1
        elif direction == "west":
            x -= 1
    return distanceBetweenPoints(0, x, 0, y)

def distanceBetweenPoints(x1, x2, y1, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if __name__ == "__main__":
    main()