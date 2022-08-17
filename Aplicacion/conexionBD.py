import MySQLdb as mysql

def conectar(user, password, bd, server='localhost'):
    conexion = None
    try:
        conexion = mysql.connect(user=user,
                                 password=password,
                                 host=server, database=bd)
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Información de identificación erronea")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La BD no existe")
        else:
            print(err)
        return None
    return conexion

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
    #miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() + "', PASSWORD='" + miPass.get() + "',APELLIDO='" + miApellido.get() + "', DIRECCION='" + miDireccion.get() + "', COMENTARIOS='" + textoComentario.get("1.0", END)+ "' WHERE ID=" + miID.get())
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, APELLIDO=?, PASSWORD=?, DIRECCION=?, COMENTARIOS=? " + "WHERE ID=" + miID.get(),(datos))
    miConexion.commit()
    messagebox.showinfo("Base de datos", "Registro actualizado con excito!")

def eliminar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miID.get())
    miConexion.commit()
    messagebox.showinfo("Base de datos", "Registro borrado con exito!")