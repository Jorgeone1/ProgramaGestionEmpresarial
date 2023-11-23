from tkinter import *
import sqlite3 as sql
from tkinter import ttk
from datetime import *
import sqlite3 as sql
import re
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from tkinter import filedialog
import shutil
def abrirAltas():
    def confirmar():
        validacionAlta.delete("1.0","end")#borra todos los elementos de validacion para volver a empezar
        contador = []
        fechaActual = datetime.now()
        insertarDatos="Insert into empleados(nombre,fechanacimiento,fechaalta,direccion,nif,datosbancarios,naf,genero,departamento,puesto,telefono,email,salario,pagasExtra,irpf,seguridadsocial,altas) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        if(re.match(r"^[A-Za-z]+$",nombreAlta.get().replace(" ","")) and not len(nombreAlta.get().strip())==0):
            contador.append(nombreAlta.get())
        else:
            validacionAlta.insert("end","Error Nombre y Apellidos no puede contener numeros o caracteres\n")
        
        if(comprobarfecha(fechanacimientoAlta.get(),"Fecha Nacimiento")):
            if(datetime.strptime(fechanacimientoAlta.get(),"%Y-%m-%d")>datetime.strptime("1900-01-01","%Y-%m-%d") and (datetime.strptime(fechanacimientoAlta.get(),"%Y-%m-%d")< fechaActual)):
                contador.append(fechanacimientoAlta.get())
            else:
                validacionAlta.insert("end",f"Error, la fecha Nacimineto no puede estar fuera del rango[1900-01-01-{fechaActual.year}-{fechaActual.month}-{fechaActual.day}]\n")
        if(comprobarfecha(fechaAlta.get(),"Fecha Alta")):
            if(datetime.strptime(fechaAlta.get(),"%Y-%m-%d")>datetime.strptime(fechanacimientoAlta.get(),"%Y-%m-%d")):
                if(datetime.strptime(fechaAlta.get(),"%Y-%m-%d")>datetime.strptime("1900-01-01","%Y-%m-%d") and datetime.strptime(fechaAlta.get(),"%Y-%m-%d")<fechaActual):   
                    if(calcularEdad(fechaAlta.get(),fechanacimientoAlta.get())>=18):
                        contador.append(fechaAlta.get())
                    else:
                        validacionAlta.insert("end","Error, tiene que ser mayor de 18 años\n")
                else:
                    validacionAlta.insert("end",f"Error, la fecha alta no puede estar fuera del rango[1900-01-01-{fechaActual.year}-{fechaActual.month}-{fechaActual.day}]\n")   
            else:
                validacionAlta.insert("end","Error, la fecha alta no puede ser menor que la fecha de nacimiento\n")
        if(re.match(r"^[A-Za-z0-9/ªº]+$",direccionAlta.get().replace(" ",""))):
            contador.append(direccionAlta.get())
        else:
            validacionAlta.insert("end","En direccion no puede estar vacio o contener caracteres especiales menos /ªº\n")
        
        if(comprobarDni(nifAlta.get())):
            contador.append(nifAlta.get())
            
        if(comprobarNifIban(bancoAlta.get())):
            contador.append(bancoAlta.get())

        if(comprobarNaf(ssAlta.get())):
            contador.append(ssAlta.get())

        if(combo.get()!="-"):
            if(combo.get()== "Hombre" or combo.get()== "Mujer" ):
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
            if(extra==12 or extra==13 or extra==14):
                contador.append(extra)
            else:
                validacionAlta.insert("end","Pagas extras Solo puede ser un rango[12-14].\n") 
        except TclError:
            validacionAlta.insert("end","Error en Pago Extra no puede contener caracteres.\n") 
        
        try:
            irp = irpfAlta.get()
            if(irp>0 and irp<=47):
                contador.append(irp)
            else:
                validacionAlta.insert("end","Error no puede ser valor 0 el irpf o superior a 47\n")
        except TclError:
            validacionAlta.insert("end","Error en IRPF no puede contener caracteres.\n") 
            
        try:
            segurida = seguridadAlta.get()
            if(segurida>0 and segurida<=47):
                contador.append(segurida)
            else:
                validacionAlta.insert("end","Error no puede ser valor 0 el Seguridad Social o superior a 47\n")
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
            
    def calcularEdad(fecha,fechanacimiento):
        fecha_actual = datetime.strptime(fecha,"%Y-%m-%d")
        fecha_objeto = datetime.strptime(fechanacimiento, "%Y-%m-%d")
        edad=int(fecha_actual.year) - int(fecha_objeto.year)
        if(fecha_objeto.month,fecha_objeto.day) >(fecha_actual.month,fecha_actual.day):
            edad -=1
            
        return edad
        
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
                    

            

    pantallaAlta = Toplevel()
    conexion = sql.connect("empleado.db")
    cursor = conexion.cursor()
    cursor.execute("select id from empleados order by id desc limit 1")
    codigo = cursor.fetchall()
    pantallaAlta.resizable(0,0)
        



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
    extraAlta = IntVar()
    seguridadAlta = DoubleVar()

        
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
    combo["values"] = ("-","Hombre","Mujer")
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
    combo2 =ttk.Combobox(pantallaAlta,textvariable=extraAlta)
    combo2.grid(row=9,column=6,sticky="ew")
    combo2["values"]=(12,13,14)
    combo2.current(0)
    Label(pantallaAlta,text="SEG.SOCIAL",font=("Microsoft Sans Serif", 8, "bold")).grid(row=9,column=7,padx=(20,0))
    Entry(pantallaAlta,textvariable=seguridadAlta).grid(row=9,column=9,sticky="ew")

    #undecima fila

    validacionAlta = Text(pantallaAlta,height=5)
    validacionAlta.grid(row=10,column=0,columnspan=7,sticky="ew",padx=(30,0),pady=15)
    Button(pantallaAlta,text="CONFIRMAR",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),command=confirmar).grid(row=10,column=7,columnspan=3,sticky="ew")
    scroll = Scrollbar(pantallaAlta, command=validacionAlta.yview)
    scroll.grid(row=10, column=7, sticky="ns",padx=(0,100))
    validacionAlta.config(yscrollcommand=scroll.set)
    
    
