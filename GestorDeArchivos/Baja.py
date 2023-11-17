from tkinter import *
import re
import datetime
pantallaBaja = Tk()
def confibaja():
    contar = []
    if(comprobarfecha(fechaBaja.get(),"Fecha Baja")):
        contar.append(fechaBaja.get())
    
    try:
        code = codigoBaja.get()
        if(code>0):
            contar.append(code)
        else:
            texto.insert("end","Error el codigo no puede ser 0 o negativo\n")
    except TclError:
        texto.insert("end","Error en el formato de codigo\n")
def comprobarfecha(fecha,tipo):
        
        if(re.match(r"^\d{4}-\d{1,2}-\d{1,2}$", fecha)):
            try:
                 datetime.strptime(fecha,"%Y-%m-%d")
                 return True
            except ValueError:
                texto.insert("end",f"Error del año, mes o dia en {tipo}\n")
                return False
        else:
             texto.insert("end",f"Error en el formato de fecha en {tipo} debe ser aaaa-mm-dd\n")
pantallaBaja.geometry("550x300")
pantallaBaja.title("Baja Empleado")
codigoBaja = IntVar()
fechaBaja = StringVar()
Label(pantallaBaja,text="CODIGO EMPLEADO", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=0,padx=(90,30),pady=(30,0))
Label(pantallaBaja,text="FECHA BAJA", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=1,padx=(40,80),pady=(30,0))

Entry(pantallaBaja,width=25).grid(row=1,column=0,padx=(90,30))
Entry(pantallaBaja,width=25,textvariable=fechaBaja).grid(row=1,column=1,padx=(40,80))

texto = Text(pantallaBaja,height=5,width=60,font=("Microsoft Sans Serif",10, "bold"),fg="red")
texto.grid(row=2,column=0,columnspan=2,pady=(30,0))

Button(pantallaBaja,text="CONFIRMAR",command=confibaja).grid(row=3,column=0,columnspan=2,padx=30,pady=(30,0))
pantallaBaja.mainloop()
