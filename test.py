#!/usr/bin/env python
# coding: utf-8

import funciones #Se importa el modulo con las funciones creadas, dicho modulo debe encontrarse en la misma carpeta que se trabaja.

print(funciones.Factorial(-4)) #Se imprime la función Factorial en un numero negativo para observar que no es posible usarla, cuando se ingresan numero negativos se volverá a pedir que ingrese un numero hasta que sea posible tomar el factorial de dicho numero, por conveniencia se hizo que la ingresar un numero no entero se convirtiera en un entero.

print(funciones.Binomial(-25,-30))#Se imprime la función Binomial en un par de números negativos para observar que no es posible usarla,se pedirá primero ingresar el primer numero de la función y el procedimiento será análogo a la función anterior, cuando se ingrese un numero valido pasara similar con el segundo numero pero se añade la condición que este sea menor que el anterior digitado.

"""En las siguientes lineas se va a imprimir valores conocidos las funciones por si en el caso anterior se ingresaron valores no conocidos"""

print(funciones.Factorial(4))

print(funciones.Binomial(5,2))
########################################

funciones.Pascal(5) #se procede obtener los primeros 6 elementos del triangulo de Pascal donde el resultado se observara en el archivo txt que se generara en la misma carpeta que incluya este archivo 