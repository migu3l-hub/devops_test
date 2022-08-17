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

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")
cuadrocolor=Entry(miFrame, textvariable=miPass)
cuadrocolor.grid(row=2, column=3, padx=10, pady=10)

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)
cuadromarca=Entry(miFrame, textvariable=miApellido)
cuadromarca.grid(row=3, column=3, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10)


# comienzo de los labels -------------------------------------------------------------------

idLabel=Label(miFrame, text="ID: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
matricula=Label(miFrame, text="matricula: ")
matricula.grid(row=0, column=2, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
modelo=Label(miFrame, text="modelo: ")
modelo.grid(row=1, column=2, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Telefono: ")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)
color=Label(miFrame, text="color: ")
color.grid(row=2, column=2, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
marca=Label(miFrame, text="marca: ")
marca.grid(row=3, column=2, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)


# Frame de los botones -------------------------------------------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Crear")
botonCrear.grid(row=1, column=0, sticky="e", padx=5, pady=5)

botonLeer=Button(miFrame2, text="Leer")
botonLeer.grid(row=1, column=1, sticky="e", padx=5, pady=5)

botonActualizar=Button(miFrame2, text="Actualizar")
botonActualizar.grid(row=1, column=2, sticky="e", padx=5, pady=5)

botonBorrar=Button(miFrame2, text="Borrar")
botonBorrar.grid(row=1, column=3, sticky="e", padx=5, pady=5)


root.mainloop()