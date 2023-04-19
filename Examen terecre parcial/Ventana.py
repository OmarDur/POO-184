from tkinter import *
from tkinter import ttk
import tkinter as tk

Ventana= Tk()
Ventana.title("CRUD Ferreteria")
Ventana.geometry("500x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)



#Pestana1: Insertar materiales
titulo= Label(pestana1,text="Insertar materiales",fg="Blue",font=("Modern",18) ).pack()
varNom= tk.StringVar()
lblNom= Label(pestana1, text="Nombre del material:").pack()
txtNom=Entry(pestana1,textvariable=varNom).pack()


varCat= tk.StringVar()
lblCat= Label(pestana1, text="Cantidad").pack()
txtCat=Entry(pestana1,textvariable=varCat).pack()

btnGuardar= Button(pestana1,text="Guardar",command=guardarMaterial).pack()

#Pestaña2:
titulo2= Label(pestana2,text="Buscar usuario",fg="Blue",font=("Modern",18) ).pack()
varBus= tk.StringVar()
lblid= Label(pestana2, text="actualizar: ").pack()
txtid=Entry(pestana2,textvariable=varBus).pack()
btnBusqueda= Button(pestana2,text="Buscar",command=actualizarmaterial).pack()

subBus=Label(pestana2,text="Registrado: ",fg="red",font=("Modern",15)).pack()
TextBus= tk.Text(pestana2,height=5,width=52).pack()

#Pestana: Actualizar Materiales
titulo3=Label(pestana3,text="Actualizar Materiales",fg="Blue",font=("Modern",18)).pack()



btnConsultar = Button(pestana3, text="Consultar", command=actualizarmateriales)
btnConsultar.pack()

treeview = ttk.Treeview(pestana3, columns=("IDMaterial", "Material", "Cantidad"), show="headings", height=5)
treeview.heading("id", text="ID")
treeview.heading("Material", text="Material")
treeview.heading("Cantidad", text="Cantidad")
treeview.pack()




panel.add(pestana1,text="Insertar Material")
panel.add(pestana2,text="Buscar Material")
panel.add(pestana3,text="Consultar Materiales")



Ventana.mainloop()