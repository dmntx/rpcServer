# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 19:51:38 2023

@author: Juan Bernal Martinez
"""

import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://192.168.56.12:8000')
#print(s.division(3,5))


n1 = float(input("Introduce tu primer número: ") )
n2 = float(input("Introduce tu segundo número: ") )

opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los dos números
    5) Raiz cuadrada del primer número
    6) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de",n1,"+",n2,"es igual a",s.suma(n1,n2))
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de",n1,"-",n2,"es igual a",s.resta(n1,n2))
    elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto de",n1,"*",n2,"es igual a",s.multiplicacion(n1,n2))
    elif opcion == 4:
        print(" ")
        print("RESULTADO: La division de",n1,"/",n2,"es igual a",s.division(n1,n2))
    elif opcion == 5:
        print(" ")
        print("RESULTADO: La raiz cuadrada de ",n1, "es igual a",s.raiz(n1))
    else:
        print("Opción incorrecta")

#print(s.system.listMethods())