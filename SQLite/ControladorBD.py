import sqlite3
from tkinter import messagebox
import bcrypt


class ControladorBD:

    def _init_(self):
        pass

    def conexionBD(self):

        try:
            conexion = sqlite3.connect("basepoo.db")
            print("Conectado a la base de datos")
            return conexion

        except sqlite3.Error as error:
            print("No se pudo conectar:", error)

    def guardarUsuario(self, nombre, correo, contrasena):

        conexion = self.conexionBD()

        if nombre == "" or correo == "" or contrasena == "":
            messagebox.showwarning("Atención", "Revisa tu formulario, hay campos vacíos.")
        else:
            cursor = conexion.cursor()

            # Encripta la contraseña antes de guardarla en la BD
            contrasena_hash = self.encriptarContrasena(contrasena)

            datos = (nombre, correo, contrasena_hash)
            query = "INSERT INTO usuarios(nombre, correo, contrasena) VALUES (?, ?, ?)"

            cursor.execute(query, datos)
            conexion.commit()
            conexion.close()

            messagebox.showinfo("Éxito", "Se guardó el usuario correctamente.")

    def encriptarContrasena(self, contrasena):
        #Devuelve la contraseña encriptada con salt.
        contrasena_bytes = contrasena.encode()
        salt = bcrypt.gensalt()
        contrasena_hash = bcrypt.hashpw(contrasena_bytes, salt)
        return contrasena_hash

    def consultarUsuario(self, id):
        #Devuelve una lista con la información del usuario correspondiente al ID indicado.
        conexion = self.conexionBD()

        if id == "":
            messagebox.showwarning("Atención", "Ingresa un ID válido.")
        else:
            cursor = conexion.cursor()
            query = "SELECT * FROM usuarios WHERE id = ?"
            datos = (id,)

            cursor.execute(query, datos)
            usuario = cursor.fetchone()

            conexion.close()

            if usuario is None:
                messagebox.showwarning("Atención", "No se encontró ningún usuario con ese ID.")
            else:
                return usuario

    def obtenerUsuarios(self):
        #Devuelve una lista con todos los usuarios de la tabla usuarios.
        conexion = self.conexionBD()
        cursor = conexion.cursor()

        query = "SELECT * FROM usuarios"
        cursor.execute(query)

        usuarios = cursor.fetchall()
        conexion.close()

        def agregarUsuario(self, nombre, correo, contrasena):
            conexion = self.conexionBD()

            if nombre == "" or correo == "" or contrasena == "":
                messagebox.showwarning("Atención", "Revisa tu formulario, hay campos vacíos.")
            else:
                cursor = conexion.cursor()

                # Encripta la contraseña antes de guardarla en la BD
                contrasena_hash = self.encriptarContrasena(contrasena)

                datos = (nombre, correo, contrasena_hash)
                query = "INSERT INTO usuarios(nombre, correo, contrasena) VALUES (?, ?, ?)"

                cursor.execute(query, datos)
                conexion.commit()
                conexion.close()

                messagebox.showinfo("Éxito", "Se guardó el usuario correctamente.")

        def eliminarUsuario(self, id):
            conexion = self.conexionBD()

            if id == "":
                messagebox.showwarning("Atención", "Ingresa un ID válido.")
            else:
                cursor = conexion.cursor()
                query = "DELETE FROM usuarios WHERE id = ?"
                datos = (id,)

                cursor.execute(query, datos)
                conexion.commit()

                if cursor.rowcount == 0:
                    messagebox.showwarning("Atención", "No se encontró ningún usuario con ese ID.")
                else:
                    messagebox.showinfo("Éxito", "Se eliminó el usuario correctamente.")

            conexion.close()

        return usuarios