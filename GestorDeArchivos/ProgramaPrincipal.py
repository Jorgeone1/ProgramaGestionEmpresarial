import tkinter as tk

root = tk.Tk()

# Entry superior con un ancho específico
entry1 = tk.Entry(root, width=20)
entry1.grid(row=0, column=0, sticky="ew", padx=(0, 0))  # Alineado a la izquierda y derecha, sin padding adicional.

# Entry inferior con un ancho mayor
entry2 = tk.Entry(root, width=30)
entry2.grid(row=1, column=0, sticky="ew", padx=(0, 0))  # Alineado a la izquierda y derecha, sin padding adicional.

# Configura la columna 0 para que se expanda y llene el espacio si la ventana cambia de tamaño
root.grid_columnconfigure(0, weight=1)

root.mainloop()