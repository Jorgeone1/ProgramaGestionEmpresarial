from tkinter import *

pantallaInforme = Tk()
pantallaInforme.geometry("800x600")

Label(pantallaInforme,text="Empleado\nAltas").grid(row=0,column=0)
Label(pantallaInforme,text="      ").grid(row=0,column=1)
Label(pantallaInforme,text="EMPLEADO BAJAS").grid(row=0,column=2)
Label(pantallaInforme,text="                 ").grid(row=0,column=3)
Label(pantallaInforme,text="EDADES MEDIAS").grid(row=0,column=4)
Label(pantallaInforme,text="                  ").grid(row=0,column=5)
Label(pantallaInforme,text="RETRIBUCION MEDIA").grid(row=0,column=6)

Text(pantallaInforme,height=2,width=10).grid(row=1,column=0,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=1,column=2,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=1,column=4,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=1,column=6,rowspan=2)

Label(pantallaInforme,text="%MUJERES").grid(row=3,column=0)
Label(pantallaInforme,text="%MUJERES").grid(row=3,column=2)
Label(pantallaInforme,text="MUJERES").grid(row=3,column=4)
Label(pantallaInforme,text="MUJERES").grid(row=3,column=6)

Text(pantallaInforme,height=2,width=10).grid(row=4,column=0,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=4,column=2,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=4,column=4,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=4,column=6,rowspan=2)

Label(pantallaInforme,text="%HOMBRES").grid(row=6,column=0)
Label(pantallaInforme,text="%HOMBRES").grid(row=6,column=2)
Label(pantallaInforme,text="HOMBRES").grid(row=6,column=4)
Label(pantallaInforme,text="HOMBRES").grid(row=6,column=6)

Text(pantallaInforme,height=2,width=10).grid(row=7,column=0,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=7,column=2,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=7,column=4,rowspan=2)
Text(pantallaInforme,height=2,width=10).grid(row=7,column=6,rowspan=2)

pantallaInforme.mainloop()