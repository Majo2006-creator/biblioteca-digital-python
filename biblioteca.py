"""
Sistema de Gestión de Biblioteca Digital
Autor: Maria Torres
Descripción:
Este programa permite gestionar libros, usuarios y préstamos en una biblioteca digital.
"""

# ==============================
# Clase Libro
# ==============================

class Libro:
    """
    Representa un libro dentro de la biblioteca
    """

    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para almacenar datos inmutables
        self.datos = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True

    def titulo(self):
        return self.datos[0]

    def autor(self):
        return self.datos[1]

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo()} - {self.autor()} | {self.categoria} | ISBN:{self.isbn} | {estado}"


# ==============================
# Clase Usuario
# ==============================

class Usuario:
    """
    Representa un usuario registrado en la biblioteca
    """

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista de libros prestados
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def mostrar_libros(self):
        print(f"\nLibros prestados a {self.nombre}:")
        if len(self.libros_prestados) == 0:
            print("No tiene libros prestados")
        else:
            for libro in self.libros_prestados:
                print(libro)


# ==============================
# Clase Biblioteca
# ==============================

class Biblioteca:
    """
    Gestiona los libros, usuarios y préstamos
    """

    def __init__(self):
        # Diccionario ISBN -> Libro
        self.libros = {}

        # Diccionario ID -> Usuario
        self.usuarios = {}

        # Conjunto para IDs únicos
        self.ids = set()

    # Añadir libro
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print("Libro agregado correctamente")
        else:
            print("El libro ya existe")

    # Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado")
        else:
            print("Libro no encontrado")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids:
            self.ids.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print("Usuario registrado")
        else:
            print("ID de usuario ya existe")

    # Eliminar usuario
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.ids:
            self.ids.remove(id_usuario)
            del self.usuarios[id_usuario]
            print("Usuario eliminado")
        else:
            print("Usuario no encontrado")

    # Prestar libro
    def prestar_libro(self, isbn, id_usuario):

        if isbn not in self.libros:
            print("Libro no existe")
            return

        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return

        libro = self.libros[isbn]

        if libro.disponible:
            usuario = self.usuarios[id_usuario]
            usuario.prestar_libro(libro)
            libro.disponible = False
            print("Libro prestado correctamente")
        else:
            print("Libro no disponible")

    # Devolver libro
    def devolver_libro(self, isbn, id_usuario):

        if isbn in self.libros and id_usuario in self.usuarios:

            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            usuario.devolver_libro(libro)
            libro.disponible = True

            print("Libro devuelto")

    # Buscar libros
    def buscar_libros(self, tipo, valor):

        print("\nResultados de búsqueda:\n")

        for libro in self.libros.values():

            if tipo == "titulo" and libro.titulo().lower() == valor.lower():
                print(libro)

            elif tipo == "autor" and libro.autor().lower() == valor.lower():
                print(libro)

            elif tipo == "categoria" and libro.categoria.lower() == valor.lower():
                print(libro)


# ==============================
# Ejemplo de uso del sistema
# ==============================

def ejemplo():

    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "001")
    libro2 = Libro("Don Quijote", "Miguel de Cervantes", "Novela", "002")
    libro3 = Libro("Python para Principiantes", "Juan Pérez", "Programación", "003")

    # Añadir libros
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    # Crear usuarios
    usuario1 = Usuario("Ana", 1)
    usuario2 = Usuario("Carlos", 2)

    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("001", 1)
    biblioteca.prestar_libro("002", 2)

    # Mostrar libros prestados
    usuario1.mostrar_libros()
    usuario2.mostrar_libros()

    # Devolver libro
    biblioteca.devolver_libro("001", 1)

    # Buscar libro por autor
    biblioteca.buscar_libros("autor", "Miguel de Cervantes")


# Ejecutar ejemplo
if __name__ == "__main__":
    ejemplo()
