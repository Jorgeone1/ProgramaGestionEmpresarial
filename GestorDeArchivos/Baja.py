from tkinter import *

pantallaBaja = Tk()

pantallaBaja.geometry("550x300")

Label(pantallaBaja,text="CODIGO EMPLEADO", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=0,padx=(90,30),pady=(30,0))
Label(pantallaBaja,text="FECHA BAJA", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=1,padx=(40,80),pady=(30,0))

Entry(pantallaBaja,width=25).grid(row=1,column=0,padx=(90,30))
Entry(pantallaBaja,width=25).grid(row=1,column=1,padx=(40,80))

Label(pantallaBaja,height=3,width=30,borderwidth=3, relief="solid",text="Mensaje", font=("Microsoft Sans Serif", 12, "bold"),fg="red").grid(row=2,column=0,columnspan=2,pady=(30,0))

Button(pantallaBaja,text="CONFIRMAR").grid(row=3,column=0,columnspan=2,padx=30,pady=(30,0))
pantallaBaja.mainloop()