def abrirBajasVentana():
    pantallaBaja = Toplevel()
    pantallaBaja.resizable(0,0)
    def confibaja():
        contar = []
        texto.delete("1.0","end")
        if(re.match(r"^[-]?[0-9]+$",codigoBaja.get())):
            conectarBaja = sql.connect("empleado.db")
            cursorbaja = conectarBaja.cursor()
            cursorbaja.execute(f"Select fechaAlta from empleados where ID = {codigoBaja.get()}")
            fechaAltita = cursorbaja.fetchall()
            cursorbaja.execute(f"Select Altas from empleados where ID = {codigoBaja.get()}")
            bajacodigoViejo = cursorbaja.fetchall()
            if(len(bajacodigoViejo)==1):
                if(bajacodigoViejo[0][0]==1):
                    try:
                        fechaAlto = datetime.strptime(fechaAltita[0][0],"%Y-%m-%d")
                        if(comprobarfecha(fechaBaja.get(),"Fecha Baja")):
                            if(fechaAlto<datetime.strptime(fechaBaja.get(),"%Y-%m-%d")):
                                contar.append(fechaBaja.get())
                                contar.append(codigoBaja.get())
                            else:
                                texto.insert("end",f"La fecha baja no puede ser menor al que alta {fechaAlto.year}-{fechaAlto.month}-{fechaAlto.day}.\n")
                    except IndexError:
                        texto.insert("end",f"Esta vacio Fecha Baja\n")

                    if(len(contar)==2):
                        respuesta= messagebox.askyesno("Confirmar","¿Desea confirmar la operacion?")
                        if respuesta:
                            bajaactu = "UPDATE Empleados SET Altas = FALSE, fechaBaja = ? WHERE ID = ?"
                            
                            cursorbaja.execute(bajaactu,contar)
                            
                            if cursorbaja.rowcount > 0:
                                texto.insert("end",f"Empleado con ID {contar[1]} actualizado con éxito.")
                                conectarBaja.commit()
                                limpiezabaja()
                            else:
                                texto.insert("end",f"No se pudo actualizar el empleado con ID {contar[1]}.\n")
                else:
                    texto.insert("end",f"El codigo {codigoBaja.get()} ya esta dado de baja.\n")
            else:
                texto.insert("end",f"Error no existe empleado con id {codigoBaja.get()}.\n")
        else:
            texto.insert("end",f"Error no puede haber caracteres en codigo\n.")

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
    codigoBaja = StringVar()
    fechaBaja = StringVar()
    Label(pantallaBaja,text="CODIGO EMPLEADO", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=0,padx=(90,30),pady=(30,0))
    Label(pantallaBaja,text="FECHA BAJA", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=1,padx=(40,80),pady=(30,0))

    Entry(pantallaBaja,width=25,textvariable=codigoBaja).grid(row=1,column=0,padx=(90,30))
    Entry(pantallaBaja,width=25,textvariable=fechaBaja).grid(row=1,column=1,padx=(40,80))

    texto = Text(pantallaBaja,height=5,width=60,font=("Microsoft Sans Serif",10, "bold"),fg="red")
    texto.grid(row=2,column=0,columnspan=2,pady=(30,0))

    Button(pantallaBaja,text="CONFIRMAR",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),width=30,command=confibaja).grid(row=3,column=0,columnspan=2,padx=30,pady=(30,0))
    
