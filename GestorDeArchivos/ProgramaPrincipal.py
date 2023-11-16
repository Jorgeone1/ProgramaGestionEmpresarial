import tkinter as tk
import sqlite3 as sql

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
    seguridadsocial int(9) not null,
    Altas boolean not null
);'''
cursor.execute(tabla)

conexion.commit()
datos = ("Jorge","2002-12-5","2009-05-02","Parla villaverde alto 12 4 izq","12345678E","ES213123123412123456789",121234567812,"Hombre","informatica","secretario",659839212,"paco@gmaicl.com",120.20,20.50,10,123456789,True)
print(len(datos))
insertarDatos="Insert into empleados(nombre,fechanacimiento,fechaalta,direccion,nif,datosbancarios,naf,genero,departamento,puesto,telefono,email,salario,pagasExtra,irpf,seguridadsocial,altas) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
cursor.execute(insertarDatos,datos)
conexion.commit()
consulta = "Select * from empleados"
cursor.execute(consulta)

# Obtener todos los resultados de la consulta
resultados = cursor.fetchall()

# Imprimir los resultados
for resultado in resultados:
    print(resultado)

conexion.close()