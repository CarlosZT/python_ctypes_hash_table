from hash import *
import timeit
import matplotlib.pyplot as plt

#Instancia de la clase HashTable
buckets = 17
my_table = HashTable(buckets)

# #Inserción de 50 elementos (0 - 49)
# for i in range(50):
#     my_table.insert(i)

# #Valor para testear la búsqueda
# value = 50

# #Test de búsqueda
# if my_table.search(value):
#     print(f'Si existe {value}')
# else:
#     print(f'No existe {value}')

# #Impresión de los buckets de la Hash Table
# my_table.show()
print('\n')
###############################################################
#load factor: a = (n/m)
#n es el numero de elementos a guardar
#m es el numero de buckets disponibles
#La complejidad esperada es O(1+a)


my_table = HashTable(17)

def multi_insert(p):
    for i in range(p):
        my_table.insert(i)

def multi_search(value):
    my_table.search(value)

def map_func(n):
    return n/buckets

# reps = 7
# for j in range(reps):
#     p = 10**j

#     for i in range(p):
#         my_table.insert(i)

#     for i in range(p):
#         my_table.search(i)
#     my_table = HashTable(17)


#Se crean variables para almacenar los datos del experimento
ins_time = []
search_time = []
ops = []
expected_ins = []
expected_srch = []

#Aqui se almacena el tiempo que dura cada ejecucion
result = 0
result_search = 0

#Repeticiones de cada medicion
reps = 10

for i in range(6):
    
    #Cantidad de operaciones a realizar (1 - 100000 de datos)
    p = 10**(i)

    for j in range(reps):
        my_table = HashTable(17)

        #Medicion de tiempo de insercion de p cantidad de datos
        result += timeit.timeit(stmt='multi_insert(p)', globals=globals(), number=1)

        #Medicion de tiempo de busqueda no exitosa de un dato (p no es un valor almacenado en la hash table)
        result_search += timeit.timeit(stmt='my_table.search(p)', globals=globals(), number=1)

    #Media de los tiempos calculados
    ins_time.append(result/reps)
    search_time.append(result_search/reps)

    ops.append(p)
    expected_ins.append(map_func(p)*5e-3)
    expected_srch.append(map_func(p)*10e-8)
    

plt.title('Work complexity')

plt.subplot(1, 2, 1)
plt.plot(ops, ins_time, 'r', label='Insertion time')
plt.plot(ops, expected_ins, 'b', label='Expected O(1 + α)')

plt.legend(loc='best')
plt.xlabel('Operations')
plt.ylabel('Time')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(ops, search_time, 'g', label='Search time')
plt.plot(ops, expected_srch, 'b', label='Expected O(1 + α)')

plt.legend(loc='best')
plt.xlabel('Operations')
plt.ylabel('Time')
plt.grid(True)
plt.show()








