from tkinter import *
from tkinter import font as tkFont

pantallaAlta = Tk()

pantallaAlta.geometry("1000x500")
customFont = tkFont.Font(family="Helvetica", size=9,weight="bold")

#Primera fila

Label(pantallaAlta,text="CÓDIGO",font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=0,padx=(5,0))
Label(pantallaAlta,text="APELLIDOS Y NOMBRES",font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=2,columnspan=8)
#Segunda Fila

Entry(pantallaAlta,width=15).grid(row=1,column=0,padx=(5,0))
Entry(pantallaAlta).grid(row=1,column=2,columnspan=8,sticky="ew")

#Tercera Fila
Label(pantallaAlta,text="FECHA NACIMIENTO",font=("Microsoft Sans Serif", 8, "bold")).grid(row=2,column=0,columnspan=2,padx=(15,0),pady=10)
Label(pantallaAlta,text="FECHA ALTA",font=("Microsoft Sans Serif", 8, "bold")).grid(row=2,column=3,padx=(0,30))
Label(pantallaAlta,text="DIRECCIÓN",font=("Microsoft Sans Serif", 8, "bold")).grid(row=2,column=4,columnspan=7)

#Cuarta Fila
Entry(pantallaAlta).grid(row=3,column=0,columnspan=2,padx=(15,0))
Entry(pantallaAlta).grid(row=3,column=3,padx=(0,30))
Entry(pantallaAlta).grid(row=3,column=4,columnspan=7,sticky="ew")

#QUINTA FILA
Label(pantallaAlta,text="NIF",font=("Microsoft Sans Serif", 8, "bold")).grid(row=4,column=0,padx=(30,0),pady=10)
Label(pantallaAlta,text="DATOS BANCARIOS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=4,column=3,columnspan=4)
Label(pantallaAlta,text="NÚMERO AFILICIACIÓN SS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=4,column=7,columnspan=3)

#sexta Fila
Entry(pantallaAlta).grid(row=5,column=0,padx=(30,0))
Entry(pantallaAlta).grid(row=5,column=3,columnspan=4,sticky="ew",padx=(0,20))
Entry(pantallaAlta).grid(row=5,column=7,columnspan=3,sticky="ew")
#Septima FILA
Label(pantallaAlta,text="SALARIO BRUTO",font=("Microsoft Sans Serif", 8, "bold")).grid(row=6,column=0,columnspan=2,padx=(30,0),pady=20)
Entry(pantallaAlta).grid(row=6,column=3)
Label(pantallaAlta,text="NUMERO PAGAS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=6,column=4)
Entry(pantallaAlta).grid(row=6,column=6)
#novena fila
Label(pantallaAlta,text="SALARIO MES",font=("Microsoft Sans Serif", 8, "bold")).grid(row=8,column=0,padx=(10,0),pady=20,columnspan=2)

Entry(pantallaAlta).grid(row=8,column=2,columnspan=2,sticky="ew")
Label(pantallaAlta,text="%IRPF",font=("Microsoft Sans Serif", 8, "bold")).grid(row=8,column=4,padx=(20,0))
Label(pantallaAlta,text="  ").grid(row=8,column=5)
Entry(pantallaAlta).grid(row=8,column=6,sticky="ew")
Label(pantallaAlta,text="RETENCION IRPF",font=("Microsoft Sans Serif", 8, "bold")).grid(row=8,column=7,padx=(20,0))
Label(pantallaAlta,text="     ").grid(row=8,column=8)
Entry(pantallaAlta).grid(row=8,column=9,sticky="ew")
#decima fila
Label(pantallaAlta,text="PRORRATA PAGAS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=9,column=0,padx=(10,0),columnspan=2)
Entry(pantallaAlta).grid(row=9,column=2,columnspan=2,sticky="ew")
Label(pantallaAlta,text="SEG.SOCIAL",font=("Microsoft Sans Serif", 8, "bold")).grid(row=9,column=4,padx=(20,0))
Entry(pantallaAlta).grid(row=9,column=6,sticky="ew")
Label(pantallaAlta,text="DEDUCCION SS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=9,column=7,padx=(20,0))
Entry(pantallaAlta).grid(row=9,column=9,sticky="ew")

#undecima fila
Text(pantallaAlta,height=3).grid(row=10,column=0,columnspan=7,sticky="ew",padx=(30,0),pady=15)
Label(pantallaAlta,text="CONFIRMAR",font=("Microsoft Sans Serif", 8, "bold")).grid(row=10,column=7,sticky="ew")
Entry(pantallaAlta).grid(row=10,column=8,columnspan=2,sticky="ew")


font = ("Helvetica", 10, "bold")
Button(pantallaAlta,text="CARGAR EMPLEADO",font=("Microsoft Sans Serif", 8, "bold"),relief="ridge",borderwidth=3).grid(row=11,column=0,columnspan=7)
Button(pantallaAlta,text="CALCULAR",font=("Microsoft Sans Serif", 8, "bold"),width=20,height=3,relief="ridge").grid(row=11,column=7)
Button(pantallaAlta,font=("Microsoft Sans Serif", 8, "bold")).grid(row=11,column=9)


pantallaAlta.mainloop()