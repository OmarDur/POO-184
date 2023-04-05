from tkinter import *
from tkinter import ttk
import tkinter as tk

Ventana= Tk()
Ventana.title("CRUD Usuarios")
Ventana.geometry("500x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)
pestana5=ttk.Frame(panel)

#Pestana1: Formulario de Usuarios
titulo= Label(pestana1,text="Registro de Usuarios",fg="Blue",font=("Modern",18) ).pack()
varNom= tk.StringVar()
lblNom= Label(pestana1, text="Nombre:").pack()
txtNom=Entry(pestana1,textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor= Label(pestana1, text="Correo:").pack()
txtCor=Entry(pestana1,textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon= Label(pestana1, text="Contraseña:").pack()
txtCon=Entry(pestana1,textvariable=varCon).pack()

btnGuardar= Button(pestana1,text="Guardar Usuario").pack()

#Pestaña2:Buscar Usuario
titulo2= Label(pestana2,text="Buscar usuario",fg="Blue",font=("Modern",18) ).pack()
varBus= tk.StringVar()
lblid= Label(pestana2, text="Identificador de usuario: ").pack()
txtid=Entry(pestana2,textvariable=varBus).pack()
btnBusqueda=Button(pestana2,text="Buscar").pack()

subBus=Label(pestana2,text="Registrado: ",fg="red",font=("Modern",15)).pack()
TextBus= tk.Text(pestana2,height=5,width=52).pack()

#Pestana: Consultar Usuarios
titulo3=Label(pestana3,text="Consultar Usuario",fg="Blue",font=("Modern",18)).pack()

def consultar_usuarios():

    pass

btnConsultar = Button(pestana3, text="Consultar", command=consultar_usuarios)
btnConsultar.pack()

treeview = ttk.Treeview(pestana3, columns=("id", "nombre", "correo"), show="headings", height=5)
treeview.heading("id", text="ID")
treeview.heading("nombre", text="Nombre")
treeview.heading("correo", text="Correo")
treeview.pack()

#Pestana de Actualizar usuarios

titulo4=Label(pestana4,text="Actualizar Usuario",fg="Blue",font=("Modern",18)).pack()

varActNom= tk.StringVar()
lblActNom= Label(pestana4, text="Nombre:").pack()
txtActNom=Entry(pestana4,textvariable=varActNom).pack()

varActCor= tk.StringVar()
lblActCor= Label(pestana4, text="Correo:").pack()
txtActCor=Entry(pestana4,textvariable=varActCor).pack()

varActCon= tk.StringVar()
lblActCon= Label(pestana4, text="Contraseña:").pack()
txtActCon=Entry(pestana4,textvariable=varActCon).pack()


btnActualizar = Button(pestana4, text="Actualizar")
btnActualizar.pack()




panel.add(pestana1,text="Formulario de usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Actualizar Usuario")
panel.add(pestana5,text="Eliminar Usuario")


Ventana.mainloop()