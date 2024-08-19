from graphics import *

def create_patchwork(design, size):
    win = GraphWin("Patchwork", size*100, size*100)

    colors = ["blue", "orange", "red"]
    digit_designs = {
        0: [0, 0, 0, 0, 0,
            0, 1, 1, 1, 0,
            0, 1, 0, 1, 0,
            0, 1, 0, 1, 0,
            0, 0, 0, 0, 0],
        # Add other digit designs here for other designs
    }

    design = digit_designs.get(design, [])

    if len(design) == 0:
        print("Design not found.")
        return

    for i in range(size):
        for j in range(size):
            x = i * 100
            y = j * 100
            index = i + (j * size)
            color = colors[design[index]]

            rect = Rectangle(Point(x, y), Point(x + 100, y + 100))
            rect.setFill(color)
            rect.draw(win)

    win.mainloop()

# Example usage
create_patchwork(0, 5)  # Create Design 0 as a 5x5 patchwork
create_patchwork(0, 7)  # Create Design 0 as a 7x7 patchwork