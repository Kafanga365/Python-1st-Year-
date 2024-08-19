import tkinter as tk
from tkinter import messagebox

def areaOfCircle(radius):
    return 3.14 * radius * radius

def circumferenceOfCircle(radius):
    return 2 * 3.14 * radius

def calculateCircleInfo():
    radius = float(entry.get())
    area = areaOfCircle(radius)
    circumference = circumferenceOfCircle(radius)
    areaLabel.config(text=f"Area: {area} cm²")
    circumferenceLabel.config(text=f"Circumference: {circumference} cm")

def closeWindow():
    window.destroy()

window = tk.Tk()
window.title("Circle Info")
window.geometry("300x200")

radiusLabel = tk.Label(window, text="Enter the radius (cm):")
radiusLabel.pack()

entry = tk.Entry(window)
entry.pack()

calculateButton = tk.Button(window, text="Calculate", command=calculateCircleInfo)
calculateButton.pack()

areaLabel = tk.Label(window, text="Area:")
areaLabel.pack()

circumferenceLabel = tk.Label(window, text="Circumference:")
circumferenceLabel.pack()

closeButton = tk.Button(window, text="Close", command=closeWindow)
closeButton.pack()

window.mainloop()