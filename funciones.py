#hecho por laboratorios papo
#este archivo contiene las funciones que se usarán en lo que a interaccion con el cliente se refiere
import os
import numpy as np
from os import walk
from time import *
import pyperclip as pr
from random import choice

def partir_encriptar():
#-----aqui hay que saber cual es el nombre del archivo que se va a operar---#
    fijo = ''
    ruta = '.'
    dir, subdirs, archivos = next(walk(ruta))
    print("Actual: ", dir)
    print("Subdirectorios: ", subdirs)
    print("Archivos: ", archivos)
    for i in range(3):
        temporal = archivos[i]
        print(temporal)
        if temporal != 'funciones.py':
            if temporal != 'main.py':
                fijo = temporal
                print(fijo)
    umbral1 = 1000000
    sizefile = os.stat(fijo).st_size
    tamaño_file = sizefile / 25
    print(tamaño_file)
    archivo = fijo
    print(type(fijo))
    largo = len(fijo)
    print(largo)
    fijo2 = list(fijo)
    print(fijo2)
    if tamaño_file < 1000:
        print("archivo muy pequeño :(")

    tamaño_file = tamaño_file / 1000
    tamaño_file = int(tamaño_file)
    tamaño_file = str(tamaño_file)
    print(tamaño_file)
    var, var2 = 0, 0
    var, var2 = str(), str()
#-------------aqui vemos el nombre del archivo sin formato--------------#
    for i in range(largo):
        if fijo2[i] != '.':
            var2 += fijo2[i]
            print(var2)
        else:
            print("hasta aca llegamos")
            break
    print(var2)
    split = 'split '+archivo+' -b '+tamaño_file+'KB '+var2
    print(split)
#-----aqui vemos el nombre del archivo sin el punto y luego se convierte en una carpeta----------#
    for i in range(largo):
        if fijo2[i] != '.':
            var += fijo2[i]
            print(var)
        else:
            print("ja lo encontre")
    print(var)
    os.system('date') 
    os.system('ls')
    os.system(split)
    os.system('ls')
    lista = (['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    cantidad = 26
    longitud = 16
    valores = "1234567890qwertyuiopasdfghjklñzxcvbnm,.-{}'¿|<>ZXCVBNM;:_][ÑLKJHGFDSAQWERTYUIOP*¡?=)(/&%$#!@ł€¶ŧ←↓→øþ~łĸŋđðßæ«»¢“”nµ"
    print("si")
#-------aqui ocurre la magia, se encriptan todas las partes----------#
    for i in range(cantidad):
        p = ""
        p = p.join([choice(valores) for i in range(longitud)])
        pr.copy(p)
        print(p)
        t = 2 
        name_file = var2+ 'a' + lista[i]
        final = 'gpg -c '+ name_file
        final = str(final)
        print(final)
        os.system(final)
#--------aqui se guardan en la carpeta--------#
    folder = 'mkdir '+var
    folder2 = var+'/'
    print(folder)
    os.system(folder)
    for i in range(cantidad):
        name_file = var2 + 'a' + lista[i] + '.gpg'
        final = 'mv '+name_file+' '+folder2
        final = str(final)
        os.system(final)
    name2_file = var2 + 'a*'
    final = 'rm ' + name2_file
    final = str(final)
    os.system(final)
#-------se acaba la funcion////___:)------#
#_____
#|     |     |----| |     | |--\  |---  |
#|     |     |    | |     | |   \ |   | |
#|     |     |    | |     | |   / |---  |
#----- |____ |----| |_____| |__/  |___| |___
#----funcion para encriptar el archivo completo, no por separado---------#
def encriptar_file():
    fijo = ''
    ruta = '.'
    dir, subdirs, archivos = next(walk(ruta))
    print("Actual: ", dir)
    print("Subdirectorios: ", subdirs)
    print("Archivos: ", archivos)
    for i in range(3):
        temporal = archivos[i]
        print(temporal)
        if temporal != 'funciones.py':
            if temporal != 'main.py':
                fijo = temporal
                print(fijo)
    sizefile = os.stat(fijo).st_size
    largo = len(fijo)
    var, fijo2 = 0, fijo
    var = str()
    for i in range(largo):
        if fijo2[i] != '.':
            var += fijo2[i]
            print(var)
        else:
            print("ja lo encontre")
    print(var)
#-------aqui ocurre la magia, se encripta----------#
    longitud = 16
    valores = "1234567890qwertyuiopasdfghjklñzxcvbnm,.-{}'¿|<>ZXCVBNM;:_][ÑLKJHGFDSAQWERTYUIOP*¡?=)(/&%$#!@ł€¶ŧ←↓→øþ~łĸŋđðßæ«»¢“”nµ"
    print("si")
    p = ""
    p = p.join([choice(valores) for i in range(longitud)])
    pr.copy(p)
    print(p)
    t = 2
    name_file = fijo
    final = 'gpg -c '+ name_file
    final = str(final)
    print(final)
    os.system(final)
    folder = 'mkdir '+var
    folder2 = var+'/'
    print(folder)
    os.system(folder)
    name_file = fijo+'.gpg'
    final = 'mv '+name_file+' '+folder2
    final = str(final)
    os.system(final)
