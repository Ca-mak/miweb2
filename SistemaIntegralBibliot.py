
#Este es un comentario exclusivamente para ver los cambio que se generan en Git ;)

class Libro(object):

    def __init__(self, id, titulo, actor, editorial):
        self.id = id
        self.titulo = titulo
        self.actor = actor
        self.editorial = editorial


    def __str__(self):
        return("%s-%s-%s-%s" % (self.id, self.titulo, self.actor, self.editorial))

    
    def __getattribute__(self, atrib):
        return object.__getattribute__(self, atrib)
        

class LibroAdmin:

    def __init__(self): #Constructor
        self.arrgLibros = [] #Se creo una lista vacia

    def agregar(self, id, tit, aut, edit):
        lib = Libro(id, tit, aut, edit) #Este es un objeto temporal

        self.arrgLibros.append(lib) #Agrega los argumentos a lib

    def __str__(self):
        s = "" #Se define una salida vacia

        for libro in self.arrgLibros:
            s+= str(libro) + "\n"
        return s

    def buscar(self, clave, por="id"): #Este es un arreglo enumerado o enumerate

        for indice, libro in enumerate(self.arrgLibros):
            if libro.__getattribute__(por) == clave:
                return indice

    def remover(self, clave, por="id"):
        
        indice = self.buscar(clave)

        if indice != None:
            self.arrgLibros.pop(indice) #Retira el elemento que esta en la posicion indice
            return indice

#PPROGRAMA PRINCIPAL
arreglo = LibroAdmin()

def main():

    arreglo = LibroAdmin()
    id = input("id: ")
    tit = input("titulo: ")
    aut = input("autor: ")
    edit = input("editorial: ")

    arreglo.agregar(id, tit, aut, edit)

    print("\n", arreglo)


def insertar():

    opc = 's'

    while opc == 's':
        id = input("id: ")
        tit = input("titulo: ")
        aut = input("autor: ")
        edit = input("editorial: ")

        arreglo.agregar(id, tit, aut, edit)
        break

            
def mostrar():

    print(arreglo)
    input("presiona algo apra continuar")
    


def busquars(busquedo):
    if (arreglo.buscar(busquedo)) != None:
        print("Elemento encontrado en la posicion {0}".format(arreglo.buscar(busquedo)))
    else:
        print("No existe el elemento")

def menu():



    ount = 1


    print("-----Sistema Integra de Biblioteca-----\nMenú Principal")
    print("[1] Agregar Libros\n[2] Eliminar Libros\n[3] Buscar Libros\n[4] Mostrar Libros\n[5] Salir\n")

    choice = input("Selecciona una opcion: ")

    choice = int(choice)
    control = True

    its = 0


    
    if(choice == 1):
                checks = True
                print("Escribe los datos de los libros que quieras agregar:\n ")
                insertar()

                while checks == True:

                    print("¿deseas agregar mas?")
                    opcion = input("[y,n]   ")

                    if opcion == "y":
                        checks = True
                        insertar()
                    elif opcion == "n":
                        checks = False
                        print("listo")                
                
                
    elif(choice == 2):
                print("Escribe el indice del libro que quieres elimninar:")
                eliminar()
    elif(choice == 3):
                print("Escribe el ID del libro que quieras buscar:")
                algo = input("aqui:   ")
                busquars(algo)
    elif(choice == 4):
                print("Mostrando Libros...")
                mostrar()
    elif(choice == 5):
                print("Hasta luego!")



if __name__ == "__main__":
    menu()
    print("¿Deseas hacer algo más?")
    dato = input("[y,n]   ")    

    if dato == "y":
        menu()
    elif dato == "n":
        print("Hasta luego!")
    
            
        
                

    