def abrirInformeVentana():
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
    pantallaInforme = Toplevel()
    pantallaInforme.geometry("550x300")
    pantallaInforme.title("Informes")
    pantallaInforme.resizable(0,0)
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
    if (resulEmpleAlta[0][0])>0:
        imprimirEmpleadoAlta=round(int(resulEmpleAlta[0][0])/int(resulTotalEmple[0][0])*100,2)
        empleadoAltas.set(str(imprimirEmpleadoAlta)+"%")

    Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=empleadoBajas).grid(row=1,column=2,rowspan=2)
    cursorInforme.execute("Select count(ID) as contador from empleados where Altas = False")
    resulEmpleBaja = cursorInforme.fetchall()
    if (resulEmpleBaja[0][0])>0:
        imprimirEmpleadoBaja=round(int(resulEmpleBaja[0][0])/int(resulTotalEmple[0][0])*100,2)
        empleadoBajas.set(str(imprimirEmpleadoBaja)+"%")

    Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=empleadoEdad).grid(row=1,column=4,rowspan=2)
    cursorInforme.execute("SELECT FechaNacimiento FROM empleados")
    resulEmpleEdad=cursorInforme.fetchall()
    if len(resulEmpleEdad)>0:
        edadSumaEmple = calcularEdad(resulEmpleEdad)
        imprimirEmpleadoEdad=round(edadSumaEmple/int(resulTotalEmple[0][0]))
        empleadoEdad.set(str(imprimirEmpleadoEdad) + " años")

    Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=empleadoRetribucion).grid(row=1,column=6,rowspan=2)
    cursorInforme.execute("SELECT salario FROM empleados")
    resulEmpleRetri=cursorInforme.fetchall()
    if len(resulEmpleRetri)>0:
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
    if (resulMujerAlta[0][0])>0:
        imprimirMujerAlta=round(int(resulMujerAlta[0][0])/int(resulTotalMujer[0][0])*100,2)
        mujeresAltas.set(str(imprimirMujerAlta)+"%")

    Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=mujeresBajas).grid(row=4,column=2,rowspan=2)
    cursorInforme.execute("Select count(ID) as contador from empleados where Altas = False and genero = 'Mujer'")
    resulMujerBaja = cursorInforme.fetchall()
    if (resulMujerBaja[0][0])>0:
        imprimirMujerBaja=round(int(resulMujerBaja[0][0])/int(resulTotalMujer[0][0])*100,2)
        mujeresBajas.set(str(imprimirMujerBaja)+"%")

    Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=mujeresEdad).grid(row=4,column=4,rowspan=2)
    cursorInforme.execute("SELECT FechaNacimiento FROM empleados where genero = 'Mujer'")
    resulMujerEdad=cursorInforme.fetchall()
    if len(resulMujerEdad)>0:
        edadSumaMujer = calcularEdad(resulMujerEdad)
        imprimirMujerEdad=round(edadSumaMujer/int(resulTotalMujer[0][0]))
        mujeresEdad.set(str(imprimirMujerEdad) + " años")

    Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=mujeresRetribucion).grid(row=4,column=6,rowspan=2)
    cursorInforme.execute("SELECT salario FROM empleados where genero = 'Mujer'")
    resulMujerRetri=cursorInforme.fetchall()
    if len(resulMujerRetri)>0:
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
    if (resulHombreAlta[0][0])>0:
        imprimirHombreAlta=round(int(resulHombreAlta[0][0])/int(resulTotalHombre[0][0])*100,2)
        hombresAltas.set(str(imprimirHombreAlta)+"%")

    Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=hombresBajas).grid(row=7,column=2,rowspan=2)
    cursorInforme.execute("Select count(ID) as contador from empleados where Altas = False and genero = 'Hombre'")
    resulHombreBaja = cursorInforme.fetchall()
    if (resulHombreBaja[0][0])>0:
        imprimirHombreBaja=round(int(resulHombreBaja[0][0])/int(resulTotalHombre[0][0])*100,2)
        hombresBajas.set(str(imprimirHombreBaja)+"%")

    Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=hombresEdad).grid(row=7,column=4,rowspan=2)
    cursorInforme.execute("SELECT FechaNacimiento FROM empleados where genero = 'Hombre'")
    resulHombreEdad=cursorInforme.fetchall()
    if len(resulHombreEdad)>0:
        edadSumaHombre = calcularEdad(resulHombreEdad)
        imprimirHombreEdad=round(edadSumaHombre/float(resulTotalHombre[0][0]),2)
        hombresEdad.set(str(imprimirHombreEdad) + " años")

    Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=hombresRetribucion).grid(row=7,column=6,rowspan=2)
    cursorInforme.execute("SELECT salario FROM empleados where genero = 'Hombre'")
    resulHombreRetri=cursorInforme.fetchall()
    if len(resulHombreRetri)>0:
        salarioHombreTotal = sumaSalario(resulHombreRetri)
        imprimirHombreretri=round(salarioHombreTotal/float(resulTotalHombre[0][0]),2)
        hombresRetribucion.set(str(imprimirHombreretri) + "€")

    conexionInforme.close()


