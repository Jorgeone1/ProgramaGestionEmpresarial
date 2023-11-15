from tkinter import *

pantallaInforme = Tk()
pantallaInforme.geometry("650x300")

Label(pantallaInforme,text="Empleado\nAltas", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=0,padx=(30,0),pady=(20,10))
Label(pantallaInforme,text="      ").grid(row=0,column=1)
Label(pantallaInforme,text="EMPLEADO\nBAJAS", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=2,pady=(20,10))
Label(pantallaInforme,text="                 ").grid(row=0,column=3)
Label(pantallaInforme,text="EDADES\nMEDIAS", font=("Microsoft Sans Serif", 8, "bold")).grid(row=0,column=4,pady=(20,10))
Label(pantallaInforme,text="                  ").grid(row=0,column=5)
Label(pantallaInforme,text="RETRIBUCION\nMEDIA", font=("Microsoft Sans Serif", 8, "bold"),fg="Blue").grid(row=0,column=6,pady=(20,10))

Text(pantallaInforme,height=2,width=10).grid(row=1,column=0,rowspan=2,padx=(30,0))
Text(pantallaInforme,height=2,width=10).grid(row=1,column=2,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=1,column=4,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=1,column=6,rowspan=2)

Label(pantallaInforme,text="%MUJERES", font=("Microsoft Sans Serif", 8)).grid(row=3,column=0,padx=(30,0),pady=(20,10))
Label(pantallaInforme,text="%MUJERES", font=("Microsoft Sans Serif", 8)).grid(row=3,column=2,pady=(20,10))
Label(pantallaInforme,text="MUJERES", font=("Microsoft Sans Serif", 8)).grid(row=3,column=4,pady=(20,10))
Label(pantallaInforme,text="MUJERES", font=("Microsoft Sans Serif", 8,"bold"),fg="CornflowerBlue").grid(row=3,column=6,pady=(20,10))

Text(pantallaInforme,height=2,width=10).grid(row=4,column=0,rowspan=2,padx=(30,0))
Text(pantallaInforme,height=2,width=10).grid(row=4,column=2,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=4,column=4,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=4,column=6,rowspan=2)

Label(pantallaInforme,text="%HOMBRES", font=("Microsoft Sans Serif", 8)).grid(row=6,column=0,padx=(30,0),pady=(20,10))
Label(pantallaInforme,text="%HOMBRES", font=("Microsoft Sans Serif", 8)).grid(row=6,column=2,pady=(20,10))
Label(pantallaInforme,text="HOMBRES", font=("Microsoft Sans Serif", 8)).grid(row=6,column=4,pady=(20,10))
Label(pantallaInforme,text="HOMBRES", font=("Microsoft Sans Serif", 8,"bold"),fg="CornflowerBlue").grid(row=6,column=6,pady=(20,10))

Text(pantallaInforme,height=2,width=10).grid(row=7,column=0,rowspan=2,padx=(30,0))
Text(pantallaInforme,height=2,width=10).grid(row=7,column=2,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=7,column=4,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=7,column=6,rowspan=2)

pantallaInforme.mainloop()