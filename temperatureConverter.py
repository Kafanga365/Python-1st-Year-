import tkinter as tk

def convertToFahrenheit():
    celsius = float(celsiusEntry.get())
    fahrenheit = (celsius * 9/5) + 32
    fahrenheitEntry.delete(0, tk.END)
    fahrenheitEntry.insert(tk.END, str(fahrenheit))

def convertToCelsius():
    fahrenheit = float(fahrenheitEntry.get())
    celsius = (fahrenheit - 32) * 5/9
    celsiusEntry.delete(0, tk.END)
    celsiusEntry.insert(tk.END, str(celsius))

def closeWindow():
    window.destroy()


window = tk.Tk()
window.title("Temperature Converter")


celsiusLabel = tk.Label(window, text="Celsius:")
celsiusLabel.pack()
celsiusEntry = tk.Entry(window)
celsiusEntry.pack()


fahrenheitLabel = tk.Label(window, text="Fahrenheit:")
fahrenheitLabel.pack()
fahrenheitEntry = tk.Entry(window)
fahrenheitEntry.pack()

# "Convert to Fahrenheit" button
toFahrenheitButton = tk.Button(window, text="Convert to Fahrenheit", command=convertToFahrenheit)
toFahrenheitButton.pack()

# "Convert to Celsius" button
toCelsiusButton = tk.Button(window, text="Convert to Celsius", command=convertToCelsius)
toCelsiusButton.pack()


closeButton = tk.Button(window, text="Close", command=closeWindow)
closeButton.pack()


window.mainloop()