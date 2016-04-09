# -*- coding: utf-8 -*-
# Monstrando números pares com uma iteração
numeros = range(10)
pares =[]
for numero in numeros:
    if not numero % 2:
        pares.append(numero)

print pares
