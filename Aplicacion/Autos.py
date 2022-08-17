from tkinter import *
from tkinter import messagebox

root=Tk()


miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)
cuadromatricula=Entry(miFrame, textvariable=miID)
cuadromatricula.grid(row=0, column=3, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")
cuadromodelo=Entry(miFrame, textvariable=miNombre)
cuadromodelo.grid(row=1, column=3, padx=10, pady=10)
cuadromodelo.config(fg="red", justify="right")

cuadroID=Entry(miFrame, textvariable=miID)
cuadroID.grid(row=2, column=1, padx=10, pady=10)

# comienzo de los labels -------------------------------------------------------------------

modelo=Label(miFrame, text="modelo: ")
modelo.grid(row=0, column=0, sticky="e", padx=10, pady=10)
nusuario=Label(miFrame, text="Id usuario: ")
nusuario.grid(row=0, column=2, sticky="e", padx=10, pady=10)

marcaLabel=Label(miFrame, text="marca: ")
marcaLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
matricula=Label(miFrame, text="matricula: ")
matricula.grid(row=1, column=2, sticky="e", padx=10, pady=10)

colorLabel=Label(miFrame, text="color: ")
colorLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

#Frame  de busqueda ---------------------------------------------

miFrame2=Frame(root)
miFrame2.pack()

matricula=Label(miFrame, text="matricula ")
matricula.grid(row=4, column=0, sticky="e", padx=10, pady=10)
model=Label(miFrame, text="modelo ")
model.grid(row=4, column=1, sticky="e", padx=10, pady=10)
clabel=Label(miFrame, text="color ")
clabel.grid(row=4, column=2, sticky="e", padx=10, pady=10)
mlabel=Label(miFrame, text="marca ")
mlabel.grid(row=4, column=3, sticky="e", padx=10, pady=10)


cuadroB=Entry(miFrame, textvariable=miID)
cuadroB.grid(row=5, column=0, padx=10, pady=10)
cuadroB1=Entry(miFrame, textvariable=miID)
cuadroB1.grid(row=5, column=1, padx=10, pady=10)
cuadroB2=Entry(miFrame, textvariable=miID)
cuadroB2.grid(row=5, column=2, padx=10, pady=10)
cuadroB3=Entry(miFrame, textvariable=miID)
cuadroB3.grid(row=5, column=3, padx=10, pady=10)

# Frame de los botones -------------------------------------------

miFrame3=Frame(root)
miFrame3.pack()

botonGuardar=Button(miFrame3, text="Guardar cambios")
botonGuardar.grid(row=1, column=1, sticky="e", padx=5, pady=5)

botonVolver=Button(miFrame3, text="Volver a ventana logueo")
botonVolver.grid(row=1, column=2, sticky="e", padx=5, pady=5)

root.mainloop()