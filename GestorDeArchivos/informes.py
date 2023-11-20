from tkinter import *
import sqlite3 as sql
from datetime import *

def calcularEdad(fecha):
    fecha_actual = datetime.now()
    edadTotal=0
    for fechas in fecha:
        fecha_objeto = datetime.strptime(fechas[0], "%Y-%m-%d")
        edad=int(fecha_actual.year) - int(fecha_objeto.year)
        if(fecha_objeto.month,fecha_objeto.day) <(fecha_actual.month,fecha_actual.day):
            edad -=1
        edadTotal+=edad
    return edadTotal
def sumaSalario(salario):
    totalSalario = 0
    for salarios in salario:
        totalSalario+=float(salarios[0])
    return totalSalario
pantallaInforme = Tk()
pantallaInforme.geometry("550x300")


empleadoAltas = StringVar()
mujeresAltas = StringVar()
hombresAltas = StringVar()
empleadoBajas = StringVar()
mujeresBajas = StringVar()
hombresBajas = StringVar()
empleadoEdad = StringVar()
mujeresEdad = StringVar()
hombresEdad = StringVar()
empleadoRetribucion = StringVar()
mujeresRetribucion = StringVar()
hombresRetribucion = StringVar()

conexionInforme = sql.connect("empleado.db")
cursorInforme = conexionInforme.cursor()


Label(pantallaInforme,text="EMPLEADO\nALTAS", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=0,padx=(30,0),pady=(20,10))
Label(pantallaInforme,text="      ").grid(row=0,column=1)
Label(pantallaInforme,text="EMPLEADO\nBAJAS", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=2,pady=(20,10))
Label(pantallaInforme,text="                 ").grid(row=0,column=3)
Label(pantallaInforme,text="EDADES\nMEDIAS", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=4,pady=(20,10))
Label(pantallaInforme,text="                  ").grid(row=0,column=5)
Label(pantallaInforme,text="RETRIBUCION\nMEDIA", font=("Microsoft Sans Serif", 8, "bold"),fg="Blue").grid(row=0,column=6,pady=(20,10))

cursorInforme.execute("Select count(ID) as contador from empleados")
resulTotalEmple = cursorInforme.fetchall()

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=empleadoAltas).grid(row=1,column=0,rowspan=2,padx=(30,0))
cursorInforme.execute("Select count(ID) as contador from empleados where Altas = True")
resulEmpleAlta = cursorInforme.fetchall()

imprimirEmpleadoAlta=round(int(resulEmpleAlta[0][0])/int(resulTotalEmple[0][0])*100,2)
empleadoAltas.set(str(imprimirEmpleadoAlta)+"%")

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=empleadoBajas).grid(row=1,column=2,rowspan=2)
cursorInforme.execute("Select count(ID) as contador from empleados where Altas = False")
resulEmpleBaja = cursorInforme.fetchall()
imprimirEmpleadoBaja=round(int(resulEmpleBaja[0][0])/int(resulTotalEmple[0][0])*100,2)
empleadoBajas.set(str(imprimirEmpleadoBaja)+"%")

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=empleadoEdad).grid(row=1,column=4,rowspan=2)
cursorInforme.execute("SELECT FechaNacimiento FROM empleados")
resulEmpleEdad=cursorInforme.fetchall()
edadSumaEmple = calcularEdad(resulEmpleEdad)
imprimirEmpleadoEdad=round(edadSumaEmple/int(resulTotalEmple[0][0]))
empleadoEdad.set(str(imprimirEmpleadoEdad) + " años")

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=empleadoRetribucion).grid(row=1,column=6,rowspan=2)
cursorInforme.execute("SELECT salario FROM empleados")
resulEmpleRetri=cursorInforme.fetchall()
salarioEmpleTotal = sumaSalario(resulEmpleRetri)
imprimirEmpleadoretri=round(salarioEmpleTotal/int(resulTotalEmple[0][0]))
empleadoRetribucion.set(str(imprimirEmpleadoretri) + "€")

Label(pantallaInforme,text="%MUJERES", font=("Microsoft Sans Serif", 8)).grid(row=3,column=0,padx=(30,0),pady=(20,10))
Label(pantallaInforme,text="%MUJERES", font=("Microsoft Sans Serif", 8)).grid(row=3,column=2,pady=(20,10))
Label(pantallaInforme,text="MUJERES", font=("Microsoft Sans Serif", 8)).grid(row=3,column=4,pady=(20,10))
Label(pantallaInforme,text="MUJERES", font=("Microsoft Sans Serif", 8,"bold"),fg="CornflowerBlue").grid(row=3,column=6,pady=(20,10))

