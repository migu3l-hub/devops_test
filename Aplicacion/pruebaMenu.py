import tkinter as tk
from tkinter import messagebox
from functools import partial



def validar():
    messagebox.showinfo("info",entrada1.get())
    if entrada1.get()=='lili':
        abrirventana2()
    else:
        messagebox.showwarning("Cuidado","Password incorrecto")


def Intento(nomUser,apUser,dirUser,telUser):
    # global nomUser
    # global apUser
    # global dirUser
    # global telUser
    print("imprimiendo datos")
    print("hola",nomUser.get(),apUser.get(),dirUser.get(),telUser.get())

def abrirventana2():
    global nomUser
    global apUser
    global dirUser
    global telUser
    otherFrame  = tk.Toplevel()
    otherFrame.geometry("280x250")
    otherFrame.title("Registro de clientes")
    etiquetaDos = tk.Label(otherFrame, text='Ingrese los datos de cliente', fg='red').grid(row=0, column=2)
    etiquetaUno = tk.Label(otherFrame, text='ID cliente', fg='red').grid(row=1, column=1)
    etiquetaDos = tk.Label(otherFrame, text='Nombre', fg='red').grid(row=2, column=1)
    etiquetaTres = tk.Label(otherFrame, text='Apellido', fg='red').grid(row=3, column=1)
    etiquetaCuatro = tk.Label(otherFrame, text='Direccion', fg='red').grid(row=4, column=1)
    etiquetaCinco = tk.Label(otherFrame, text='Telefono', fg='red').grid(row=5, column=1)
    Cajaid = tk.Entry(otherFrame, textvariable=idUser).grid(row=1, column=2)
    Cajanom = tk.Entry(otherFrame, textvariable=nomUser).grid(row=2, column=2)
    Cajaap = tk.Entry(otherFrame, textvariable=apUser).grid(row=3, column=2)
    Cajadir = tk.Entry(otherFrame, textvariable=dirUser).grid(row=4, column=2)
    Cajatel = tk.Entry(otherFrame, textvariable=telUser).grid(row=5, column=2)
    #handler = lambda: self.onCloseOtherFrame(otherFrame)
    #btn = tk.Button(otherFrame, text="Regresar", command=handler).grid(row=7, column=3)
    btn = tk.Button(otherFrame, text="Mostrar", command=partial(Intento,nomUser,apUser,dirUser,telUser)).grid(row=8, column=3)
    btn = tk.Button(otherFrame, text="Mostrarlos",command=lambda :print(nomUser.get(),apUser.get(),dirUser.get(),telUser.get())).grid(row=9,column=3)
    #btn = tk.Button(otherFrame, text="Guardar",command=partial(self.crear, "48", nomUser.get(), apUser.get(), dirUser.get(), telUser.get())).grid(row=7, column=2)


def cerrarventana():
    ventana.destroy()

ventana=tk.Tk()
ventana.title("Ventana 1")
ventana.geometry('380x300')
ventana.configure(background='dark turquoise')
idUser=tk.StringVar()
nomUser = tk.StringVar()
apUser = tk.StringVar()
dirUser = tk.StringVar()
telUser = tk.StringVar()
el=tk.Label(ventana,text="Password",bg="pink",fg="White")
el.pack(padx=5,pady=5,ipadx=5,ipady=5)
entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)
boton=tk.Button(ventana,text="Nueva Ventana", fg="blue", command=abrirventana2)
boton.pack(side=tk.TOP)
boton3=tk.Button(ventana,text="Validar password", fg="blue",command=validar)
boton3.pack(side=tk.TOP)
ventana.mainloop()




# def createNewWindow():
#
#     newWindow = tk.Toplevel(app)
#     newWindow = tk.Tk()
#     labelExample = tk.Label(newWindow, text = "New Window")
#     caja = tk.Entry(newWindow)
#     caja.pack()
#     buttonExample = tk.Button(newWindow, text = "New Window button", command=partial(hola,"hello"))
#     labelExample.pack()
#     buttonExample.pack()
#
#
# def quitar():
#     app.destroy()
#
#
# app = tk.Tk()
# buttonExample = tk.Button(app,text="Create new window",command=lambda:[createNewWindow(), quitar()])
# buttonExample.pack()
#
# app.mainloop()