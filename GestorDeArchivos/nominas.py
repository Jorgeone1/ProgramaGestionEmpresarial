from tkinter import *
from tkinter import font as tkFont
import sqlite3 as sql
import re
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib import colors
def capture_to_pdf():
    # Captura la ventana de Tkinter
    

    pantallaFotocopiar = Tk()
    cursorInforme.execute(f"Select nombre, direccion, nif, naf,DatosBancarios,fechaalta,fechabaja,salario from empleados where id ={codigoNomina.get()}")
    datosImprimir =cursorInforme.fetchall()
    pantallaFotocopiar.geometry("800x400")
    datosfotocopia = Text(pantallaFotocopiar,height=20,width=90)
    datosfotocopia.grid(row=0,column=0,padx=35,pady=35)
    print(datosImprimir)
    c = canvas.Canvas(f"nombre.pdf")
    c.drawString(100,750,datosImprimir[0][0])
    c.drawString(100,730,datosImprimir[0][1])
    c.setLineWidth(1)
    c.setStrokeColor(colors.black)
    c.line(50, 710, 550, 710)
    c.drawString(100,670,f"NIF {datosImprimir[0][2]}")
    c.drawString(150,670,f"NAF {datosImprimir[0][3]}")
    c.drawString(150,670,f"CCC {datosImprimir[0][4]}")
    c.save()
    textoFotocopia = f'''
    
    {datosImprimir[0][1]}
    ---------------------------------------------------------------------------------

    NIF {datosImprimir[0][2]}        NAF {datosImprimir[0][3]}          CCC {datosImprimir[0][4]}
    PERIODO: OCTUBRE     DIAS: 30    F. ALTA: {datosImprimir[0][5]}         F. BAJA:{datosImprimir[0][6]}
    ---------------------------------------------------------------------------------

    CONCEPTOS SALARIALES
    SALARIO BASE                                                               {salarioMesNomina.get()}
    DESCUENTOS
    BASE IMPONIBLE     {salarioMesNomina.get()}           IRPF {irpfNomina.get()}%                    {retencionIRPFNomina.get()}
    BCCC               {prorataNomina.get()}           SS {seguridadNomina.get()}%                    {deduccionSS.get()}
    ---------------------------------------------------------------------------------

    PRORRATA DE PAGAS: {round(prorataNomina.get()-salarioMesNomina.get(),2)}                           TOTAL A PERCIBIR {PercibirNomina.get()}
    '''
    datosfotocopia.insert("end",textoFotocopia)

    
   

def cargarEmpleado():
    textoError.delete("1.0","end")
    if(re.match(r"^[-]?[0-9]+$",codigoNomina.get())):
        cursorInforme.execute(f"Select nombre,fechanacimiento,fechaalta,direccion,nif,datosbancarios,naf,salario,irpf,seguridadsocial from empleados where id ={codigoNomina.get()} ")
        datos = cursorInforme.fetchall()
        if len(datos)!=0:
            textoError.insert("end",f"Empleado con ID {codigoNomina.get()} cargado con éxito.")
            listaVariables=[nombreNomina,fechanacimientoNomina,fechaNomina,direccionNomina,nifNomina,bancoNomina,ssNomina]
            for i in range(0,len(listaVariables)):
                listaVariables[i].set(datos[0][i])
            irpfNomina.set(datos[0][8])
            seguridadNomina.set(datos[0][9])
            numeroPaga.set(14)
            salarioTotal = int(datos[0][7])*12
            SaliroNomina.set(str(salarioTotal))
        else:
            textoError.insert("end",f"No Existe el empleado con ID {codigoNomina.get()}.")
    else:
        textoError.insert("end",f"No puede contener Caracteres.\n")
def CalcularNomina():
    salarioBruto = SaliroNomina.get()
    irpfPorcentaje = irpfNomina.get()
    seguridadsocialPorcentaje=seguridadNomina.get()
    salarioMesNomina.set(round((float(salarioBruto)/12),2))
    prorataNomina.set(round((float(salarioMesNomina.get())*float(numeroPaga.get()))/12,2))
    retencionIRPFNomina.set(round((salarioMesNomina.get()*irpfPorcentaje)/100,2))
    deduccionSS.set(round((prorataNomina.get()*seguridadsocialPorcentaje)/100,2))
    PercibirNomina.set(round(salarioMesNomina.get()-retencionIRPFNomina.get()-deduccionSS.get(),2))
conexionInforme= sql.connect("empleado.db")
cursorInforme = conexionInforme.cursor()


pantallaNomina = Tk()

pantallaNomina.geometry("1000x500")
customFont = tkFont.Font(family="Helvetica", size=9,weight="bold")

codigoNomina = StringVar()
nombreNomina = StringVar()
fechanacimientoNomina = StringVar()
fechaNomina = StringVar()
direccionNomina = StringVar()
nifNomina = StringVar()
bancoNomina = StringVar()
ssNomina = StringVar()
SaliroNomina = DoubleVar()
irpfNomina = IntVar()
extraNomina = DoubleVar()
numeroPaga = IntVar()
seguridadNomina = DoubleVar()
salarioMesNomina = DoubleVar()
prorataNomina = DoubleVar()
retencionIRPFNomina = DoubleVar()
deduccionSS = DoubleVar()
PercibirNomina = DoubleVar()
#Primera fila

Label(pantallaNomina,text="CÓDIGO",font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=0,padx=(5,0))
Label(pantallaNomina,text="APELLIDOS Y NOMBRES",font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=2,columnspan=8)
#Segunda Fila

