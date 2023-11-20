from tkinter import *
import re
from datetime import *
import sqlite3
from tkinter import messagebox
pantallaBaja = Tk()
def confibaja():
    contar = []
    texto.delete("1.0","end")
    cursorbaja.execute(f"Select fechaAlta from empleados where ID = {code}")
    fechaAltita = cursorbaja.fetchall()
    fechaAlto = datetime.strptime(fechaAltita[0][0],"%Y-%m-%d")
    
    if(comprobarfecha(fechaBaja.get(),"Fecha Baja")):
        contar.append(fechaBaja.get())
        if(fechaAlto>datetime.strptime(fechaBaja.get(),"%Y-%m-%d")):
            texto.insert("end",f"No se pudo actualizar el empleado con ID {contar[1]}.")
    try:
        code = codigoBaja.get()
        if(code>0):
            contar.append(code)
        else:
            texto.insert("end","Error el codigo no puede ser 0 o negativo\n")
    except TclError:
        texto.insert("end","Error en el formato de codigo\n")
    print(contar)
    if(len(contar)==2):
        respuesta= messagebox.askyesno("Confirmar","¿Desea confirmar la operacion?")
        if respuesta:
            bajaactu = "UPDATE Empleados SET Altas = FALSE, fechaBaja = ? WHERE ID = ?"
            conectarBaja = sqlite3.connect("empleado.db")
            cursorbaja = conectarBaja.cursor()
            cursorbaja.execute(bajaactu,contar)
            
            if cursorbaja.rowcount > 0:
                texto.insert("end",f"Empleado con ID {contar[1]} actualizado con éxito.")
                conectarBaja.commit()
                limpiezabaja()
            else:
                texto.insert("end",f"No se pudo actualizar el empleado con ID {contar[1]}.")

def limpiezabaja():
    codigoBaja.set("")
    fechaBaja.set("")
        
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

Entry(pantallaBaja,width=25,textvariable=codigoBaja).grid(row=1,column=0,padx=(90,30))
Entry(pantallaBaja,width=25,textvariable=fechaBaja).grid(row=1,column=1,padx=(40,80))

texto = Text(pantallaBaja,height=5,width=60,font=("Microsoft Sans Serif",10, "bold"),fg="red")
texto.grid(row=2,column=0,columnspan=2,pady=(30,0))

Button(pantallaBaja,text="CONFIRMAR",command=confibaja).grid(row=3,column=0,columnspan=2,padx=30,pady=(30,0))
pantallaBaja.mainloop()
