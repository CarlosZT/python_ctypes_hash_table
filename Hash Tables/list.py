from ctypes import CDLL, POINTER, Structure, c_int
import os

#Estructuras para referenciar los custom types en el código de C
# List representa las listas enlazadas y Node cada uno de los elementos que las conforman 

class Node(Structure):
    pass
Node._fields_=[('next', POINTER(Node)),('value', c_int)]

class List(Structure):
    _fields_=[('head', POINTER(Node))]

