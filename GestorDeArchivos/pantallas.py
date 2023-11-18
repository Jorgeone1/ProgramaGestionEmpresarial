from tkinter import *
from tkinter import ttk
from datetime import *
import sqlite3 as sql
import re
import math
from tkinter import messagebox
def confirmar():
    validacionAlta.delete("1.0","end")#borra todos los elementos de validacion para volver a empezar
    contador = []
    insertarDatos="Insert into empleados(nombre,fechanacimiento,fechaalta,direccion,nif,datosbancarios,naf,genero,departamento,puesto,telefono,email,salario,pagasExtra,irpf,seguridadsocial,altas) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    if(re.match(r"^[A-Za-z]+$",nombreAlta.get().replace(" ","")) and not len(nombreAlta.get().strip())==0):
        print("nombre correcto")
        contador.append(nombreAlta.get())
    else:
        validacionAlta.insert("end","Error Nombre y Apellidos\n")
    
    if(comprobarfecha(fechanacimientoAlta.get(),"Fecha Nacimiento")):
        contador.append(fechanacimientoAlta.get())
    
    if(comprobarfecha(fechaAlta.get(),"Fecha Alta")):
        contador.append(fechaAlta.get())
    
    if(re.match(r"^[A-Za-z0-9]+$",direccionAlta.get().replace(" ",""))):
        contador.append(direccionAlta.get())
    else:
         validacionAlta.insert("end","En direccion no puede estar vacio o contener caracteres especiales\n")
    
    if(comprobarDni(nifAlta.get())):
        contador.append(nifAlta.get())
        
    if(comprobarNifIban(bancoAlta.get())):
        contador.append(bancoAlta.get())

    if(comprobarNaf(ssAlta.get())):
        contador.append(ssAlta.get())

    if(combo.get()!="-"):
        if(combo.get== "Hombre" or combo.get()== "Mujer" or combo.get()=="Otros"):
            contador.append(combo.get())
        else:
            validacionAlta.insert("end","Error tiene que seleccionar un genero de las opciones\n")
    else:
        validacionAlta.insert("end","Error tiene que seleccionar un genero\n")

    if(re.match(r"^[A-Za-z]+$",departamentoAlta.get().replace(" ",""))):
        contador.append(departamentoAlta.get())
    else:
         validacionAlta.insert("end","En departamento no puede estar vacio o contener caracteres especiales o números\n")
  
    if(re.match(r"^[A-Za-z]+$",puestoAlta.get().replace(" ",""))):
        contador.append(puestoAlta.get())
    else:
         validacionAlta.insert("end","En Puesto no puede estar vacio o contener caracteres especiales o números\n")    
    try:
        if(re.match(r"^\d{9,10}$",str(telefonoAlta.get()))):
            contador.append(telefonoAlta.get())
        else:
            validacionAlta.insert("end","En telefono tiene que ser 9 números\n")
    except TclError:
        validacionAlta.insert("end","En telefono no puede contener caracteres y tiene que ser 9 números\n")
    if(re.match(r"^[A-Za-z0-9/_.]+@[A-Za-z]+\.[A-Za-z]{2,4}",emailalta.get())):
        contador.append(emailalta.get())
    else:
        validacionAlta.insert("end","El correo tiene un formato incorrecto\n")
    try:
        salario = SaliroAlta.get()
        if(salario>0):
            contador.append(salario)
        else:
            validacionAlta.insert("end","Error no puede ser valor 0 el Salario\n")
    except TclError:
        validacionAlta.insert("end","Error en sueldo no puede contener caracteres.\n") 
        
   
    
    try:
        extra = extraAlta.get()
        contador.append(extra)
    except TclError:
        validacionAlta.insert("end","Error en Pago Extra no puede contener caracteres.\n") 
    
    try:
        irp = irpfAlta.get()
        if(irp>0):
            contador.append(irp)
        else:
            validacionAlta.insert("end","Error no puede ser valor 0 el irpf\n")
    except TclError:
        validacionAlta.insert("end","Error en IRPF no puede contener caracteres.\n") 
        
    try:
        segurida = seguridadAlta.get()
        if(segurida>0):
            contador.append(segurida)
        else:
            validacionAlta.insert("end","Error no puede ser valor 0 el Seguridad Social\n")
    except TclError:
        validacionAlta.insert("end","Error en Seguridad Social no puede contener caracteres.\n") 
        
    if(len(contador)==16):
        respuesta = messagebox.askyesno("Confirmar","¿desea confirmar?")
        if(respuesta):
            contador.append(True)
            print(insertarDatos)
            print(contador)
            conexion = sql.connect("empleado.db")
            cursor = conexion.cursor()
            cursor.execute(insertarDatos,contador)
            conexion.commit()
            validacionAlta.delete("1.0","end")
            validacionAlta.insert("end","Se ha añadido correctamente")
            limpiar()
            conexion.close()
        
        