def abrirNominaVentana():
    def capture_to_pdf():
        # Captura la ventana de Tkinter
        conexionInforme= sql.connect("empleado.db")
        cursorInforme = conexionInforme.cursor()
        fecha_actual = datetime.now()
        cursorInforme.execute(f"Select nombre, direccion, nif, naf,DatosBancarios,fechaalta,fechabaja,salario from empleados where id ={codigoNomina.get()}")
        datosImprimir =cursorInforme.fetchall()
        diasmese={1:"ENERO",2:"FEBRERO",3:"MARZO",4:"ABRIL",5:"MAYO",6:"JUNIO",7:"JULIO",8:"AGOSTO",9:"SEPTIEMBRE",10:"OCTUBRE",11:"NOVIEMBRE",12:"DICIEMBRE"}
        mesescantidad={"ENERO":31,"FEBRERO":28,"MARZO":31,"ABRIL":30,"MAYO":31,"JUNIO":30,"JULIO":31,"AGOSTO":31,"SEPTIEMBRE":30,"OCTUBRE":30,"NOVIEMBRE":30,"DICIEMBRE":31}
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")],initialfile=f"{nombreNomina.get().replace(" ","-")}_Nomina.pdf")
        if file_path:
            c = canvas.Canvas(f"{nombreNomina.get().replace(" ","-")}_Nomina.pdf")
            c.setFont("Helvetica-Bold",11)
            c.drawString(75,750,datosImprimir[0][0])
            c.drawString(75,730,datosImprimir[0][1])
            c.setLineWidth(1)
            c.setStrokeColor(colors.black)
            c.line(75, 710, 550, 710)
            c.setFont("Helvetica",9)
            c.setFont("Helvetica-Bold",9)
            c.drawString(75,670,f"NIF:")
            c.setFont("Helvetica",9)
            c.drawString(105,670,f"{datosImprimir[0][2]}")
            c.setFont("Helvetica-Bold",9)
            c.drawString(250,670,f"NAF:")
            c.setFont("Helvetica",9)
            c.drawString(270,670,f"{datosImprimir[0][3]}")
            c.setFont("Helvetica-Bold",9)
            c.drawString(380,670,f"CCC:")
            c.setFont("Helvetica",9)
            c.drawString(430,670,f"{datosImprimir[0][4]}")
            c.setFont("Helvetica-Bold",9)
            c.drawString(75,640,f"PERIODO:")
            c.setFont("Helvetica",11)
            c.drawString(125,640,f"{diasmese[fecha_actual.month]}")
            c.setFont("Helvetica-Bold",9)
            c.drawString(230,640,f"DIAS:")
            c.setFont("Helvetica",11)
            c.drawString(260,640,f"{mesescantidad[diasmese[fecha_actual.month]]}")
            c.setFont("Helvetica-Bold",9)
            c.drawString(300,640,f"F.ALTA:")
            c.setFont("Helvetica",11)
            c.drawString(340,640,f"{datosImprimir[0][5]}")
            c.setFont("Helvetica-Bold",9)
            c.drawString(430,640,f"F.BAJA:")
            c.setFont("Helvetica",9)
            c.drawString(470,640,f"{datosImprimir[0][6]}")
            c.setFont("Helvetica-Bold",9)
            c.line(75, 610, 550, 610)
            c.drawString(75,580,f"CONCEPTOS SALARIALES")
            c.drawString(75,550,f"SALARIO BASE")
            c.setFont("Helvetica",9)
            c.drawString(470,550,f"{salarioMesNomina.get()}")
            c.setFont("Helvetica-Bold",9)
            c.drawString(75,520,f"DESCUENTOS")
            c.drawString(75,490,f"BASE IMPONIBLE")
            c.setFont("Helvetica",9)
            c.drawString(200,490,f"{salarioMesNomina.get()}")
            c.setFont("Helvetica-Bold",9)
            c.drawString(300,490,f"IRPF:")
            c.setFont("Helvetica",9)
            c.drawString(330,490,f"{irpfNomina.get()}%")
            c.drawString(470,490,f"{retencionIRPFNomina.get()}")
            c.setFont("Helvetica-Bold",9)
            c.drawString(75,460,f"BBCC:")
            c.setFont("Helvetica",9)
            c.drawString(200,460,f"{prorataNomina.get()}")
            c.setFont("Helvetica-Bold",9)
            c.drawString(300,460,f"SS:")
            c.setFont("Helvetica",9)
            c.drawString(330,460,f"{seguridadNomina.get()}%")
            c.drawString(470,460,f"{deduccionSS.get()}")
            c.line(75, 430, 550, 430)
            c.setFont("Helvetica-Bold",9)
            c.drawString(75,400,f"PRORRATA DE PAGAS: ")
            c.setFont("Helvetica",9)
            c.drawString(200,400,f"{round(prorataNomina.get()-salarioMesNomina.get(),2)}")
            c.setFont("Helvetica-Bold",9)
            c.drawString(350,400,f"TOTAL A PERCIBIR: ")
            c.setFont("Helvetica",9)
            c.drawString(470,400,f"{PercibirNomina.get()}")
            
            c.save()
            shutil.move(f"{nombreNomina.get().replace(" ","-")}_Nomina.pdf", file_path)
        conexionInforme.close()
        
    

    def cargarEmpleado():
        conexionInforme= sql.connect("empleado.db")
        cursorInforme = conexionInforme.cursor()
        textoError.delete("1.0","end")
        if(re.match(r"^[-]?[0-9]+$",codigoNomina.get())):
            cursorInforme.execute(f"Select nombre,fechanacimiento,fechaalta,direccion,nif,datosbancarios,naf,salario,irpf,seguridadsocial,pagasExtra from empleados where id ={codigoNomina.get()} ")
            datos = cursorInforme.fetchall()
            if len(datos)!=0:
                textoError.insert("end",f"Empleado con ID {codigoNomina.get()} cargado con éxito.")
                listaVariables=[nombreNomina,fechanacimientoNomina,fechaNomina,direccionNomina,nifNomina,bancoNomina,ssNomina]
                for i in range(0,len(listaVariables)):
                    listaVariables[i].set(datos[0][i])
                irpfNomina.set(datos[0][8])
                seguridadNomina.set(datos[0][9])
                numeroPaga.set(datos[0][10])
                salarioTotal = int(datos[0][7])*12
                SaliroNomina.set(str(salarioTotal))
            else:
                textoError.insert("end",f"No Existe el empleado con ID {codigoNomina.get()}.")
        else:
            textoError.insert("end",f"No puede contener Caracteres.\n")
        conexionInforme.close()
    def CalcularNomina():
        salarioBruto = SaliroNomina.get()
        irpfPorcentaje = irpfNomina.get()
        seguridadsocialPorcentaje=seguridadNomina.get()
        salarioMesNomina.set(round((float(salarioBruto)/12),2))
        prorataNomina.set(round((float(salarioMesNomina.get())*float(numeroPaga.get()))/12,2))
        retencionIRPFNomina.set(round((salarioMesNomina.get()*irpfPorcentaje)/100,2))
        deduccionSS.set(round((prorataNomina.get()*seguridadsocialPorcentaje)/100,2))
        PercibirNomina.set(round(salarioMesNomina.get()-retencionIRPFNomina.get()-deduccionSS.get(),2))



    pantallaNomina = Toplevel()
    pantallaNomina.resizable(0,0)
    pantallaNomina.geometry("1000x500")

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


    Button(pantallaNomina,text="CARGAR EMPLEADO",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),command=cargarEmpleado).grid(row=11,column=0,columnspan=7)
    Button(pantallaNomina,text="CALCULAR",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),command=CalcularNomina).grid(row=11,column=7)
    Button(pantallaNomina,text="CONFIRMAR",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),command=capture_to_pdf).grid(row=11,column=9)



    
    
