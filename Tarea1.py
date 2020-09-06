#!/usr/bin/env python
# coding: utf-8

import funciones

def P(n,k):#Se define una función la cual calcula la probabilidad de obtener k veces un resultado al lanzar una moneda(cara o sello) al realizarlo n veces 
    return funciones.Binomial(n,k)/(2**n)#Se emplea la formula dada para retornar la probabilidad de obtener un resultado k veces después hacer n experimentos

"la probabilidad de que si se hace este experimento 100 veces, el resultado sean 10 veces cara."

P10 = P(100,10)#Usando la función definida anteriormente se usa n=100 y k=10 para hallar el resultado de la probabilidad de que salga cara 10 veces si se lanza la moneda 100 veces

print("la probabilidad de que si se hace este experimento 100 veces, el resultado sean 10 veces cara = ",P10)

"la probabilidad de que caiga cara más de 30 veces."

Pmas30=0 #Se define la variable Pmas30 como el valor cero

#Para hallar la probabilidad de que caigan más de 30 caras se deben sumar la todasprobabilidadesde de que caiga cara 31 veces hasta 100 veces, para ello se usara un ciclo for que hara la suma desde P(100,31) hasta P(100,100)

for i in range(31,101): #Se inicia un ciclo for qe va desde i=31 hasta i=100
    Pmas30 +=P(100,i)#A la variable Pmas30 se le suma la probabilidad de que en 100 lanzamientos se obtengan i caras

print("la probabilidad de que caiga cara más de 30 veces. = ",Pmas30)