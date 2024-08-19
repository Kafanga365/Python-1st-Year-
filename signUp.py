import tkinter as tk
from tkinter import messagebox
import csv

def saveLoginDetails(username, password):
    with open('loginDetails.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def validatePassword(password):
    if len(password) < 5:
        return "Password must be at least 5 characters long."
    if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        return "Password must contain at least one letter and one number."
    return ""

def handleSignup():
    username = usernameEntry.get()
    password = passwordEntry.get()

    # Password Validation
    validationMessage = validatePassword(password)
    if validationMessage:
        messagebox.showwarning("Warning", validationMessage)
        return

    # Save login details
    saveLoginDetails(username, password)
    messagebox.showinfo("Success", "Account created successfully!")
    signupWindow.destroy()

def togglePasswordVisibility():
    if showPasswordVar.get():
        passwordEntry.config(show="")
    else:
        passwordEntry.config(show="*")

signupWindow = tk.Tk()
signupWindow.title("Employee Sign Up")

usernameLabel = tk.Label(signupWindow, text="Username:")
usernameLabel.pack()
usernameEntry = tk.Entry(signupWindow)
usernameEntry.pack()

passwordLabel = tk.Label(signupWindow, text="Password:")
passwordLabel.pack()
passwordEntry = tk.Entry(signupWindow, show="*")
passwordEntry.pack()

showPasswordVar = tk.BooleanVar()
showPasswordCheckbox = tk.Checkbutton(signupWindow, text="Show Password", variable=showPasswordVar, command=togglePasswordVisibility)
showPasswordCheckbox.pack()

signupButton = tk.Button(signupWindow, text="Sign Up", command=handleSignup)
signupButton.pack()

signupWindow.mainloop()