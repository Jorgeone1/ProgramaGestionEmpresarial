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
    seguridadsocial double not null,
    Altas boolean not null,
    fechaBaja DATE 
);'''
cursor.execute(tabla)

conexion.commit()

consulta = "Select * from empleados"
cursor.execute(consulta)

# Obtener todos los resultados de la consulta
resultados = cursor.fetchall()

# Imprimir los resultados
for resultado in resultados:
    print(resultado)
print("------------------------------")
cursor.execute("Select * from empleados where Altas = True")

# Obtener todos los resultados de la consulta
resultados = cursor.fetchall()

# Imprimir los resultados
for resultado in resultados:
    print(resultado)
conexion.close()