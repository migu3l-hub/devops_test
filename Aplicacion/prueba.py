import tkinter as Tk
from tkinter import messagebox
from functools import partial
import MySQLdb as mysql
import sys

nombre = ''
apellido = ''
direccion = ''
telefono = ''
nomUser = ''

########################################################################
class MyApp(object):
    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Menu principal")
        self.frame = Tk.Frame(parent)
        self.frame.grid()

        etiquetaPrincipal = Tk.Label(self.frame, text='Menus', fg='gray').grid(row=0, column=1)
        etiquetaDos = Tk.Label(self.frame, text='Menu de clientes', fg='red').grid(row=4, column=1)
        etiquetaPrincipal = Tk.Label(self.frame, text='Menu de administradores', fg='red').grid(row=1, column=1)
        btn = Tk.Button(self.frame, text="Clientes", command=self.RegistroCliente).grid(row=5, column=0)
        btn1 = Tk.Button(self.frame, text="Fechas", command=self.Registrofechas).grid(row=5, column=1)
        btn2 = Tk.Button(self.frame, text="Reservas", command=self.RegistroReserva).grid(row=5, column=2)
        btn3 = Tk.Button(self.frame, text="Vehiculos", command=self.RegistroVehiculo).grid(row=6, column=1)
        btn4 = Tk.Button(self.frame, text="reservas", command=self.Adminreserva).grid(row=2, column=2)
        btn5 = Tk.Button(self.frame, text="Clientes", command=self.Admincliente).grid(row=2, column=0)
        btn6 = Tk.Button(self.frame, text="Fechas", command=self.Adminfechas).grid(row=2, column=1)
        btn6 = Tk.Button(self.frame, text="Vehiculos", command=self.Adminvehiculo).grid(row=3, column=1)


    # ----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()

    # ------------------------------Conexion BD -------------
    # def conexion(self,user='peta', password='cachacuas', bd='alquilerautos', server='localhost'):
    #     conexion = None
    #     try:
    #         conexion = mysql.connect(user=user,
    #                                  password=password,
    #                                  host=server, database=bd)
    #     except mysql.Error as err:
    #         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #             print("Información de identificación erronea")
    #         elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #             print("La BD no existe")
    #         else:
    #             print(err)
    #         return None
    #     return conexion

    def crear(self,id,nombre,apellido,direccion,telefono):
        conexion = mysql.connect(user='peta',password='cachacuas',host='localhost', database='alquilerautos')
        cursor = conexion.cursor()
        datos = (id.get(),nombre.get(),apellido.get(),direccion.get(),telefono.get())
        mySql_insert_query = """INSERT INTO clientes (id_cliente, nombre, apellido, direccion,telefono) 
                                   VALUES 
                                   (%s, %s, %s, %s,%s) """
        cursor.execute(mySql_insert_query,datos)
        conexion.commit()
        messagebox.showinfo("Base de datos", "Registro insertado con exito")
        conexion.close()

    def leerCliente(self,idUser,nombre,apellido,direccion,telefono):
        conexion = mysql.connect(user='peta', password='cachacuas', host='localhost', database='alquilerautos')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id_cliente=" + idUser.get())
        usuario = cursor.fetchall()
        for user in usuario:
            idUser.set(user[0])
            nombre.set(user[1])
            apellido.set(user[4])
            direccion.set(user[2])
            telefono.set(user[3])
        conexion.commit()
        messagebox.showinfo("Base de datos", "Registro leido con exito")
        conexion.close()

    def actualizarCliente(self,idUser,nombre,apellido,direccion,telefono):
        conexion = mysql.connect(user='peta', password='cachacuas', host='localhost', database='alquilerautos')
        cursor = conexion.cursor()
        datos = (nombre.get(), apellido.get(), direccion.get(), telefono.get(), idUser.get())
        consulta = """UPDATE clientes set nombre=%s,apellido=%s,direccion=%s,telefono=%s WHERE id_cliente=%s"""
        cursor.execute(consulta,datos)
        conexion.commit()
        messagebox.showinfo("Base de datos", "Registro actualizado con excito!")

    def eliminarCliente(self,idUser):
        conexion = mysql.connect(user='peta', password='cachacuas', host='localhost', database='alquilerautos')
        cursor = conexion.cursor()
        datos = (idUser.get(),)
        consulta = """DELETE FROM clientes WHERE id_cliente=%s"""
        cursor.execute(consulta,datos)
        conexion.commit()
        messagebox.showinfo("Base de datos", "Registro eliminado con excito!")

    def crearReserva(self, id, precio):
        conexion = mysql.connect(user='peta', password='cachacuas', host='localhost', database='alquilerautos')
        cursor = conexion.cursor()
        datos = (id.get(), precio.get())
        mySql_insert_query = """INSERT INTO reserva (id_reserva, precio_total) 
                                    VALUES 
                            (%s, %s) """
        cursor.execute(mySql_insert_query, datos)
        conexion.commit()
        messagebox.showinfo("Base de datos", "Registro insertado con exito")
        conexion.close()

    def leerReserva(self, id,precio):
        conexion = mysql.connect(user='peta', password='cachacuas', host='localhost', database='alquilerautos')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM reserva WHERE id_reserva=" + id.get())
        reservas = cursor.fetchall()
        for reserva in reservas:
            id.set(reserva[0])
            precio.set(reserva[1])
        conexion.commit()
        messagebox.showinfo("Base de datos", "Registro leido con exito")
        conexion.close()

    def actualizarReserva(self,id,precio):
        conexion = mysql.connect(user='peta', password='cachacuas', host='localhost', database='alquilerautos')
        cursor = conexion.cursor()
        datos = (precio.get(), id.get())
        consulta = """UPDATE reserva set precio_total=%s WHERE id_reserva=%s"""
        cursor.execute(consulta,datos)
        conexion.commit()
        messagebox.showinfo("Base de datos", "Registro actualizado con excito!")

    def eliminarReserva(self,id):
        conexion = mysql.connect(user='peta', password='cachacuas', host='localhost', database='alquilerautos')
        cursor = conexion.cursor()
        datos = (id.get(),)
        consulta = """DELETE FROM reserva WHERE id_reserva=%s"""
        cursor.execute(consulta,datos)
        conexion.commit()
        messagebox.showinfo("Base de datos", "Registro eliminado con excito!")




    def crearCoche(self, matricula,modelo,color,marca,reserva):
        conexion = mysql.connect(user='peta', password='cachacuas', host='localhost', database='alquilerautos')
        cursor = conexion.cursor()
        datos = (matricula.get(),modelo.get(),color.get(),marca.get(),reserva.get())
        mySql_insert_query = """INSERT INTO coche (matricula, modelo,color,marca,id_reserva) 
                                    VALUES 
                            (%s, %s, %s, %s, %s) """
        cursor.execute(mySql_insert_query, datos)
        conexion.commit()
        messagebox.showinfo("Base de datos", "Registro insertado con exito")
        conexion.close()

    def crearFecha(self, idReserva,idcliente,fechaInicio,fechaFinal):
        conexion = mysql.connect(user='peta', password='cachacuas', host='localhost', database='alquilerautos')
        cursor = conexion.cursor()
        datos = (idReserva.get(),idcliente.get(),fechaInicio.get(),fechaFinal.get())
        mySql_insert_query = """INSERT INTO fechas (id_reserva,id_cliente,fecha_inicio,fecha_final) 
                                    VALUES 
                            (%s, %s, %s, %s) """
        cursor.execute(mySql_insert_query, datos)
        conexion.commit()
        messagebox.showinfo("Base de datos", "Registro insertado con exito")
        conexion.close()
    # ------------------------------INTEFACEZ-------------------------------------------------------------------------
    def RegistroCliente(self):
        """"""
        self.hide()
        global nomUser,apUser,dirUser,telUser,idUser
        otherFrame = Tk.Toplevel()
        otherFrame.geometry("280x250")
        otherFrame.title("Registro de clientes")
        Tk.Label(otherFrame, text='Ingrese los datos de cliente', fg='red').grid(row=0, column=2)
        Tk.Label(otherFrame, text='ID cliente', fg='red').grid(row=1, column=1)
        Tk.Label(otherFrame, text='Nombre', fg='red').grid(row=2, column=1)
        Tk.Label(otherFrame, text='Apellido', fg='red').grid(row=3, column=1)
        Tk.Label(otherFrame, text='Direccion', fg='red').grid(row=4, column=1)
        Tk.Label(otherFrame, text='Telefono', fg='red').grid(row=5, column=1)
        Tk.Entry(otherFrame, textvariable=idUser).grid(row=1, column=2)
        Tk.Entry(otherFrame, textvariable=nomUser).grid(row=2, column=2)
        Tk.Entry(otherFrame, textvariable=apUser).grid(row=3, column=2)
        Tk.Entry(otherFrame, textvariable=dirUser).grid(row=4, column=2)
        Tk.Entry(otherFrame, textvariable=telUser).grid(row=5, column=2)
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        Tk.Button(otherFrame, text="Regresar", command=handler).grid(row=7, column=1)
        Tk.Button(otherFrame, text="Guardar", command=partial(self.crear,idUser,nomUser,apUser,dirUser,telUser)).grid(row=7,column=2)


    def RegistroReserva(self):
        """"""
        self.hide()
        otherFrame = Tk.Toplevel()
        otherFrame.title("Reservas")
        global idReserva
        global precio

        Tk.Label(otherFrame, text='Ingrese los datos de la reserva', fg='red').grid(row=0, column=2)
        Tk.Label(otherFrame, text='ID reserva', fg='red').grid(row=1, column=1)
        Tk.Label(otherFrame, text='precio', fg='red').grid(row=2, column=1)

        Tk.Entry(otherFrame, textvariable=idReserva).grid(row=1, column=2)
        Tk.Entry(otherFrame, textvariable=precio).grid(row=2, column=2)

        handler = lambda: self.onCloseOtherFrame(otherFrame)
        Tk.Button(otherFrame, text="Cerrar", command=handler).grid(row=3, column=3)
        Tk.Button(otherFrame, text="Guardar", command=partial(self.crearReserva,idReserva,precio)).grid(row=3,column=2)

    def RegistroVehiculo(self):
        self.hide()
        otherFrame = Tk.Toplevel()
        global matricula, color, marca, modelo,idReservaCoche
        otherFrame.title("Registrar Vehiculo")

        Tk.Label(otherFrame, text='Ingrese los datos de el auto', fg='red').grid(row=0, column=2)
        Tk.Label(otherFrame, text='Matricula', fg='red').grid(row=1, column=1)
        Tk.Label(otherFrame, text='modelo', fg='red').grid(row=2, column=1)
        Tk.Label(otherFrame, text='color', fg='red').grid(row=3, column=1)
        Tk.Label(otherFrame, text='marca', fg='red').grid(row=4, column=1)
        Tk.Label(otherFrame, text='id_reserva', fg='red').grid(row=5, column=1)

        Tk.Entry(otherFrame, textvariable=matricula).grid(row=1, column=2)
        Tk.Entry(otherFrame, textvariable=modelo).grid(row=2, column=2)
        Tk.Entry(otherFrame, textvariable=color).grid(row=3, column=2)
        Tk.Entry(otherFrame, textvariable=marca).grid(row=4, column=2)
        Tk.Entry(otherFrame, textvariable=idReservaCoche).grid(row=5, column=2)

        handler = lambda: self.onCloseOtherFrame(otherFrame)
        Tk.Button(otherFrame, text="Cerrar", command=handler).grid(row=7, column=3)
        Tk.Button(otherFrame, text="Guardar", command=partial(self.crearCoche,matricula,modelo,color,marca,idReservaCoche)).grid(row=7,column=2)


    def Registrofechas(self):
        self.hide()
        otherFrame = Tk.Toplevel()
        global idClienteFecha, idReservaFecha, fechaInicio, fechaFinal
        otherFrame.title("Reservas")

        Tk.Label(otherFrame, text='Ingrese los datos de las fechas', fg='red').grid(row=0, column=2)
        Tk.Label(otherFrame, text='ID reserva', fg='red').grid(row=1, column=1)
        Tk.Label(otherFrame, text='ID cliente', fg='red').grid(row=2, column=1)
        Tk.Label(otherFrame, text='Fecha entrega', fg='red').grid(row=3, column=1)
        Tk.Label(otherFrame, text='Fecha devolucion', fg='red').grid(row=4, column=1)

        Tk.Entry(otherFrame, textvariable=idReservaFecha).grid(row=1, column=2)
        Tk.Entry(otherFrame, textvariable=idClienteFecha).grid(row=2, column=2)
        Tk.Entry(otherFrame, textvariable=fechaInicio).grid(row=3, column=2)
        Tk.Entry(otherFrame, textvariable=fechaFinal).grid(row=4, column=2)

        handler = lambda: self.onCloseOtherFrame(otherFrame)
        Tk.Button(otherFrame, text="Cerrar", command=handler).grid(row=7, column=3)
        Tk.Button(otherFrame, text="Guardar", command = partial(self.crearFecha,idClienteFecha,idReservaFecha,fechaInicio,fechaFinal)).grid(row=7,column=2)


    def Adminreserva(self):
        self.hide()
        otherFrame = Tk.Toplevel()
        otherFrame.title("Reservas")
        global idReserva,precio

        Tk.Label(otherFrame, text='Ingrese los datos de la reserva', fg='red').grid(row=1, column=1)
        Tk.Label(otherFrame, text='ID reserva', fg='red').grid(row=2, column=0)
        Tk.Label(otherFrame, text='precio', fg='red').grid(row=3, column=0)

        Tk.Entry(otherFrame, textvariable=idReserva).grid(row=2, column=1)
        Tk.Entry(otherFrame, textvariable=precio).grid(row=3, column=1)

        Tk.Button(otherFrame, text="Crear",command=partial(self.crearReserva,idReserva,precio)).grid(row=4, column=0)
        Tk.Button(otherFrame, text="Leer",command=partial(self.leerReserva,idReserva,precio)).grid(row=4, column=1)
        Tk.Button(otherFrame, text="Actualizar",command=partial(self.actualizarReserva,idReserva,precio)).grid(row=4, column=2)
        Tk.Button(otherFrame, text="Borrar", command=partial(self.eliminarReserva,idReserva)).grid(row=5, column=1)

        handler = lambda: self.onCloseOtherFrame(otherFrame)
        Tk.Button(otherFrame, text="Cerrar", command=handler).grid(row=2, column=2)


    def Admincliente(self):
        """"""
        self.hide()
        global nomUser,apUser,dirUser,telUser,idUser
        otherFrame = Tk.Toplevel()
        otherFrame.geometry("300x230")
        otherFrame.title("Registro de clientes")
        Tk.Label(otherFrame, text='Ingrese los datos de cliente', fg='red').grid(row=1, column=1)
        Tk.Label(otherFrame, text='ID cliente', fg='red').grid(row=2, column=0)
        Tk.Label(otherFrame, text='Nombre', fg='red').grid(row=3, column=0)
        Tk.Label(otherFrame, text='Apellido', fg='red').grid(row=4, column=0)
        Tk.Label(otherFrame, text='Direccion', fg='red').grid(row=5, column=0)
        Tk.Label(otherFrame, text='Telefono', fg='red').grid(row=6, column=0)
        Tk.Entry(otherFrame, textvariable=idUser).grid(row=2, column=1)
        Tk.Entry(otherFrame, textvariable=nomUser).grid(row=3, column=1)
        Tk.Entry(otherFrame, textvariable=apUser).grid(row=4, column=1)
        Tk.Entry(otherFrame, textvariable=dirUser).grid(row=5, column=1)
        Tk.Entry(otherFrame, textvariable=telUser).grid(row=6, column=1)

        Tk.Button(otherFrame, text="Crear", command=partial(self.crear,idUser,nomUser,apUser,dirUser,telUser)).grid(row=7, column=0)
        Tk.Button(otherFrame, text="Leer", command=partial(self.leerCliente,idUser,nomUser,apUser,dirUser,telUser)).grid(row=7, column=1)
        Tk.Button(otherFrame, text="Actualizar", command=partial(self.actualizarCliente,idUser,nomUser,apUser,dirUser,telUser)).grid(row=7, column=2)
        Tk.Button(otherFrame, text="Borrar", command=partial(self.eliminarCliente,idUser)).grid(row=8, column=1)

        handler = lambda: self.onCloseOtherFrame(otherFrame)
        Tk.Button(otherFrame, text="Regresar", command=handler).grid(row=4, column=2)

        #Tk.Button(otherFrame, text="Guardar", command=partial(self.crear,idUser,nomUser,apUser,dirUser,telUser)).grid(row=7,column=2)


    def Adminfechas(self):
        self.hide()
        otherFrame = Tk.Toplevel()
        global idClienteFecha, idReservaFecha, fechaInicio, fechaFinal
        otherFrame.title("Reservas")

        Tk.Label(otherFrame, text='Ingrese los datos de las fechas', fg='red').grid(row=1, column=1)
        Tk.Label(otherFrame, text='ID reserva', fg='red').grid(row=2, column=0)
        Tk.Label(otherFrame, text='ID cliente', fg='red').grid(row=3, column=0)
        Tk.Label(otherFrame, text='Fecha entrega', fg='red').grid(row=4, column=0)
        Tk.Label(otherFrame, text='Fecha devolucion', fg='red').grid(row=5, column=0)

        Tk.Entry(otherFrame, textvariable=idReservaFecha).grid(row=2, column=1)
        Tk.Entry(otherFrame, textvariable=idClienteFecha).grid(row=3, column=1)
        Tk.Entry(otherFrame, textvariable=fechaInicio).grid(row=4, column=1)
        Tk.Entry(otherFrame, textvariable=fechaFinal).grid(row=5, column=1)

        Tk.Button(otherFrame, text="Crear", command=partial(self.crearFecha,idClienteFecha,idReservaFecha,fechaInicio,fechaFinal)).grid(row=6, column=0)
        Tk.Button(otherFrame, text="Leer").grid(row=6, column=1)
        Tk.Button(otherFrame, text="Actualizar").grid(row=6, column=2)
        Tk.Button(otherFrame, text="Borrar").grid(row=7, column=1)

        handler = lambda: self.onCloseOtherFrame(otherFrame)
        Tk.Button(otherFrame, text="Cerrar", command=handler).grid(row=3, column=2)
        #Tk.Button(otherFrame, text="Guardar", command=partial(self.crearFecha,idReservaFecha,idClienteFecha,fechaInicio,fechaFinal)).grid(row=7,column=2)

    def Adminvehiculo(self):
        self.hide()
        otherFrame = Tk.Toplevel()
        global matricula, color, marca, modelo,idReservaCoche
        otherFrame.title("Registrar Vehiculo")

        Tk.Label(otherFrame, text='Ingrese los datos de el auto', fg='red').grid(row=1, column=1)
        Tk.Label(otherFrame, text='Matricula', fg='red').grid(row=2, column=0)
        Tk.Label(otherFrame, text='modelo', fg='red').grid(row=3, column=0)
        Tk.Label(otherFrame, text='color', fg='red').grid(row=4, column=0)
        Tk.Label(otherFrame, text='marca', fg='red').grid(row=5, column=0)
        Tk.Label(otherFrame, text='id_reserva', fg='red').grid(row=6, column=0)

        Tk.Entry(otherFrame, textvariable=matricula).grid(row=2, column=1)
        Tk.Entry(otherFrame, textvariable=modelo).grid(row=3, column=1)
        Tk.Entry(otherFrame, textvariable=color).grid(row=4, column=1)
        Tk.Entry(otherFrame, textvariable=marca).grid(row=5, column=1)
        Tk.Entry(otherFrame, textvariable=idReservaCoche).grid(row=6, column=1)

        Tk.Button(otherFrame, text="Crear").grid(row=7, column=0)
        Tk.Button(otherFrame, text="Leer").grid(row=7, column=1)
        Tk.Button(otherFrame, text="Actualizar").grid(row=7, column=2)
        Tk.Button(otherFrame, text="Borrar").grid(row=8, column=1)

        handler = lambda: self.onCloseOtherFrame(otherFrame)
        Tk.Button(otherFrame, text="Cerrar", command=handler).grid(row=3, column=2)
        #Tk.Button(otherFrame, text="Guardar", command=partial(self.crearCoche,matricula,modelo,color,marca,idReservaCoche)).grid(row=7,column=2)



    # ----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()

    # ----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()


# ----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
   # root.geometry("400x300")
    idUser = Tk.StringVar()
    nomUser = Tk.StringVar()
    apUser = Tk.StringVar()
    dirUser = Tk.StringVar()
    telUser = Tk.StringVar()
    # Variables de reserva
    idReserva = Tk.StringVar()
    precio = Tk.StringVar()
    # Variables de coche
    matricula = Tk.StringVar()
    modelo = Tk.StringVar()
    color = Tk.StringVar()
    marca = Tk.StringVar()
    idReservaCoche = Tk.StringVar()
    # Variables de fecha
    idClienteFecha = Tk.StringVar()
    idReservaFecha = Tk.StringVar()
    fechaInicio = Tk.StringVar()
    fechaFinal = Tk.StringVar()

    app = MyApp(root)
    root.mainloop()