Entry(pantallaNomina,width=15,textvariable=codigoNomina).grid(row=1,column=0,padx=(5,0))
Entry(pantallaNomina,textvariable=nombreNomina,state="disabled").grid(row=1,column=2,columnspan=8,sticky="ew")

#Tercera Fila
Label(pantallaNomina,text="FECHA NACIMIENTO",font=("Microsoft Sans Serif", 8, "bold")).grid(row=2,column=0,columnspan=2,padx=(15,0),pady=10)
Label(pantallaNomina,text="FECHA ALTA",font=("Microsoft Sans Serif", 8, "bold")).grid(row=2,column=3,padx=(0,30))
Label(pantallaNomina,text="DIRECCIÓN",font=("Microsoft Sans Serif", 8, "bold")).grid(row=2,column=4,columnspan=7)

#Cuarta Fila
Entry(pantallaNomina,textvariable=fechanacimientoNomina,state="disabled").grid(row=3,column=0,columnspan=2,padx=(15,0))
Entry(pantallaNomina,textvariable=fechaNomina,state="disabled").grid(row=3,column=3,padx=(0,30))
Entry(pantallaNomina,textvariable=direccionNomina,state="disabled").grid(row=3,column=4,columnspan=7,sticky="ew")

#QUINTA FILA
Label(pantallaNomina,text="NIF",font=("Microsoft Sans Serif", 8, "bold")).grid(row=4,column=0,padx=(30,0),pady=10)
Label(pantallaNomina,text="DATOS BANCARIOS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=4,column=3,columnspan=4)
Label(pantallaNomina,text="NÚMERO AFILICIACIÓN SS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=4,column=7,columnspan=3)

#sexta Fila
Entry(pantallaNomina,textvariable=nifNomina,state="disabled").grid(row=5,column=0,padx=(30,0))
Entry(pantallaNomina,textvariable=bancoNomina,state="disabled").grid(row=5,column=3,columnspan=4,sticky="ew",padx=(0,20))
Entry(pantallaNomina,textvariable=ssNomina,state="disabled").grid(row=5,column=7,columnspan=3,sticky="ew")
#Septima FILA
Label(pantallaNomina,text="SALARIO BRUTO",font=("Microsoft Sans Serif", 8, "bold")).grid(row=6,column=0,columnspan=2,padx=(30,0),pady=20)
Entry(pantallaNomina,textvariable=SaliroNomina,state="disabled").grid(row=6,column=3)
Label(pantallaNomina,text="NUMERO PAGAS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=6,column=4)
Entry(pantallaNomina,state="disabled",textvariable=numeroPaga).grid(row=6,column=6)
#novena fila
Label(pantallaNomina,text="SALARIO MES",font=("Microsoft Sans Serif", 8, "bold")).grid(row=8,column=0,padx=(10,0),pady=20,columnspan=2)

Entry(pantallaNomina,textvariable=salarioMesNomina).grid(row=8,column=2,columnspan=2,sticky="ew")
Label(pantallaNomina,text="%IRPF",font=("Microsoft Sans Serif", 8, "bold")).grid(row=8,column=4,padx=(20,0))
Label(pantallaNomina,text="  ").grid(row=8,column=5)
Entry(pantallaNomina,textvariable=irpfNomina,state="disabled").grid(row=8,column=6,sticky="ew")
Label(pantallaNomina,text="RETENCION IRPF",font=("Microsoft Sans Serif", 8, "bold")).grid(row=8,column=7,padx=(20,0))
Label(pantallaNomina,text="     ").grid(row=8,column=8)
Entry(pantallaNomina,textvariable=retencionIRPFNomina).grid(row=8,column=9,sticky="ew")
#decima fila
Label(pantallaNomina,text="PRORRATA PAGAS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=9,column=0,padx=(10,0),columnspan=2)
Entry(pantallaNomina,textvariable=prorataNomina).grid(row=9,column=2,columnspan=2,sticky="ew")
Label(pantallaNomina,text="SEG.SOCIAL",font=("Microsoft Sans Serif", 8, "bold")).grid(row=9,column=4,padx=(20,0))
Entry(pantallaNomina,textvariable=seguridadNomina,state="disabled").grid(row=9,column=6,sticky="ew")
Label(pantallaNomina,text="DEDUCCION SS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=9,column=7,padx=(20,0))
Entry(pantallaNomina,textvariable=deduccionSS).grid(row=9,column=9,sticky="ew")

#undecima fila
textoError = Text(pantallaNomina,height=3)
textoError.grid(row=10,column=0,columnspan=7,sticky="ew",padx=(30,0),pady=15)
Label(pantallaNomina,text="A PERCIBIR",font=("Microsoft Sans Serif", 8, "bold")).grid(row=10,column=7,sticky="ew")
Entry(pantallaNomina,textvariable=PercibirNomina).grid(row=10,column=8,columnspan=2,sticky="ew")


Button(pantallaNomina,text="CARGAR EMPLEADO",font=("Microsoft Sans Serif", 8, "bold"),relief="ridge",borderwidth=3,command=cargarEmpleado).grid(row=11,column=0,columnspan=7)
Button(pantallaNomina,text="CALCULAR",font=("Microsoft Sans Serif", 8, "bold"),width=20,height=3,relief="ridge",command=CalcularNomina).grid(row=11,column=7)
Button(pantallaNomina,text="CONFIRMAR",font=("Microsoft Sans Serif", 8, "bold"),command=capture_to_pdf).grid(row=11,column=9)


pantallaNomina.mainloop()