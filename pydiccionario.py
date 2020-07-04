#! /usr/bin/python
# -*- coding: utf-8 -*-
#Código de libre distibución y modificación. Si es modificado favor evitar referencias.
#https://github.com/J0seca


import os
from random import randint

#Lista de caracteres a usar:
caracteres = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

print("Creador de diccionario con contraseñas al azar.\n\nLos carácteres definidos a utilizar son:")
print(caracteres)
print("------------------")
l_caract = len(caracteres) #Largo de lista de caracteres
l_pass = input("Caracteres totales contraseña: ") #total de caracteres por contrasena
total_pass = input("Total de contraseñas a generar: ") #total de contrasenas a generar

#Verificamos si archivo existe:
if(not os.path.isfile('diccionario.txt')):
 print('Archivo diccionario.txt no existe. Creando archivo!')
 d = open('diccionario.txt',"w") #creando archivo
 d.close()

else:
 #Si archivo existe se crea un respaldo en una lista
 diccionario = open("diccionario.txt","r")
 diccionario_lineas = diccionario.readlines()
 diccionario.close()


diccionario = open("diccionario.txt","w")


def copia_respaldo():
 if(diccionario_lineas):
  print("\n\nArchivo original con " + str(len(diccionario_lineas)) + " contraseñas guardadas.")
  print("Creando respaldo...")
  print("------------------")

  for i in range(0, len(diccionario_lineas)):
   diccionario.write(diccionario_lineas[i])

 else:
  print("No hay respaldo en archivo original. Continuando con operación ...")
  print("------------------")

copia_respaldo()

#Creando contrasena
print("Iniciando proceso de creación de contraseñas ...")
e = 0
while e <= (total_pass - 1):
 i = 0
 password = ""

 while i <= (l_pass - 1):
  password += caracteres[randint(0, l_caract - 1)] #agregando caracteres
  i += 1

 password += '\n' #agregamos salto de linea
 diccionario.write(password) #agregamos contrasena a archivo
 e += 1

diccionario.close()
diccionario = open("diccionario.txt","r") #Ineficiente pero lo abrimos para saber total de contrasenas con readlines
print("------------------")
print("Proceso de creación de contraseñas terminado!")
print("------------------")
print("Se creó un total de " + str(e) + " contraseñas. Contraseñas totales en archivo: " + str(len(diccionario.readlines())) )
print("------------------")
diccionario.close()