conexion = sql.connect("empleado.db")
cursor = conexion.cursor()
tabla = '''CREATE TABLE IF NOT EXISTS Empleados (
    ID INTEGER primary key autoincrement,
    Nombre VARCHAR(50) not null,
    fechaNacimiento Date not null,
    FechaAlta DATE not null,
    Direccion varchar(150) not null,
    NIF varchar(9) not null,
    DatosBancarios varchar(24) not null,
    NAF varchar(12) not null,
    genero varchar(20) not null,
    departamento varchar(50) not null,
    puesto varchar(50) not null,
    telefono int(9) not null,
    email varchar(100) not null,
    salario float not null,
    pagasExtra float not null,
    irpf float not null,
    seguridadsocial double not null,
    Altas boolean not null,
    fechaBaja DATE 
);'''
cursor.execute(tabla)

conexion.commit()
conexion.close()

pantallaMenu = Tk()
pantallaMenu.geometry("800x600")
pantallaMenu.title("Menu")
logo = PhotoImage(file="mario.png")
logo = logo.subsample(6)
Label(pantallaMenu,text="Nominator+",font=("Helvetica",30,"bold")).grid(row=1,column=0,columnspan=2,padx=(60,0),pady=10)
Label(pantallaMenu,image=logo).grid(row=2,column=0,columnspan=2,padx=(60,0))
Button(pantallaMenu,text="ALTAS",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),width=30,command=abrirAltas).grid(row=3,column=0,padx=60,pady=30)
Button(pantallaMenu,text="BAJAS",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),width=30,command=abrirBajasVentana).grid(row=3,column=1,pady=30)
Button(pantallaMenu,text="INFORMES",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),width=30,command=abrirInformeVentana).grid(row=4,column=0,padx=60)
Button(pantallaMenu,text="NÓMINAS",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),width=30,command=abrirNominaVentana).grid(row=4,column=1)
pantallaMenu.mainloop()