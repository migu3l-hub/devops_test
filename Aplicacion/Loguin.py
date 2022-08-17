from tkinter import *
from tkinter import messagebox

ventana=Tk()

barraMenu=Menu(ventana)
ventana.config(menu=barraMenu, width=100, height=300)

usuarioTipo=Menu(barraMenu, tearoff=0)
usuarioTipo.add_command(label="Usuario especializado")
usuarioTipo.add_command(label="Usuario cliente")

barraMenu.add_cascade(label="Elegir usuario", menu=usuarioTipo)

#-------------parte principal----

miFrame=Frame(ventana)
miFrame.pack()

instruccion=Label(miFrame, text="Ingrese como cliente al sistema para hacer reservas")
instruccion.grid(row=0, column=1, sticky="n", padx=10, pady=10)

nomusuario=Label(miFrame, text="Nombre del usuario:")
nomusuario.grid(row=1, column=0, sticky="e", padx=10, pady=10)
contraseñaL=Label(miFrame, text="Contraseña:")
contraseñaL.grid(row=2, column=0, sticky="e", padx=10, pady=10)

nusuario=Entry(miFrame)
nusuario.grid(row=1, column=1, padx=10, pady=10)
pusuario=Entry(miFrame)
pusuario.grid(row=2, column=1, padx=10, pady=10)

botonAcceder=Button(miFrame, text="Acceder")
botonAcceder.grid(row=1, column=2)

#---------------mitad-------------------#

instruccion=Label(miFrame, text="Escriba su nombre y constraseña de administrador")
instruccion.grid(row=3, column=1, sticky="n", padx=10, pady=10)

adminombre=Label(miFrame, text="Nombre del administrador:")
adminombre.grid(row=4, column=0, sticky="e", padx=10, pady=10)
paswAdmin=Label(miFrame, text="Contraseña:")
paswAdmin.grid(row=5, column=0, sticky="e", padx=10, pady=10)

nomadmin=Entry(miFrame)
nomadmin.grid(row=4, column=1, padx=10, pady=10)
padmin=Entry(miFrame)
padmin.grid(row=5, column=1, padx=10, pady=10)

Acceder=Button(miFrame, text="Acceder")
Acceder.grid(row=4, column=2)
ventana.mainloop()
