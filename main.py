import os
import time
from funciones import *
import pyperclip as pr

print("\tBienvenido a Cløudßløcks")
print("tu nube privada")
print("(Y)deseas encriptar el archivo completo con una misma clave?(menos seguridad, pero mas rapido)")
print("(N)o cada parte del archivo con una clave diferente?: ")
wish = input()
wish = str(wish)
if wish == 'Y':
    encriptar_file()
if wish == 'N':
    print("\tADVERTENCIA!!!")
    print("se copiara automaticamente al portapapeles una contraseña generada aleatoriamente.")
    print("la cual podrá decidir si usar para encriptar el archivo o no")
    print("si desea usarla para encriptar el archivo simplemente oprima Ctrl+v sobre el lugar para ingresarla")
    print("abajo aparecera la opción de guardarla en su gestor de contraseñas")
    print("ingrese 1 si quiere seguir: ")
    opcion = input()
    opcion = int(opcion)
    print(opcion)
    if opcion == 1:
        pr.paste()
        partir_encriptar()
