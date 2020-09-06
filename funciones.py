#!/usr/bin/env python
# coding: utf-8

def Factorial(n): #Se crea una función llamada Factorial la cual servirá para calcular factoriales dado un numero n.
    
    while n != abs(int(n)):#En el caso que el numero n no sea positivo o entero se pedirá copiarlo de nuevo hasta que n sea positivo y entero
        print ("n debe ser entero positivo")#Mensaje sobre la forma que debe tener n
        n = int(float(input("ingrese un valor entero positivo al cual le quiera calcular el factorial, en el caso de no entregar un numero entero se va a tomar la parte entera del numero ingresado "))) #Se pide dar n y se entregara la parte entera del numero entregado así sea flotante, se hace de la forma anteior ya que en caso de omitir el float() el codigo no podra convertir el string en entero
    
    if n==0: # Cuando n es cero se entrega el factorial como 1
        factorial = 1
    
    else: #En el caso que el numero entregado sea diferente de cero se procede a calcular el factorial
        factorial = 1 #Se define la variable factorial como el valor 1
        for i in range(1,n): #Se inicia un ciclo el cual va desde i=0 hasta i=n-1
            factorial*= (i+1)#A la variable factorial se le va a multiplicar el valor i+1 por lo tanto factorial sera 1*2*3*...*n
            
    return factorial #al llamar a la función Factorial se entregara el valor de la variable factorial

def Binomial(n,k):#Se crea una función llamada Binomial la cual servirá para calcular los coeeficientes binomiales dado dos numeros n y k.

#####Se procede de forma analaga que se hizo con el factorial para los valores de n
    while n != abs(int(n)):
        print ("n debe ser entero positivo")
        n = int(float(input("ingrese un valor entero positivo n, en el caso de no entregar un numero entero se va a tomar la parte entera del numero ingresado")))
####################################

######De forma similar se procede con k pero el ciclo debe cumplir una condición extra la cual es que k no puede ser mayor que, entonces el ciclo se ejecutara mientras k sea un numero no entero, negativo o mayor que n
    while k != abs(int(k)) or k >n:
        print ("k debe ser entero positivo y a lo sumo igual que n")
        k = int(float(input("ingrese un valor entero positivo k que tambien sea menor o igual a n, en el caso de no entregar un numero entero se va a tomar la parte entera del numero ingresado")))
########################################################################


    return Factorial(n) / (Factorial(k) * Factorial(n - k))#Usando la formula dada en la tarea la función binomial entrega(retorna) n!/(k!(n-k)!)

def Pascal(n):#Se crea una función llamada Pascal la cual servirá para calcular los coeeficientes binomiales de forma ordenada dado un numeros n
    triangulo = open("Pascal-n.txt", "w")#Se abre/crea un archivo txt con el nombre Pascal-n en el que solo se podrá escribir y se almacenara en la variable triangulo

    for i in range(n+1):#Inicia un ciclo for que va de i=0 a i=n
        triangulo.write("n = " + str(int(i)))#se escribe en el txt n = valor de i
        
        for k in range (n+1-i,-1,-1): #Inicia un ciclo for, su uso sera por algo estetico y solo hara espacios entre el anterior escrito y lo que seguira con un espaciado n-i+1
            triangulo.write(" ")
            
        for j in range(i+1):#Inicia un ciclo for que va de j=0 a j=i
            triangulo.write(str(int(Binomial(i,j))) + " ")#Se escribe en el txt el valor del coeficiente binomial i,j precedido por un espacio

        triangulo.write("\n") #Se hace un salto de linea en el txt
    triangulo.close()#Cierra el archivo txt
    return