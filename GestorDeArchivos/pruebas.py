import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Coordenadas para un hexágono regular
hexagon = [
    150, 50,  # Punto 1
    200, 90,  # Punto 2
    200, 150, # Punto 3
    150, 190, # Punto 4
    100, 150, # Punto 5
    100, 90   # Punto 6
]

# Dibujar un hexágono
canvas.create_polygon(hexagon, fill='blue', outline='yellow', width=3)

root.mainloop()