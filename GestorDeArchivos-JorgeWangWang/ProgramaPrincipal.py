#Autor Jorge Wang Wang
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
        contador = [] #Array que guarda los datos validados
        fechaActual = datetime.now() #coge la fecha actual
        #query para insertar datos
        insertarDatos="Insert into empleados(nombre,fechanacimiento,fechaalta,direccion,nif,datosbancarios,naf,genero,departamento,puesto,telefono,email,salario,pagasExtra,irpf,seguridadsocial,altas) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        
        #En cada comprobación si acierta el entry se añade al array sino añade un mensje
        #comprueba que nombre no contenga numeros y que los espacios en blancos no afecten
        if(re.match(r"^[A-Za-z]+$",nombreAlta.get().replace(" ","")) and not len(nombreAlta.get().strip())==0):
            contador.append(nombreAlta.get())
        else:
            validacionAlta.insert("end","Error Nombre y Apellidos no puede contener numeros o caracteres\n")
        #comprueba que la fecha existe y que no sea inferior a 1990 o superior al actual y el formato este bien
        if(comprobarfecha(fechanacimientoAlta.get(),"Fecha Nacimiento")):
            if(datetime.strptime(fechanacimientoAlta.get(),"%Y-%m-%d")>datetime.strptime("1900-01-01","%Y-%m-%d") and (datetime.strptime(fechanacimientoAlta.get(),"%Y-%m-%d")< fechaActual)):
                contador.append(fechanacimientoAlta.get())
            else:
                validacionAlta.insert("end",f"Error, la fecha Nacimineto no puede estar fuera del rango[1900-01-01/{fechaActual.year}-{fechaActual.month}-{fechaActual.day}]\n")
        #Comprueba que fecha alta no sea inferior a fecha de nacimiento, que tenga 18 años y el formato este bien
        if(comprobarfecha(fechaAlta.get(),"Fecha Alta")):
            if(datetime.strptime(fechaAlta.get(),"%Y-%m-%d")>datetime.strptime(fechanacimientoAlta.get(),"%Y-%m-%d")):
                if(datetime.strptime(fechaAlta.get(),"%Y-%m-%d")>datetime.strptime("1900-01-01","%Y-%m-%d") and datetime.strptime(fechaAlta.get(),"%Y-%m-%d")<fechaActual):   
                    if(calcularEdad(fechaAlta.get(),fechanacimientoAlta.get())>=18):
                        contador.append(fechaAlta.get())
                    else:
                        validacionAlta.insert("end","Error, tiene que ser mayor de 18 años\n")
                else:
                    validacionAlta.insert("end",f"Error, la fecha alta no puede estar fuera del rango[1900-01-01/{fechaActual.year}-{fechaActual.month}-{fechaActual.day}]\n")   
            else:
                validacionAlta.insert("end","Error, la fecha alta no puede ser menor que la fecha de nacimiento\n")
        #comprueba que la direccion no tenga simbolos raros que no sean los permitidos
        if(re.match(r"^[A-Za-z0-9/ªº]+$",direccionAlta.get().replace(" ",""))):
            contador.append(direccionAlta.get())
        else:
            validacionAlta.insert("end","En direccion no puede estar vacio o contener caracteres especiales menos /ªº\n")
        #comprueba el dni
        if(comprobarDni(nifAlta.get().replace(" ",""))):
            contador.append(nifAlta.get().replace(" ",""))
        #comprueba el Iban
        if(comprobarNifIban(bancoAlta.get())):
            contador.append(bancoAlta.get())
        #comprueba el NAF
        if(comprobarNaf(ssAlta.get().replace(" ",""))):
            contador.append(ssAlta.get().replace(" ",""))
        #comprueba que el combobox seleccione solo dos generos sino dara error
        if(combo.get()!="-"):
            if(combo.get()== "Hombre" or combo.get()== "Mujer" ):
                contador.append(combo.get())
            else:
                validacionAlta.insert("end","Error tiene que seleccionar un genero de las opciones\n")
        else:
            validacionAlta.insert("end","Error tiene que seleccionar un genero\n")
        #comprueba que departamento no tenga numeros o simbolos
        if(re.match(r"^[A-Za-z]+$",departamentoAlta.get().replace(" ",""))):
            contador.append(departamentoAlta.get())
        else:
            validacionAlta.insert("end","En departamento no puede estar vacio o contener caracteres especiales o números\n")
        #comprueba que puesto no tiene simbolos o departamento
        if(re.match(r"^[A-Za-z]+$",puestoAlta.get().replace(" ",""))):
            contador.append(puestoAlta.get())
        else:
            validacionAlta.insert("end","En Puesto no puede estar vacio o contener caracteres especiales o números\n")    
        #no se si hay numeros de 10 digitos pero por si acaso hace un try catch la cual si produce error no lo añade al array
        try:
            if(re.match(r"^\d{9,10}$",str(telefonoAlta.get()))):
                contador.append(telefonoAlta.get())
            else:
                validacionAlta.insert("end","En telefono tiene que ser 9 números\n")
        except TclError:
            validacionAlta.insert("end","En telefono no puede contener caracteres y tiene que ser 9 números\n")
        #comprueba que la regular expresion coincide con el correo
        if(re.match(r"^[A-Za-z0-9/_.]+@[A-Za-z]+\.[A-Za-z]{2,4}$",emailalta.get())):
            contador.append(emailalta.get())
        else:
            validacionAlta.insert("end","El correo tiene un formato incorrecto\n")
        #El resto igual comprueba de la misma manera que no contenga caracteres
        try:
            salario = SaliroAlta.get()
            if(salario>0):
                contador.append(salario)
            else:
                validacionAlta.insert("end","Error no puede ser valor 0 el Salario\n")
        except TclError:
            validacionAlta.insert("end","Error en sueldo no puede contener caracteres.\n") 
        #comprueba que no inserten algun dato extra que no sea de las opciones
        try:
            extra = int(combo2.get())
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
        #si el array se llena por completo cumplira el if
        if(len(contador)==16):
            respuesta = messagebox.askyesno("Confirmar","¿desea confirmar?") #pregunta si desea insertar el usuario
            if(respuesta):
                contador.append(True)#añade el ultimo dato
                conexion = sql.connect("empleado.db")#conecta con la base de datos y hace las operaciones
                cursor = conexion.cursor()
                cursor.execute(insertarDatos,contador)
                conexion.commit()
                validacionAlta.delete("1.0","end")#elimina en caso de que haya los errores de los entry
                validacionAlta.insert("end","Se ha añadido correctamente") #avisa al usuario del exito de la operacion
                limpiar() #limpia las operaciones y actualiza el codigo
                conexion.close() # cierra la conexion
    #calcula la edad cogiendo el tiempo y restando, ademas si el dia es inferior a su cumpleaños
    def calcularEdad(fecha,fechanacimiento):
        fecha_actual = datetime.strptime(fecha,"%Y-%m-%d")
        fecha_objeto = datetime.strptime(fechanacimiento, "%Y-%m-%d")
        edad=int(fecha_actual.year) - int(fecha_objeto.year)
        if(fecha_objeto.month,fecha_objeto.day) >(fecha_actual.month,fecha_actual.day):
            edad -=1
        return edad
        #limpia los entrys
    def limpiar():
        #actualiza el codigo con uno nuevo
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
        SaliroAlta.set("0.0")
        irpfAlta.set("0")
        emailalta.set("")
        seguridadAlta.set("0.0")
        combo.set(0)
        combo2.set(0)
    def comprobarDni(dni):
        letras= "TRWAGMYFPDXBNJZSQVHLCKE" #lista en orden de los codigos
        letnum={"X":"0","Y":"1","Z":"2"} #diccionario para sustituirlas letras en el dni
        if(len(dni)==9):
            if(re.search(r"[0-9]{8}[A-Za-z]{1}",dni)):#Comprueba si el codigo que inserto el 
                numeros = int(dni[:8])-int((int(dni[:8])/23))*23
                if(dni[-1].upper()==letras[numeros]):#comprueba que la letra sea la misma que el del usuario
                    
                    return True
                else:
                    validacionAlta.insert("end","El DNI es incorrecto en su ultima letra\n")
                    return False
            elif(re.search(r"^[x|X|Y|y|Z|z]{1}[0-9]{7}[A-Za-z]{1}$",dni)):#Comprueba si es un NIE
                numeros=int(letnum[dni[0].upper()]+dni[1:8])-(int(int(letnum[dni[0].upper()]+dni[1:8])/23)*23)
                if(letras[numeros]==dni[-1].upper()): #comprueba que el indice de numeros en el string de letras coincida con el dni del usuario
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
    #Crea y devuelve un IBAN pero realizando las operaciones
    def CreadorIBAN(cuenta):
        total=cuenta+"142800" 
        numerosiban=98-(int(total)%97) #realiza la operación para calcular los numeros de despues del ES
        if(len(str(numerosiban))==1):
            numerosiban="0" + str(numerosiban) #Crea un iban pero con los numeros creados por las operaciones 
        iban="ES"+str(numerosiban)+cuenta
        print(iban)
        return iban
    def comprobarfecha(fecha,tipo): #comprueba que la fecha tenga el formato adecuado
            
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
    #introduce el codigo actual
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
    seguridadAlta = DoubleVar()

        
    #Primera fila
    Label(pantallaAlta,text="CÓDIGO",font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=0,padx=(5,0))
    Label(pantallaAlta,text="APELLIDOS Y NOMBRES",font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=2,columnspan=8)

    #Segunda Fila

    Entry(pantallaAlta,width=15,textvariable=codigos,state="disabled").grid(row=1,column=0,padx=(5,0))
    Entry(pantallaAlta,textvariable=nombreAlta).grid(row=1,column=2,columnspan=8,sticky="ew")
    #antes de comprobar el codigo comprueba que no este vacio sino pondira 0 y no seria logico
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
    combo2 =ttk.Combobox(pantallaAlta)
    combo2.grid(row=9,column=6,sticky="ew")
    combo2["values"]=(12,13,14)
    combo2.current(0)
    Label(pantallaAlta,text="SEG.SOCIAL",font=("Microsoft Sans Serif", 8, "bold")).grid(row=9,column=7,padx=(20,0))
    Entry(pantallaAlta,textvariable=seguridadAlta).grid(row=9,column=9,sticky="ew")

    #undecima fila
    #configuracion del scroll
    validacionAlta = Text(pantallaAlta,height=5,fg="red",font=("Microsoft Sans Serif", 8, "bold"))
    validacionAlta.grid(row=10,column=0,columnspan=7,sticky="ew",padx=(30,0),pady=15)
    Button(pantallaAlta,text="CONFIRMAR",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),command=confirmar).grid(row=10,column=7,columnspan=3,sticky="ew",padx=(30,0))
    scroll = Scrollbar(pantallaAlta, command=validacionAlta.yview)
    scroll.grid(row=10, column=7, sticky="ns",padx=(0,100))
    validacionAlta.config(yscrollcommand=scroll.set)
    
    
