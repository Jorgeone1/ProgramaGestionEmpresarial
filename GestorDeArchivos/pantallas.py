from tkinter import *
from tkinter import font as tkFont
pantallaAlta = Tk()

pantallaAlta.geometry("900x400")
customFont = tkFont.Font(family="Helvetica", size=9,weight="bold")


#primera Fila
Label(pantallaAlta,text="CÓDIGO",font=customFont).grid(row=0,column=0)
Label(pantallaAlta,text="APELLIDOS Y NOMBRE").grid(row=0,column=1,columnspan=5)
#Segunda Fila
Entry(pantallaAlta,width=10).grid(row=1,column=0,pady=10)
Entry(pantallaAlta,width=100).grid(row=1,column=1,columnspan=5)
#Tercera Fila
Label(pantallaAlta,text="FECHA NAC").grid(row=2,column=0)
Label(pantallaAlta,text="FECHA ALTA").grid(row=2,column=1)
Label(pantallaAlta,text="DIRECCIÓN").grid(row=2,column=2,columnspan=4)

#Cuarta Fila
Entry(pantallaAlta,width=20).grid(row=3,column=0,sticky="ew",padx=(30,0))
Entry(pantallaAlta,width=25).grid(row=3,column=1,sticky="ew")
Entry(pantallaAlta,width=25).grid(row=3,column=2,sticky="ew",columnspan=4)
#Quinta Fila
Label(pantallaAlta,text="NIF").grid(row=4,column=0)
Label(pantallaAlta,text="DATOS BANCARIOS").grid(row=4,column=1,columnspan=3)
Label(pantallaAlta,text="NÚMERO DE AFILICIACIÓN SS").grid(row=4,column=4,columnspan=2)
#Sexta Fila
Entry(pantallaAlta).grid(row=5,column=0)
Entry(pantallaAlta,width=60).grid(row=5,column=1,columnspan=3)
Entry(pantallaAlta,width=40).grid(row=5,column=4,columnspan=2)
#Septima Fila
Label(pantallaAlta,text="GÉNERO").grid(row=6,column=0)
Label(pantallaAlta,text="DEPARTAMENTO").grid(row=6,column=1,columnspan=3)
Label(pantallaAlta,text="PUESTO").grid(row=6,column=4,columnspan=2)
#Octava Fila
Entry(pantallaAlta).grid(row=7,column=0)
Entry(pantallaAlta,width=60).grid(row=7,column=1,columnspan=3)
Entry(pantallaAlta,width=40).grid(row=7,column=4,columnspan=2)
#Novena Fila
Label(pantallaAlta,text="TELÉFONO").grid(row=8,column=0,pady=10,sticky="ew")
Entry(pantallaAlta).grid(row=8,column=1,pady=10,sticky="ew")
Label(pantallaAlta,text="SALARIO MENSUAL").grid(row=8,column=2,pady=10,sticky="ew")
Entry(pantallaAlta).grid(row=8,column=3,pady=10,sticky="ew")
Label(pantallaAlta,text="IRPF").grid(row=8,column=4,pady=10,sticky="ew")
Entry(pantallaAlta).grid(row=8,column=5,pady=10,sticky="ew")
#Decima Fila
Label(pantallaAlta,text="EMAIL").grid(row=9,column=0,pady=5)
Entry(pantallaAlta).grid(row=9,column=1,pady=5)
Label(pantallaAlta,text="PAGAS EXTRAS").grid(row=9,column=2,pady=5)
Entry(pantallaAlta).grid(row=9,column=3,pady=5)
Label(pantallaAlta,text="SEG. SOCIAL").grid(row=9,column=4,pady=5)
Entry(pantallaAlta).grid(row=9,column=5,pady=5)
#undecima y duodecima linea
Text(pantallaAlta,height=5).grid(row=10,column=0,columnspan=4,rowspan=2)
Button(pantallaAlta,text="Confirmar").grid(row=10,column=5,columnspan=2,rowspan=2)


pantallaAlta.mainloop()