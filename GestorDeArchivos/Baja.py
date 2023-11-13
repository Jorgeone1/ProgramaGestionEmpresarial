from tkinter import *

pantallaBaja = Tk()

pantallaBaja.geometry("500x500")

Label(pantallaBaja,text="CODIGO EMPLEADO").grid(row=0,column=0,padx=30,pady=30)
Label(pantallaBaja,text="FECHA BAJA").grid(row=0,column=1,padx=30,pady=30)

Entry(pantallaBaja).grid(row=1,column=0)
Entry(pantallaBaja).grid(row=1,column=1)

Text(pantallaBaja,height=5,width=50).grid(row=2,column=0,columnspan=2,padx=30)

Button(pantallaBaja,text="CONFIRMAR").grid(row=3,column=0,columnspan=2,padx=30)
pantallaBaja.mainloop()
