import tkinter as tk

# Defines the Boolean operator
def booleanOperator(a, b):
    return a or b

window = tk.Tk()
window.title("Boolean Operator Truth Table")

# four rows for the truth table
rows = [
    [False, False],
    [False, True],
    [True, False],
    [True, True]
]

# BooleanVar variables for user input
userInputs = [tk.BooleanVar() for _ in range(4)]

# labels and entry boxes for each row
for i, row in enumerate(rows):
    label = tk.Label(window, text=f"{row[0]} or {row[1]} = ")
    label.grid(row=i, column=0)

    entry = tk.Entry(window, textvariable=userInputs[i])
    entry.grid(row=i, column=1)

# Check the user's predictions
def checkPredictions():
    correctAnswers = [booleanOperator(row[0], row[1]) for row in rows]
    userAnswers = [var.get() for var in userInputs]

    for i, answer in enumerate(userAnswers):
        if answer == correctAnswers[i]:
            result = "Correct"
        else:
            result = "Incorrect"
        print(f"Prediction #{i+1}: {result}")


checkButton = tk.Button(window, text="Check Predictions", command=checkPredictions)
checkButton.grid(row=len(rows), column=0, columnspan=2)


def closeWindow():
    window.destroy()

closeButton = tk.Button(window, text="Close", command=closeWindow)
closeButton.grid(row=len(rows)+1, column=0, columnspan=2)

window.mainloop()