def abrirBajasVentana():
    pantallaBaja = Toplevel()
    pantallaBaja.resizable(0,0)
    def confibaja():
        contar = []#igual que en alta usamos el mismo metodo
        texto.delete("1.0","end")
        if(re.match(r"^[-]?[0-9]+$",codigoBaja.get())):
            conectarBaja = sql.connect("empleado.db")#recogemos los datos importantes y los guardamos
            cursorbaja = conectarBaja.cursor()
            cursorbaja.execute(f"Select fechaAlta from empleados where ID = {codigoBaja.get()}")
            fechaAltita = cursorbaja.fetchall()
            cursorbaja.execute(f"Select Altas from empleados where ID = {codigoBaja.get()}")
            bajacodigoViejo = cursorbaja.fetchall()
            #comprueba que exista el empleado, que este en alta
            if(len(bajacodigoViejo)==1):
                if(bajacodigoViejo[0][0]==1):
                    try:
                        fechaAlto = datetime.strptime(fechaAltita[0][0],"%Y-%m-%d")
                        if(comprobarfecha(fechaBaja.get(),"Fecha Baja")):#comprueba que el formato de fechabaja este bien y sea mayor que el de fecha alta
                            if(fechaAlto<datetime.strptime(fechaBaja.get(),"%Y-%m-%d")):
                                contar.append(fechaBaja.get())
                                contar.append(codigoBaja.get())
                            else:
                                texto.insert("end",f"La fecha baja no puede ser menor al que alta {fechaAlto.year}-{fechaAlto.month}-{fechaAlto.day}.\n")
                    except IndexError:
                        texto.insert("end",f"Esta vacio Fecha Baja\n")

                    if(len(contar)==2):#si el array esta lleno pregunta si confirma o no
                        respuesta= messagebox.askyesno("Confirmar","¿Desea confirmar la operacion?")
                        if respuesta:
                            bajaactu = "UPDATE Empleados SET Altas = FALSE, fechaBaja = ? WHERE ID = ?" #la sentencia sql para actualizar la baja
                            cursorbaja.execute(bajaactu,contar)
                            texto.insert("end",f"Empleado con ID {contar[1]} actualizado con éxito.")
                            conectarBaja.commit()
                            limpiezabaja()
                else:
                    texto.insert("end",f"El codigo {codigoBaja.get()} ya esta dado de baja.\n")
            else:
                texto.insert("end",f"Error no existe empleado con id {codigoBaja.get()}.\n")
        else:
            texto.insert("end",f"Error no puede haber caracteres en codigo\n.")

    def limpiezabaja():
        codigoBaja.set("")
        fechaBaja.set("")
            
    def comprobarfecha(fecha,tipo): #comprueba la fecha
            
            if(re.match(r"^\d{4}-\d{1,2}-\d{1,2}$", fecha)):
                try:
                    datetime.strptime(fecha,"%Y-%m-%d")
                    return True
                except ValueError:
                    texto.insert("end",f"Error del año, mes o dia en {tipo}\n")
                    return False
            else:
                texto.insert("end",f"Error en el formato de fecha en {tipo} debe ser aaaa-mm-dd\n")
    #todo los detalles del menu
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
    def calcularEdad(fecha):#sirve para calcular la edad restando la fecha actual con la de su nacimiento y devolviendo la suma de todas ellas
        fecha_actual = datetime.now()
        edadTotal=0
    
        for fechas in fecha:
            fecha_objeto = datetime.strptime(fechas[0], "%Y-%m-%d")
            edad=int(fecha_actual.year) - int(fecha_objeto.year)
            if(fecha_objeto.month,fecha_objeto.day) <(fecha_actual.month,fecha_actual.day):
                edad -=1
            edadTotal+=edad
        return edadTotal

    def sumaSalario(salario):#suma los salarios del array que mande
        totalSalario = 0
        for salarios in salario:
            totalSalario+=float(salarios[0])
        return totalSalario
    #variables para añadir a los label
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

    cursorInforme.execute("Select count(ID) as contador from empleados")#todo los empleados
    resulTotalEmple = cursorInforme.fetchall()

    Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=empleadoAltas).grid(row=1,column=0,rowspan=2,padx=(30,0))
    cursorInforme.execute("Select count(ID) as contador from empleados where Altas = True")
    resulEmpleAlta = cursorInforme.fetchall()
    if (resulEmpleAlta[0][0])>0:#para que no suelte un error
        imprimirEmpleadoAlta=round(int(resulEmpleAlta[0][0])/int(resulTotalEmple[0][0])*100,2)#calculos para sacar la probabilidad
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
        edadSumaEmple = calcularEdad(resulEmpleEdad)#coger la suma total
        imprimirEmpleadoEdad=round(edadSumaEmple/int(resulTotalEmple[0][0]))#calcula la media
        empleadoEdad.set(str(imprimirEmpleadoEdad) + " años")

    Label(pantallaInforme,height=2,width=10,borderwidth=1,relief="solid",textvariable=empleadoRetribucion).grid(row=1,column=6,rowspan=2)
    cursorInforme.execute("SELECT salario FROM empleados")
    resulEmpleRetri=cursorInforme.fetchall()
    if len(resulEmpleRetri)>0:
        salarioEmpleTotal = sumaSalario(resulEmpleRetri)#igual en edad
        imprimirEmpleadoretri=round(salarioEmpleTotal/int(resulTotalEmple[0][0]))
        empleadoRetribucion.set(str(imprimirEmpleadoretri) + "€")

    Label(pantallaInforme,text="%MUJERES", font=("Microsoft Sans Serif", 8)).grid(row=3,column=0,padx=(30,0),pady=(20,10))
    Label(pantallaInforme,text="%MUJERES", font=("Microsoft Sans Serif", 8)).grid(row=3,column=2,pady=(20,10))
    Label(pantallaInforme,text="MUJERES", font=("Microsoft Sans Serif", 8)).grid(row=3,column=4,pady=(20,10))
    Label(pantallaInforme,text="MUJERES", font=("Microsoft Sans Serif", 8,"bold"),fg="CornflowerBlue").grid(row=3,column=6,pady=(20,10))

    cursorInforme.execute("Select count(ID) as contador from empleados where genero = 'Mujer'")
    resulTotalMujer = cursorInforme.fetchall()
    #calculos de los datos de las mujeres
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
    #calculo de los datos de los hombres
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
        # Crea un pdf
        #informacion
        conexionInforme= sql.connect("empleado.db")
        cursorInforme = conexionInforme.cursor()
        fecha_actual = datetime.now()#coge la fecha actual
        cursorInforme.execute(f"Select nombre, direccion, nif, naf,DatosBancarios,fechaalta,fechabaja,salario from empleados where id ={codigoNomina.get()}")
        datosImprimir =cursorInforme.fetchall()#guarda los datos del cliente
        #diccionarios para relacionar el mes y su numero o cantidad de dias
        diasmese={1:"ENERO",2:"FEBRERO",3:"MARZO",4:"ABRIL",5:"MAYO",6:"JUNIO",7:"JULIO",8:"AGOSTO",9:"SEPTIEMBRE",10:"OCTUBRE",11:"NOVIEMBRE",12:"DICIEMBRE"}
        mesescantidad={"ENERO":31,"FEBRERO":28,"MARZO":31,"ABRIL":30,"MAYO":31,"JUNIO":30,"JULIO":31,"AGOSTO":31,"SEPTIEMBRE":30,"OCTUBRE":30,"NOVIEMBRE":30,"DICIEMBRE":31}
        #pregunta en que lugar del archivo quiero guardar el pdf
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")],initialfile=f"{nombreNomina.get().replace(" ","-")}_Nomina.pdf")
        #pdf creado a partir de la clase canvas
        if file_path:
            c = canvas.Canvas(f"{nombreNomina.get().replace(" ","-")}_Nomina.pdf")
            c.setFont("Helvetica-Bold",11)
            c.drawString(270,780,"IMPRESO NOMINA")
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
            c.drawString(280,670,f"{datosImprimir[0][3]}")
            c.setFont("Helvetica-Bold",9)
            c.drawString(380,670,f"CCC:")
            c.setFont("Helvetica",9)
            c.drawString(410,670,f"{datosImprimir[0][4]}")
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
        if(re.match(r"^[-]?[0-9]+$",codigoNomina.get())):#comprueba que el codigo sea un numero y no un caracter
            cursorInforme.execute(f"Select nombre,fechanacimiento,fechaalta,direccion,nif,datosbancarios,naf,irpf,seguridadsocial,pagasExtra,salario from empleados where id ={codigoNomina.get()} ")
            datos = cursorInforme.fetchall()#recoge los datos
            if len(datos)!=0:#comprueba que el usuario exista y si existe imprime los datos
                textoError.insert("end",f"Empleado con ID {codigoNomina.get()} cargado con éxito.")
                listaVariables=[nombreNomina,fechanacimientoNomina,fechaNomina,direccionNomina,nifNomina,bancoNomina,ssNomina,irpfNomina,seguridadNomina,numeroPaga]
                for i in range(0,len(listaVariables)):#for para relacionar los datos con el array
                    listaVariables[i].set(datos[0][i])
                salarioTotal = int(datos[0][10])*12 #cosas extras que no estan en la base de datos
                SaliroNomina.set(str(salarioTotal))
                textoError.delete("1.0","end")
                textoError.insert("end",f"Para Imprimirlo pulsa a calcular")
                boton1["state"] = NORMAL #desbloquea el boton normal
                boton2["state"] = DISABLED #bloquea imprimir para que la nomina no salga con datos mezclados
            else:
                textoError.insert("end",f"No Existe el empleado con ID {codigoNomina.get()}.")
        else:
            textoError.insert("end",f"No puede contener Caracteres.\n")
        conexionInforme.close()
    
    def CalcularNomina():#hace los calculos necesarios
        salarioBruto = SaliroNomina.get()
        irpfPorcentaje = irpfNomina.get()
        seguridadsocialPorcentaje=seguridadNomina.get()
        salarioMesNomina.set(round((float(salarioBruto)/12),2))
        prorataNomina.set(round((float(salarioMesNomina.get())*float(numeroPaga.get()))/12,2))
        retencionIRPFNomina.set(round((salarioMesNomina.get()*irpfPorcentaje)/100,2))
        deduccionSS.set(round((prorataNomina.get()*seguridadsocialPorcentaje)/100,2))
        PercibirNomina.set(round(salarioMesNomina.get()-retencionIRPFNomina.get()-deduccionSS.get(),2))
        boton2["state"]=NORMAL #activa el boton de imprimir
        textoError.delete("1.0","end")
    
    def cambiarEstado(event):
        boton2["state"]=DISABLED
        boton1["state"]=DISABLED
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

    codigo = Entry(pantallaNomina,width=15,textvariable=codigoNomina)
    codigo.grid(row=1,column=0,padx=(5,0))
    codigo.bind("<KeyRelease>",cambiarEstado)
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

    Entry(pantallaNomina,textvariable=salarioMesNomina,state="disabled").grid(row=8,column=2,columnspan=2,sticky="ew")
    Label(pantallaNomina,text="%IRPF",font=("Microsoft Sans Serif", 8, "bold")).grid(row=8,column=4,padx=(20,0))
    Label(pantallaNomina,text="  ").grid(row=8,column=5)
    Entry(pantallaNomina,textvariable=irpfNomina,state="disabled").grid(row=8,column=6,sticky="ew")
    Label(pantallaNomina,text="RETENCION IRPF",font=("Microsoft Sans Serif", 8, "bold")).grid(row=8,column=7,padx=(20,0))
    Label(pantallaNomina,text="     ").grid(row=8,column=8)
    Entry(pantallaNomina,textvariable=retencionIRPFNomina,state="disabled").grid(row=8,column=9,sticky="ew")
    #decima fila
    Label(pantallaNomina,text="PRORRATA PAGAS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=9,column=0,padx=(10,0),columnspan=2)
    Entry(pantallaNomina,textvariable=prorataNomina,state="disabled").grid(row=9,column=2,columnspan=2,sticky="ew")
    Label(pantallaNomina,text="SEG.SOCIAL",font=("Microsoft Sans Serif", 8, "bold")).grid(row=9,column=4,padx=(20,0))
    Entry(pantallaNomina,textvariable=seguridadNomina,state="disabled").grid(row=9,column=6,sticky="ew")
    Label(pantallaNomina,text="DEDUCCION SS",font=("Microsoft Sans Serif", 8, "bold")).grid(row=9,column=7,padx=(20,0))
    Entry(pantallaNomina,textvariable=deduccionSS,state="disabled").grid(row=9,column=9,sticky="ew")

    #undecima fila
    textoError = Text(pantallaNomina,height=3,fg="red",font=("Microsoft Sans Serif", 8, "bold"))
    textoError.grid(row=10,column=0,columnspan=7,sticky="ew",padx=(30,0),pady=15)
    Label(pantallaNomina,text="A PERCIBIR",font=("Microsoft Sans Serif", 8, "bold")).grid(row=10,column=7,sticky="ew")
    Entry(pantallaNomina,textvariable=PercibirNomina,state="disabled").grid(row=10,column=8,columnspan=2,sticky="ew")


    Button(pantallaNomina,text="CARGAR EMPLEADO",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),command=cargarEmpleado).grid(row=11,column=0,columnspan=7)
    boton1 =Button(pantallaNomina,text="CALCULAR",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),state="disabled",command=CalcularNomina)
    boton1.grid(row=11,column=7)
    boton2 =Button(pantallaNomina,text="IMPRIMIR",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),state="disabled",command=capture_to_pdf)
    boton2.grid(row=11,column=9)


