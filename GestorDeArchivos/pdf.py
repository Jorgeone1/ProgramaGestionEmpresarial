from tkinter import *

pantallaFotocopiar = Tk()

pantallaFotocopiar.geometry("800x400")

datosfotocopia = Text(pantallaFotocopiar,height=20,width=90)
datosfotocopia.grid(row=0,column=0,padx=35,pady=35)
textoFotocopia = '''
RODRIGUEZ LOPEZ, LORENZO
C/ BATALLA DEL MAR, 16
---------------------------------------------------------------------------------

NIF 14310644K        NAF 28123123412123          CCC ES19 2321 1232 89 1232134556
PERIODO: OCTUBRE     DIAS: 30    F. ALTA: 12/09/2022         F. BAJA:
---------------------------------------------------------------------------------

CONCEPTOS SALARIALES
SALARIO BASE                                                              1800,00
DESCUENTOS
BASE IMPONIBLE     1800,00           IRPF    15,00%                        270,00
BCCC               2100,00           SS 6,35%                              133,35
---------------------------------------------------------------------------------

PRORRATA DE PAGAS: 300,00                                TOTAL A PERCIBIR 1396,65
'''
datosfotocopia.insert("end",textoFotocopia)
pantallaFotocopiar.mainloop()