def limpiar():
    conexion = sql.connect("empleado.db")
    cursor = conexion.cursor()
    cursor.execute("select id from empleados order by id desc limit 1")
    codigo = cursor.fetchall()
    codinuevo = codigo[0][0]
    codinuevo +=1
    codigos.set(codinuevo)
    nombreAlta.set("")
    nombreAlta.set("")
    fechanacimientoAlta.set("")
    fechaAlta.set("")
    direccionAlta.set("")
    nifAlta.set("")
    bancoAlta.set("")
    ssAlta.set("")
    departamentoAlta.set("")
    puestoAlta.set("")
    telefonoAlta.set("")
    SaliroAlta.set("")
    irpfAlta.set("")
    emailalta.set("")
    extraAlta.set("")
    seguridadAlta.set("")
def comprobarDni(dni):
    letras= "TRWAGMYFPDXBNJZSQVHLCKE" #lista en orden de los codigos
    letnum={"X":"0","Y":"1","Z":"2"} #diccionario para sustituirlas letras en el dni
    if(len(dni)==9):
        if(re.search(r"[0-9]{8}[A-Za-z]{1}",dni)):#Comprueba si el codigo que inserto el 
            numeros = int(dni[:8])-int((int(dni[:8])/23))*23
            if(dni[-1].upper()==letras[numeros]):#comprueba que la letra sea la misma que el del usuario
                print("El DNI es correcto")
                return True
            else:
                validacionAlta.insert("end","El DNI es incorrecto en su ultima letra\n")
                return False
        elif(re.search(r"^[x|X|Y|y|Z|z]{1}[0-9]{7}[A-Za-z]{1}$",dni)):#Comprueba si es un NIE
            numeros=int(letnum[dni[0].upper()]+dni[1:8])-(int(int(letnum[dni[0].upper()]+dni[1:8])/23)*23)
            if(letras[numeros]==dni[-1].upper()): #comprueba que el indice de numeros en el string de letras coincida con el dni del usuario
                print("El NIE es correcto")
                return True
            else:
                validacionAlta.insert("end","Error el NIE es incorrecto en la ultima letra\n")
                return False
        else:
            validacionAlta.insert("end","Error en el formato del DNI o NIE\n")
    else:
        validacionAlta.insert("end","Error El DNI o NIF tiene que tener una longitud de 9\n")
    

#Y9408905X
#comprobacion del naf
def comprobarNaf(naf):
    if(len(naf)==12):
        if(naf.isdigit()):
            if(int(naf[2:10])<10000000):#comprueba si los numeros del medio supera los 
                numeros=((int(naf[:1])+int(naf[2:10]))*10000000)%97
                return correctoNaf(numeros,naf[10:12])
            else:
                numeros=int((int(naf[:10]))%97)#sino realizara otro tipo de operación
                return correctoNaf(numeros,naf[10:12])
                    
        else:
            validacionAlta.insert("end","Error del formato del codigo NAF\n")
    else:
        validacionAlta.insert("end","Error de longitud del codigo NAF\n")

#comprueba que los digitos coincidan con el calculado
def correctoNaf(naf,c):
    if(str(naf)==c):
        print("codigo NAF correcto")  
        return True
    else:
        validacionAlta.insert("end","Codigo NAF equivocado en la validacion\n")
        return False

#comprueba si el codigo introducido es un iban o un ccc
def comprobarNifIban(iban):
    #Elimina los espacios posibles que hayan puesto en el ccc o iban
    iban = iban.replace(" ","")
    if(re.search("[E|e]{1}[S|s]{1}[0-9]{22}",iban)):#comprueba si es un iban
        if(comprobarIBAN(iban[4:24])):#comprueba que el ccc del interior del iban es correcto
            if(CreadorIBAN(iban[4:24])==iban.upper()):#comprueba que si las operaciones hechas son correctas y se parecen al iban
                print("El IBAN es correcto")
                return True
            else:
                validacionAlta.insert("end","El IBAN es incorrecto\n")
                return False
        else:
            validacionAlta.insert("end","Error el CCC del IBAN es incorrecto\n")
            return False
    else:
        validacionAlta.insert("end","Error en el formato del IBAN\n")
        return False

