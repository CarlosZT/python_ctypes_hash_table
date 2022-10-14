from list import *

#Clase para implementar la HashTable

class HashTable():
    def __init__(self, size) -> None:
        self.size = size 

        #Se crea la hash table (un array de listas enlazadas)
        d = []*(self.size)
        self.ht = (List * self.size)(*d)

        #Ruta para localizar el hash_table.so Cambiarlo si no te localiza el archivo
        path = (os.getcwd() + "\\Hash Tables\\hash_table.so").replace('\\', '/')

        #Se carga el código compilado
        self.libc = CDLL(path)

        #Definición de métodos disponibles en el código C (Argumentos y Return's)
        self.libc.init_hash_table.argtypes = [POINTER(List), c_int]
        self.libc.show.argtypes = [POINTER(List), c_int]
        self.libc.insert.argtypes = [POINTER(List), c_int]

        self.libc.hash_func.argtypes = [c_int, c_int]
        self.libc.hash_func.restype = c_int

        self.libc.search.argtypes = [POINTER(List), c_int, c_int]
        self.libc.search.restype = c_int

        self.libc.init_hash_table(self.ht, c_int(self.size))

    #Función de insercion
    def insert(self, value):
        self.libc.insert(self.ht[self.libc.hash_func(c_int(value), c_int(self.size))], value, c_int(self.size))

    #Función de búsqueda
    def search(self, value):
        return self.libc.search(self.ht, c_int(value), c_int(self.size))==1

    #Función para mostsrar los buckets y su contenido
    def show(self):
        self.libc.show(self.ht, c_int(self.size))