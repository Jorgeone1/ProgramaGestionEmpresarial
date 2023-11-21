import tkinter as tk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def crear_pdf():
    nombre = entry_nombre.get()
    contenido = entry_contenido.get("1.0", "end-1c")

    if nombre and contenido:
        # Crear un objeto canvas para el PDF
        c = canvas.Canvas(f"{nombre}.pdf", pagesize=letter)

        # Dibujar líneas
        c.setLineWidth(1)
        c.setStrokeColor(colors.black)
        c.line(50, 750, 550, 750)  # Línea horizontal
           # Línea vertical

        # Dibujar un rectángulo
        c.rect(100, 500, 300, 200, stroke=1, fill=0)

        # Agregar texto
        c.drawString(100, 750, "PDF generado desde Tkinter")
        c.drawString(100, 730, f"Nombre: {nombre}")
        c.drawString(100, 710, "Contenido:")
        c.drawString(100, 690, contenido)

        # Guardar el PDF
        c.save()
        resultado.config(text=f"PDF '{nombre}.pdf' creado exitosamente.")
    else:
        resultado.config(text="Por favor, ingresa un nombre y contenido.")

# Crear la ventana de Tkinter
ventana = tk.Tk()
ventana.title("Generador de PDF")

# Crear etiquetas y entradas de texto
etiqueta_nombre = tk.Label(ventana, text="Nombre del PDF:")
etiqueta_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

etiqueta_contenido = tk.Label(ventana, text="Contenido:")
etiqueta_contenido.pack()
entry_contenido = tk.Text(ventana, height=10, width=40)
entry_contenido.pack()

# Botón para generar el PDF
boton_generar_pdf = tk.Button(ventana, text="Generar PDF", command=crear_pdf)
boton_generar_pdf.pack()

# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()