from tkinter import *
import sqlite3 as sql
pantallaInforme = Tk()
pantallaInforme.geometry("550x300")


empleadoAltas = IntVar()
mujeresAltas = IntVar()
hombresAltas = IntVar()
empleadoBajas = IntVar()
mujeresBajas = IntVar()
hombresBajas = IntVar()
empleadoEdad = IntVar()
mujeresEdad = IntVar()
hombresEdad = IntVar()
empleadoRetribucion = IntVar()
mujeresRetribucion = IntVar()
hombresRetribucion = IntVar()

conexionInforme = sql.connect("empleado.db")
cursorInforme = conexionInforme.cursor()


Label(pantallaInforme,text="EMPLEADO\nALTAS", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=0,padx=(30,0),pady=(20,10))
Label(pantallaInforme,text="      ").grid(row=0,column=1)
Label(pantallaInforme,text="EMPLEADO\nBAJAS", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=2,pady=(20,10))
Label(pantallaInforme,text="                 ").grid(row=0,column=3)
Label(pantallaInforme,text="EDADES\nMEDIAS", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=4,pady=(20,10))
Label(pantallaInforme,text="                  ").grid(row=0,column=5)
Label(pantallaInforme,text="RETRIBUCION\nMEDIA", font=("Microsoft Sans Serif", 8, "bold"),fg="Blue").grid(row=0,column=6,pady=(20,10))

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=empleadoAltas).grid(row=1,column=0,rowspan=2,padx=(30,0))
cursorInforme.execute("Select count(ID) as contador from empleados where genero = 'Hombre'")
resulEmpleAlta = cursorInforme.fetchall()
for resultado in resulEmpleAlta:
    print(resultado)
Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=empleadoBajas).grid(row=1,column=2,rowspan=2)

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=empleadoEdad).grid(row=1,column=4,rowspan=2)

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=empleadoRetribucion).grid(row=1,column=6,rowspan=2)

Label(pantallaInforme,text="%MUJERES", font=("Microsoft Sans Serif", 8)).grid(row=3,column=0,padx=(30,0),pady=(20,10))
Label(pantallaInforme,text="%MUJERES", font=("Microsoft Sans Serif", 8)).grid(row=3,column=2,pady=(20,10))
Label(pantallaInforme,text="MUJERES", font=("Microsoft Sans Serif", 8)).grid(row=3,column=4,pady=(20,10))
Label(pantallaInforme,text="MUJERES", font=("Microsoft Sans Serif", 8,"bold"),fg="CornflowerBlue").grid(row=3,column=6,pady=(20,10))

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=mujeresAltas).grid(row=4,column=0,rowspan=2,padx=(30,0))
Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=mujeresBajas).grid(row=4,column=2,rowspan=2)
Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=mujeresEdad).grid(row=4,column=4,rowspan=2)
Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=mujeresRetribucion).grid(row=4,column=6,rowspan=2)

Label(pantallaInforme,text="%HOMBRES", font=("Microsoft Sans Serif", 8)).grid(row=6,column=0,padx=(30,0),pady=(20,10))
Label(pantallaInforme,text="%HOMBRES", font=("Microsoft Sans Serif", 8)).grid(row=6,column=2,pady=(20,10))
Label(pantallaInforme,text="HOMBRES", font=("Microsoft Sans Serif", 8)).grid(row=6,column=4,pady=(20,10))
Label(pantallaInforme,text="HOMBRES", font=("Microsoft Sans Serif", 8,"bold"),fg="CornflowerBlue").grid(row=6,column=6,pady=(20,10))

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=hombresAltas).grid(row=7,column=0,rowspan=2,padx=(30,0))
Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=hombresBajas).grid(row=7,column=2,rowspan=2)
Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=hombresEdad).grid(row=7,column=4,rowspan=2)
Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=hombresRetribucion).grid(row=7,column=6,rowspan=2)

pantallaInforme.mainloop()