def mostrarAutor():
    messagebox.showinfo("Creador Programa","Autor: Jorge Wang Wang\nClase: Dam2\nModulo: Sistema de Gestion Empresarial")
    
conexion = sql.connect("empleado.db")
cursor = conexion.cursor()
#sentencia sql para crear la tabla si no existiese
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

#Detalles del Menu
pantallaMenu = Tk()
pantallaMenu.geometry("800x600")
pantallaMenu.title("Menu")
pantallaMenu.resizable(0,0)
logo = PhotoImage(file="mario.png") #importa la imagen
logo = logo.subsample(6) #hace la imagen mas pequeña en escala
Label(pantallaMenu,text="Nominator+",font=("Helvetica",30,"bold")).grid(row=1,column=0,columnspan=2,padx=(60,0),pady=10)
Label(pantallaMenu,image=logo).grid(row=2,column=0,columnspan=2,padx=(60,0))
Button(pantallaMenu,text="ALTAS",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),width=30,command=abrirAltas).grid(row=3,column=0,padx=60,pady=30)
Button(pantallaMenu,text="BAJAS",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),width=30,command=abrirBajasVentana).grid(row=3,column=1,pady=30)
Button(pantallaMenu,text="INFORMES",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),width=30,command=abrirInformeVentana).grid(row=4,column=0,padx=60)
Button(pantallaMenu,text="NÓMINAS",padx=10,pady=10, relief="raised",borderwidth=5, background="#4CAF50", foreground="white", font=("Helvetica", 12),width=30,command=abrirNominaVentana).grid(row=4,column=1)
Button(pantallaMenu,text="?",width=5,command=mostrarAutor).grid(row=5,column=0,columnspan=3,padx=(60,0),pady=20)
pantallaMenu.mainloop()
