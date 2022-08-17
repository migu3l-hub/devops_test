from tkinter import *
from tkinter import messagebox
import sqlite3

#Cada frame se puede dividir en diferentes filas y columnas con grid
# Al crear un menu y pasarle como primer parametro otro menu hacemos referencia a que el menu estara dentro del otro menu
# recuerda que si le pones "()"  a las funciones se activan automaticamente al ser leidas
# para poder rescatar el texto que el usuario escribe en una caja de texto se deben crear variables asociadas a la caja de texto para que alli se guarde la informacion
# CONSULTA PARAMETRISADA sirve para no poner toda la instruccion de mysql para insertar o hacer algun movimiento en la base de datos esto consiste en crear una variable
# que lleve todas las demas variables donde van los campos que se quieran insertar en la base de datos el ejemplo esta en la funcion crear()
# se usa esta sintaxis miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
# donde el primer parametro de esta funcion tiene 5 signos de interrogacion correspondientes a los valores que seran insertados en orden que la variable en la que
# almacenamos todos los campos que queremos insertar el primero es NULL por que es el ID y lo pusimos como campo autoincrementable
# el segundo parametro es la variable donde estan todos los campos que queremos insertar esta variable es un arreglo
# UNA BUENA PRACTICA SERIA MODULARIZAR ESTAS FUNCIONES EN PAQUETES PARA PODER USARLAS CUANDO QUERAMOS

root=Tk()


# ------ funciones-------------------------------------------------

def conexionBD():
    miConexion=sqlite3.connect("Usuarios")# se crea la base de datos usuarios si no exciste
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            APELLIDO VARCHAR(10),
            PASSWORD VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
        ''')
        messagebox.showinfo("Base de datos", "Base de datos creada con excito!!") # es una ventana emergente el primer parametro es el titulo de la ventana el segundo  lo que dice
    except:
        messagebox.showwarning("Atencion!", "La base de datos ya exciste!")

def salirAplicacion():
    valor=messagebox.askquestion("Salir","Deseas realmente salir de la aplicacion?") # askquestion retorna un valor que puede ser evaluado despues
    if valor=="yes":
        root.destroy()

def limpiarCampos():
    miNombre.set("")
    miID.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    textoComentario.delete(1.0,END) # se borra el cuadro de texto desde el primer caracter hasta el final

def crear():
    miConexion=sqlite3.connect("Usuarios") # si la base de datos exciste se conecta con ella
    miCursor=miConexion.cursor()
    #Esta es la forma de insertar valores desde variables que estan en un cuadro de texto a una base de datos
    #miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'" + miNombre.get() + "','" + miApellido.get() + "','" + miPass.get() + "','" + miDireccion.get()+ "','" + textoComentario.get("1.0",END)+ "')")
    datos=miNombre.get(),miApellido.get(),miPass.get(),miDireccion.get(),textoComentario.get("1.0",END)
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
    miConexion.commit()

    messagebox.showinfo("Base de datos","Registro insertado con exito")

def leer():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miID.get())
    usuario=miCursor.fetchall()
    for user in usuario:
        miID.set(user[0])
        miNombre.set(user[1])
        miPass.set(user[3])
        miApellido.set(user[2])
        miDireccion.set(user[4])
        textoComentario.insert(1.0, user[5])

    miConexion.commit()

def actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    datos = miNombre.get(), miApellido.get(), miPass.get(), miDireccion.get(), textoComentario.get("1.0", END)
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, APELLIDO=?, PASSWORD=?, DIRECCION=?, COMENTARIOS=? " + "WHERE ID=" + miID.get(),(datos))
    miConexion.commit()
    messagebox.showinfo("Base de datos", "Registro actualizado con excito!")

def eliminar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miID.get())
    miConexion.commit()
    messagebox.showinfo("Base de datos", "Registro borrado con exito!")


#------------------------------------------------------------------------
#INTERFAZ GRAFICA

barraMenu=Menu(root) # se especifica que el menu estara dentro de nuestra raiz
root.config(menu=barraMenu, width=300, height=300)

BDMenu=Menu(barraMenu, tearoff=0) #quita las rayitas de los menus en la barra de menu
BDMenu.add_command(label="Conectar", command=conexionBD) # esto crea las opciones dentro de los menus
BDMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0) #quita las rayitas de los menus en la barra de menu
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos) # son las etiquetas que aparecen al pulsar en el menu

crudMenu=Menu(barraMenu, tearoff=0) #quita las rayitas de los menus en la barra de menu
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar" ,command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0) #quita las rayitas de los menus en la barra de menu
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de....")

barraMenu.add_cascade(label="BBDD", menu=BDMenu) #con esto le decimos a nuestro menu principal que debe agregar una etiqueta label y el menu al que hace referencua es BDMenu
barraMenu.add_cascade(label="Borrar", menu=borrarMenu) # se debe especificar con cada menu que queremos que este dentro el menu principal
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#-------------comienzo de cuadro de textos (Entry)------------------------------------

miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miID) # el parametro textvariable es donde le indicamos al cuadro de texto la variable donde se almacenara lo que escriba el usuario
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right") #fg= foreground (color frontal)

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=5,pady=5)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview) # esto logra que se deplaze el texto en forma vertical
scrollVert.grid(row=5, column=2, sticky="nsew") # sticky es la posicion del objeto dentro de su cuadrito
textoComentario.config(yscrollcommand=scrollVert.set) # sirve para que la scroll se ajuste a lo que se escriba en el cuadro de texto



# comienzo de los labels -------------------------------------------------------------------

idLabel=Label(miFrame, text="ID: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password: ")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=5, pady=5)


# Frame de los botones -------------------------------------------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Crear", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=5, pady=5)


botonLeer=Button(miFrame2, text="Leer", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=5, pady=5)

botonActualizar=Button(miFrame2, text="Actualizar", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=5, pady=5)

botonBorrar=Button(miFrame2, text="Borrar", command=eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=5, pady=5)




root.mainloop()