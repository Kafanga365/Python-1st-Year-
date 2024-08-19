def personalGreeting():
    # Ask the user for their name
    name = input("What is your name? ")
    
    # Create a personalised greeting
    greeting = f"Hello, {name}! Nice to meet you."
    
    #Output the greeting
    print(greeting)
    
    # Call the function to run it
    personalGreeting()
    
    
def formalName():
    #Ask the user for their given name and family name
        givenName = input("What's your given name? ")
        familyName = input("What;s your family name? ")
        
    # Create a formal version of the name
        formalVersion = f"Mr. {givenName} {familyName}"
    
    # Output the formal name
        print("Your formal name is:", formalVersion)
    
    # Call the function to run it
        (formalName)
        
# A simple kilograms to ounces conversion program
# It asks for a weight in kilograms (for example 10)
# and converts it to ounces (352.74)
def kilos2Ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = kilos * 35.274
    print("The weight in ounces is", ounces)
    
# modified version of the kilograms to ounces conversion program
# this will display the output in the form of a message
# the user's kilos value and the calculated values are displayed to 2.d.p.

def modifiedKilosToOunces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = kilos * 35.274
# format to two decimal places 
    formattedKilos = "{:.2f}".format(kilos)
# format ounces to two decimal places
    formattedOunces = "{:.2f}".format(ounces)
    message = f"{formattedKilos} kilos is equal to {formattedOunces} ounces"
    print(message)
    
# Call the function to run it


def generateEmail(firstName, lastName, entryYear):
# find the first 4 letters of the surname
# find the first letter of the forename
# find the last two digits of the entry year
    surnamePart = LastName[:4].lower()
    forenamePart = firstName[0].lower()
    yearPart = str(entryYear)[-2:]

# combine the surname, forename and entry year parts
    email = f"{surnamePart}.{forenamePart}.{yearPart}@university.edu"
    return email


# using elif specifies and alternative condition (e.g. 'else if')
def gradeTest():
    mark = float(input("Enter the mark (between 0 and 10): "))
    
    if mark < 0 or mark > 10:
        print("Invalid mark! Please enter a mark between 0 and 10.")
    elif mark >= 9:
        print("Grade: A")
    elif mark >= 7:
        print("Grade: B")
    elif mark >= 5:
        print("Grade: C")
    else:
        print("Grade: F")
    
    return mark

mark = gradeTest()
print("The entered mark is:", mark)


from graphics import *

def graphicLetters():
    # Get the word from the user
    word = input("Enter a word: ")
    
    # Open a graphics window
    win = GraphWin("Graphic Letters", 400, 300)
    
    for letter in word:
        # Prompt the user to click the mouse
        click_point = win.getMouse()
        
        # Create a Text object for the letter
        text = Text(click_point, letter)
        text.setSize(36)  # Set the text size to make it appear big
        
        # Draw the letter in the graphics window
        text.draw(win)
    
    # Wait for the user to click to close the window
    win.getMouse()
    win.close()

# Call the function to start the program
graphicLetters()



def singASong():
    # Get the word from the user
    word = input("Enter a word: ")
    
    # Get the number of lines and repetitions from the user
    num_lines = int(input("Enter the number of lines: "))
    num_repetitions = int(input("Enter the number of times to repeat the word on each line: "))
    
    # Generate and print the song
    for _ in range(num_lines):
        line = word * num_repetitions
        print(line)

# Call the function to start the program
singASong()



def exchangeTable():
    exchange_rate = 1.17
    
    # Print the table header
    print("{:>10s} {:>10s}".format("Euro (€)", "Pound (£)"))
    
    # Generate and print the table rows
    for euro in range(21):
        pound = euro * exchange_rate
        print("{:>10d} {:>10.2f}".format(euro, pound))

# Call the function to generate the exchange table
exchangeTable()



def makeInitialism():
    # Get the phrase from the user
    phrase = input("Enter a phrase: ")
    
    # Split the phrase into words
    words = phrase.split()
    
    # Extract the first letter of each word and convert to uppercase
    initials = [word[0].upper() for word in words]
    
    # Print the initialism
    print("Initialism:", ''.join(initials))

# Call the function to start the program
makeInitialism()