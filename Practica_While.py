#Ejercicio 2.
#Calcular el factorial de un numero natural utilizando la estructura while y sin utilizar ninguna librería ni el operador
#de multiplicación *
#n!=(n*n-1)!
# 
fac=1
ct=0
n=int(input("Introdusca un numero: "))
while(n>0):
    ct=ct+1
    fac=fac*ct
    n=n-1
print("El factorial es: ",fac)