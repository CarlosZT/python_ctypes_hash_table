from hash import *

#Instancia de la clase HashTable
my_table = HashTable(17)

#Inserción de 50 elementos (0 - 49)
for i in range(50):
    my_table.insert(i)

#Valor para testear la búsqueda
value = 50

#Test de búsqueda
if my_table.search(value):
    print(f'Si existe {value}')
else:
    print(f'No existe {value}')

#Impresión de los buckets de la Hash Table
my_table.show()
print('\n')





