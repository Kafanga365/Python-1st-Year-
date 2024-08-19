import tkinter as tk

def recommendActivity():
    temperature = float(tempEntry.get())

    if temperature > 25:
        recommendation = "You should go swimming in the sea."
    elif temperature >= 10:
        recommendation = "You should stay at home and watch a film."
    else:
        recommendation = "You should go skiing."

    recommendationLabel.configure(text=recommendation)

def closeWindow():
    window.destroy()


window = tk.Tk()
window.title("What to Do Today")
window.geometry("300x200")

# temperature input label and entry
tempLabel = tk.Label(window, text="Enter today's temperature:")
tempLabel.pack()

tempEntry = tk.Entry(window)
tempEntry.pack()


recommendButton = tk.Button(window, text="Recommend", command=recommendActivity)
recommendButton.pack()


recommendationLabel = tk.Label(window, text="")
recommendationLabel.pack()


closeButton = tk.Button(window, text="Close", command=closeWindow)
closeButton.pack()


window.mainloop()