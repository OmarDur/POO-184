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

varNom= tk.StringVar()
lblNom= Label(pestana3, text="Nombre:").pack()
txtNom=Entry(pestana3,textvariable=varNom).pack()







panel.add(pestana1,text="Formulario de usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Actualizar Usuario")


Ventana.mainloop()