cursorInforme.execute("Select count(ID) as contador from empleados where genero = 'Mujer'")
resulTotalMujer = cursorInforme.fetchall()

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=mujeresAltas).grid(row=4,column=0,rowspan=2,padx=(30,0))
cursorInforme.execute("Select count(ID) as contador from empleados where Altas = True and genero = 'Mujer'")
resulMujerAlta = cursorInforme.fetchall()
imprimirMujerAlta=round(int(resulMujerAlta[0][0])/int(resulTotalMujer[0][0])*100,2)
mujeresAltas.set(str(imprimirMujerAlta)+"%")

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=mujeresBajas).grid(row=4,column=2,rowspan=2)
cursorInforme.execute("Select count(ID) as contador from empleados where Altas = False and genero = 'Mujer'")
resulMujerBaja = cursorInforme.fetchall()
imprimirMujerBaja=round(int(resulMujerBaja[0][0])/int(resulTotalMujer[0][0])*100,2)
mujeresBajas.set(str(imprimirMujerBaja)+"%")

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=mujeresEdad).grid(row=4,column=4,rowspan=2)
cursorInforme.execute("SELECT FechaNacimiento FROM empleados where genero = 'Mujer'")
resulMujerEdad=cursorInforme.fetchall()
edadSumaMujer = calcularEdad(resulMujerEdad)
imprimirMujerEdad=round(edadSumaMujer/int(resulTotalMujer[0][0]))
mujeresEdad.set(str(imprimirMujerEdad) + " años")

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=mujeresRetribucion).grid(row=4,column=6,rowspan=2)
cursorInforme.execute("SELECT salario FROM empleados where genero = 'Mujer'")
resulMujerRetri=cursorInforme.fetchall()
salarioMujerTotal = sumaSalario(resulMujerRetri)
imprimirMujerretri=round(salarioMujerTotal/int(resulTotalMujer[0][0]))
mujeresRetribucion.set(str(imprimirMujerretri) + "€")

Label(pantallaInforme,text="%HOMBRES", font=("Microsoft Sans Serif", 8)).grid(row=6,column=0,padx=(30,0),pady=(20,10))
Label(pantallaInforme,text="%HOMBRES", font=("Microsoft Sans Serif", 8)).grid(row=6,column=2,pady=(20,10))
Label(pantallaInforme,text="HOMBRES", font=("Microsoft Sans Serif", 8)).grid(row=6,column=4,pady=(20,10))
Label(pantallaInforme,text="HOMBRES", font=("Microsoft Sans Serif", 8,"bold"),fg="CornflowerBlue").grid(row=6,column=6,pady=(20,10))

cursorInforme.execute("Select count(ID) as contador from empleados where genero = 'Hombre'")
resulTotalHombre = cursorInforme.fetchall()

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=hombresAltas).grid(row=7,column=0,rowspan=2,padx=(30,0))
cursorInforme.execute("Select count(ID) as contador from empleados where Altas = True and genero = 'Hombre'")
resulHombreAlta = cursorInforme.fetchall()
imprimirHombreAlta=round(int(resulHombreAlta[0][0])/int(resulTotalHombre[0][0])*100,2)
hombresAltas.set(str(imprimirHombreAlta)+"%")

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=hombresBajas).grid(row=7,column=2,rowspan=2)
cursorInforme.execute("Select count(ID) as contador from empleados where Altas = False and genero = 'Hombre'")
resulHombreBaja = cursorInforme.fetchall()
imprimirHombreBaja=round(int(resulHombreBaja[0][0])/int(resulTotalHombre[0][0])*100,2)
hombresBajas.set(str(imprimirHombreBaja)+"%")

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=hombresEdad).grid(row=7,column=4,rowspan=2)
cursorInforme.execute("SELECT FechaNacimiento FROM empleados where genero = 'Hombre'")
resulHombreEdad=cursorInforme.fetchall()
edadSumaHombre = calcularEdad(resulHombreEdad)
imprimirHombreEdad=round(edadSumaHombre/float(resulTotalHombre[0][0]),2)
hombresEdad.set(str(imprimirHombreEdad) + " años")

Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=hombresRetribucion).grid(row=7,column=6,rowspan=2)
cursorInforme.execute("SELECT salario FROM empleados where genero = 'Hombre'")
resulHombreRetri=cursorInforme.fetchall()
salarioHombreTotal = sumaSalario(resulHombreRetri)
imprimirHombreretri=round(salarioHombreTotal/float(resulTotalHombre[0][0]),2)
hombresRetribucion.set(str(imprimirHombreretri) + "€")

conexionInforme.close()
pantallaInforme.mainloop()