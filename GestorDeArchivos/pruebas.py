from PIL import ImageGrab
import tkinter as tk
import img2pdf

def capture_to_pdf():
    # Captura la ventana de Tkinter
    x=root.winfo_rootx()
    y=root.winfo_rooty()
    x1=x+root.winfo_width()
    y1=y+root.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save("capture.png")

    # Convierte la imagen capturada a PDF
    with open("output.pdf", "wb") as f:
        f.write(img2pdf.convert("capture.png"))

root = tk.Tk()
button = tk.Button(root, text="Capture and Convert to PDF", command=capture_to_pdf)
button.pack()
root.mainloop()