#Comprobación y operaciones del ccc
def comprobarIBAN(iban):
    entidad=iban[0:8] #Guarda los datos de la oficina y codigo de entidad
    codigocuenta=iban[10:20] #Guarda el numero de cuenta
    num1=[4,8,5,10,9,7,3,6] #Guarda las operaciones para el primer digito en orden
    num2=[1,2,4,8,5,10,9,7,3,6] #Guarda las operaciones del segundo digito en orden
    if(len(iban)==20):
        digito1=primerDigito(entidad,num1) #Realiza las operaciones del digito 1
        digito2=segundoDigito(codigocuenta,num2) #Realiza las operaciones del digito 2
        total= f"{digito1}{digito2}" #los junta
        return total==iban[8:10]   #devuelve un booleano si coinciden o no
    else:
        validacionAlta.insert("end","Error en el formato de IBAN/CCC\n")

#operaciones del primer digito
def primerDigito(entidad,num1):
    numeros=0
    for po in range(0,8): #for que realiza las operaciones
        numeros= numeros + (int(entidad[po])*num1[po])
    resto=numeros%11
    
    if(resto==1):
        return 1
    else:
        return int(11- resto)
    
#Operaciones con el segundo digito
def segundoDigito(codigocuenta,num2):
    numeros2=0
    for pi in range(0,len(num2)): # for que realiza las operaciones
        numeros2= numeros2 + (int(codigocuenta[pi])*num2[pi])
    resto2=11-(numeros2%11)
    if(resto2==10):
        return 1
    else:
        return resto2
#ES8520854882515194350922
#Crea y devuelve un IBAN pero realizando las operaciones
def CreadorIBAN(cuenta):
    total=cuenta+"142800" 
    numerosiban=98-(int(total)%97) #realiza la operación para calcular los numeros de despues del ES
    if(len(str(numerosiban))==1):
        numerosiban="0" + str(numerosiban) #Crea un iban pero con los numeros creados por las operaciones 
    iban="ES"+str(numerosiban)+cuenta
    print(iban)
    return iban
def comprobarfecha(fecha,tipo):
        
        if(re.match(r"^\d{4}-\d{1,2}-\d{1,2}$", fecha)):
            try:
                 datetime.strptime(fecha,"%Y-%m-%d")
                 return True
            except ValueError:
                validacionAlta.insert("end",f"Error del año, mes o dia en {tipo}\n")
                return False
        else:
             validacionAlta.insert("end",f"Error en el formato de fecha en {tipo} debe ser aaaa-mm-dd\n")
                 

        

pantallaAlta = Tk()
conexion = sql.connect("empleado.db")
cursor = conexion.cursor()
cursor.execute("select id from empleados order by id desc limit 1")
codigo = cursor.fetchall()

    



pantallaAlta.geometry("1000x500")
pantallaAlta.title("Alta Empleado")

codigos = IntVar()
nombreAlta = StringVar()
fechanacimientoAlta = StringVar()
fechaAlta = StringVar()
direccionAlta = StringVar()
nifAlta = StringVar()
bancoAlta = StringVar()
ssAlta = StringVar()
departamentoAlta = StringVar()
puestoAlta = StringVar()
telefonoAlta = IntVar()
SaliroAlta = DoubleVar()
irpfAlta = IntVar()
emailalta = StringVar()
extraAlta = DoubleVar()
seguridadAlta = DoubleVar()
print(len(codigo))

    
#Primera fila
Label(pantallaAlta,text="CÓDIGO",font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=0,padx=(5,0))
Label(pantallaAlta,text="APELLIDOS Y NOMBRES",font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=2,columnspan=8)

#Segunda Fila

Entry(pantallaAlta,width=15,textvariable=codigos,state="disabled").grid(row=1,column=0,padx=(5,0))
Entry(pantallaAlta,textvariable=nombreAlta).grid(row=1,column=2,columnspan=8,sticky="ew")

if(len(codigo)==0):
    codigos.set(1)
else:
    codi = (codigo[0][0])
    codi+=1 
    codigos.set(codi)
#Tercera Fila
Label(pantallaAlta,text="FECHA NACIMIENTO",font=("Microsoft Sans Serif", 8, "bold")).grid(row=2,column=0,columnspan=2,padx=(15,0),pady=10)
Label(pantallaAlta,text="FECHA ALTA",font=("Microsoft Sans Serif", 8, "bold")).grid(row=2,column=3,padx=(0,30))
Label(pantallaAlta,text="DIRECCIÓN",font=("Microsoft Sans Serif", 8, "bold")).grid(row=2,column=4,columnspan=7)

