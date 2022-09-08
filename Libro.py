class Libro(object):
    def __init__(self, id, titulo, autor, editorial):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial

    def __str__(self):
        return "%s - %s - %s - %s" % (self.id, self.titulo, self.autor, self.editorial)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)


class LibroAdmin(object):
    def __init__(self):
        self.arregloLibros = []

    def agregar(self, id, titulo, autor, editorial):
        lib = Libro(id, titulo, autor, editorial)
        self.arregloLibros.append(lib)

    def __str__(self):
        s = ""
        for libro in self.arregloLibros:
            s += str(libro) + '\n'
        return s

    def buscar(self, clave, por="id"):
        for indice, libro in enumerate(self.arregloLibros):
            if libro.__getattribute__(por) == clave:
                return indice
            else:
                return None

    def remover(self, clave, por='id'):
        indice = self.buscar(clave)
        if indice is not None:
            self.arregloLibros.pop(indice)
        return indice


# Programa principal
arreglo = LibroAdmin()
id = input("Id: ")
titulo = input("Titulo: ")
autor = input("Autor: ")
editorial = input("Editorial: ")

arreglo.agregar(id, titulo, autor, editorial)
print("\n", arreglo)


# Buscar un elemento por su ID
buscado = input("ID del elemento a bsucar: ")
indexBuscado = arreglo.buscar(buscado)
if indexBuscado is not None:
    print("Elemento encontrado en posicion: {0}".format(indexBuscado))
else:
    print("Este ID no se encuentra en el registro.")

# Remover un elemento por ID
remover = input("ID del elemento a eliminar: ")
indexRemover = arreglo.remover(remover)
if indexRemover is not None:
    print("Elemento a remover de ls posicion: {0}".format(indexRemover))
else:
    print("Este ID no se encuentra en el registro.")


print("\n", arreglo)
