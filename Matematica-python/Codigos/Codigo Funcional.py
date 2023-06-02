import math
from tkinter import Y                           #importamos las librerias que vamos a usar
import matplotlib.pyplot as plt
import numpy as np
print("Seleccione el tipo de funcion que va a introducir a continuacion.")
print("======================")
print("1->Funcion Racional")
print("2->Funcion Irracional")
print("3->Funcion Algebraica")                  #Le pedimos al usuario que indique que funcion va a graficar
print("4->Funcion Exponencial ")
opcion = int(input("Opcion->"))
x = 0
def k (x):
        global y
        y= (2*x + 8)                            #Definimos la funcion
        return y
if opcion == 1:
        print("1 - muchos \n 2 - uno")
        des=int(input("¿Desea calcular un punto o muchos?"))    #le preguntamos si desea calcular muchos puntos o solo uno
        if des == 1:
                x = 0
                listaX=[]
                listaY=[]
                rang1= int(input("ingrese desde donde se empieza a analizar x")) #ingresa el dominio
                rang2= int(input("ingrese hasta donde se va a analizar x"))

                for j in range (rang1,rang2):
                        x = j + 1
                        listaX.append(x)                #Añadimos las x y las y a una lista para despues graficar
                        listaY.append(k(x= j + 1))
                        
                plt.plot([listaX],[listaY],'.r')        #Graficamos
                plt.show()
        elif des == 2:                                  #Si solo queire graficar un punto
                x = int(input("ingrese el valor del punto a calcular: ")) 
                k(x)
                print("x =",x,"e y es igual a",y)  #Mostramos los resultados
                plt.plot(x,y,'.r')                       #Graficamos
                plt.show()                             
elif opcion == 2:
        print("1 - muchos \n 2 - uno")
        des=int(input("¿Desea calcular un punto o muchos?"))
        if des == 1:
                x = 0
                listaX=[]
                listaY=[]
                rang1= int(input("ingrese desde donde se empieza a analizar x"))
                rang2= int(input("ingrese hasta donde se va a analizar x"))

                for j in range (rang1,rang2):
                        x = j + 1
                        listaX.append(x)
                        listaY.append(k(x= j + 1))
                        
                plt.plot([listaX],[listaY],'.r')
                plt.show()
        elif des == 2:
                x = int(input("ingrese el valor del punto a calcular: "))
                k(x)
                print("x =",x,"e y es igual a",y)
                plt.plot(x,y,'.r')
                plt.show()
elif opcion == 3:
        print("1 - muchos \n 2 - uno")
        des=int(input("¿Desea calcular un punto o muchos?"))
        if des == 1:
                x = 0
                listaX=[]
                listaY=[]
                rang1= int(input("ingrese desde donde se empieza a analizar x"))
                rang2= int(input("ingrese hasta donde se va a analizar x"))

                for j in range (rang1,rang2):
                        x = j + 1
                        listaX.append(x)
                        listaY.append(k(x= j + 1))
                        
                plt.plot([listaX],[listaY],'.r')
                plt.show()
        elif des == 2:
                x = int(input("ingrese el valor del punto a calcular: "))
                k(x)
                print("x =",x,"e y es igual a",y)
                plt.plot(x,y,'.r')
                plt.show()
elif opcion == 4:
        print("1 - muchos \n 2 - uno")
        des=int(input("¿Desea calcular un punto o muchos?"))
        if des == 1:
                x = 0
                listaX=[]
                listaY=[]
                rang1= int(input("ingrese desde donde se empieza a analizar x"))
                rang2= int(input("ingrese hasta donde se va a analizar x"))

                for j in range (rang1,rang2):
                        x = j + 1
                        listaX.append(x)
                        listaY.append(k(x= j + 1))
                        
                plt.plot([listaX],[listaY],'.r')
                plt.show()
        elif des == 2:
                x = int(input("ingrese el valor del punto a calcular: "))
                k(x)
                print("x =",x,"e y es igual a",y)
                plt.plot(x,y,'.r')
                plt.show()