#Cuarta Fila
Entry(pantallaAlta,textvariable=fechanacimientoAlta).grid(row=3,column=0,columnspan=2,padx=(15,0))
Entry(pantallaAlta,textvariable=fechaAlta).grid(row=3,column=3,padx=(0,30))
Entry(pantallaAlta,textvariable=direccionAlta).grid(row=3,column=4,columnspan=7,sticky="ew")

#QUINTA FILA
Label(pantallaAlta,text="NIF",font=("Microsoft Sans Serif", 8, "bold")).grid(row=4,column=0,padx=(30,0),pady=10)
Label(pantallaAlta,text="DATOS BANCARIOS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=4,column=3,columnspan=4)
Label(pantallaAlta,text="NÚMERO AFILICIACIÓN SS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=4,column=7,columnspan=3)

#sexta Fila
Entry(pantallaAlta,textvariable=nifAlta).grid(row=5,column=0,padx=(30,0))
Entry(pantallaAlta,textvariable=bancoAlta).grid(row=5,column=3,columnspan=4,sticky="ew",padx=(0,20))
Entry(pantallaAlta,textvariable=ssAlta).grid(row=5,column=7,columnspan=3,sticky="ew")
#Septima FILA
Label(pantallaAlta,text="GENERO",font=("Microsoft Sans Serif", 8, "bold")).grid(row=6,column=0,padx=(30,0),pady=10)
Label(pantallaAlta,text="DEPARTAMENTO",font=("Microsoft Sans Serif", 8, "bold")).grid(row=6,column=3,columnspan=4,padx=(0,20))
Label(pantallaAlta,text="PUESTO",font=("Microsoft Sans Serif", 8, "bold")).grid(row=6,column=7,columnspan=3)

#octava Fila

combo = ttk.Combobox(pantallaAlta)
combo.grid(row=7,column=0,padx=(30,0))
combo["values"] = ("-","Hombre","Mujer","Otros")
combo.current(0)
Entry(pantallaAlta,textvariable=departamentoAlta).grid(row=7,column=3,sticky="ew",columnspan=4,padx=(0,20))
Entry(pantallaAlta,textvariable=puestoAlta).grid(row=7,column=7,sticky="ew",columnspan=3)

#novena fila
Label(pantallaAlta,text="TELÉFONO",font=("Microsoft Sans Serif", 8, "bold")).grid(row=8,column=0,padx=(10,0),pady=20,columnspan=2)

Entry(pantallaAlta,textvariable=telefonoAlta).grid(row=8,column=2,columnspan=2,sticky="ew")
Label(pantallaAlta,text="SALARIO MENSUAL",font=("Microsoft Sans Serif", 8, "bold")).grid(row=8,column=4,padx=(20,0))
Label(pantallaAlta,text="  ").grid(row=8,column=5)
Entry(pantallaAlta,textvariable=SaliroAlta).grid(row=8,column=6,sticky="ew")
Label(pantallaAlta,text="IRPF",font=("Microsoft Sans Serif", 8, "bold")).grid(row=8,column=7,padx=(20,0))
Label(pantallaAlta,text="     ").grid(row=8,column=8)
Entry(pantallaAlta,textvariable=irpfAlta).grid(row=8,column=9,sticky="ew")
#decima fila
Label(pantallaAlta,text="EMAIL",font=("Microsoft Sans Serif", 8, "bold")).grid(row=9,column=0,padx=(10,0),columnspan=2)
Entry(pantallaAlta,textvariable=emailalta).grid(row=9,column=2,columnspan=2,sticky="ew")
Label(pantallaAlta,text="PAGAS EXTRAS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=9,column=4,padx=(20,0))
Entry(pantallaAlta,textvariable=extraAlta).grid(row=9,column=6,sticky="ew")
Label(pantallaAlta,text="SEG.SOCIAL",font=("Microsoft Sans Serif", 8, "bold")).grid(row=9,column=7,padx=(20,0))
Entry(pantallaAlta,textvariable=seguridadAlta).grid(row=9,column=9,sticky="ew")

#undecima fila

validacionAlta = Text(pantallaAlta,height=5)
validacionAlta.grid(row=10,column=0,columnspan=7,sticky="ew",padx=(30,0),pady=15)
Button(pantallaAlta,text="CONFIRMAR",font=("Microsoft Sans Serif", 8, "bold"),command=confirmar).grid(row=10,column=7,columnspan=3,sticky="ew")
scroll = Scrollbar(pantallaAlta, command=validacionAlta.yview)
scroll.grid(row=10, column=7, sticky="ns",padx=(0,100))
validacionAlta.config(yscrollcommand=scroll.set)

pantallaAlta.mainloop()