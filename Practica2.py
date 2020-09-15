##################Practica Nº2: Estructura Condicionales##############
#1.Ingrese un tiempo X que esta repesentado en segundos,luego ingrese el tiempo que tomara en realizar una tarea Z representado en segundos, minutos y horas. Se pide verificar si con el tiempo X se puede finalizar la tarea Z.
'''x=int(input("Ingrese el tiempo en segundos \n"))
z=int(input("Ingrese el tiempo que tomara en realizar una tarea \n"))
un=str(input("Ingrese la unidad el tiempo (seg,min y hrs)\n"))
if un == 'hrs':
    chs=z*3600
    print("Hora en segundos \t",chs,"segundos")
    if x==chs:
         print("el tiempo es suficiente \t", x)
    else:
         print("el tiempo no es suficiente \t", chs)
elif un =='min':
    cms=z*60
    print("Minutos en segundos \t",cms,"segundos")
    if x==cms:
         print("el tiempo es suficiente \t", x)
    else:
         print("el tiempo no es suficiente \t", cms )
elif un == 'seg':
    print("es ta en segundos \t",un) 
    if x==z:
         print("el tiempo es suficiente \t", x)
    else:
         print("el tiempo no es suficiente \t", z)'''

#2. Utilizando los coeficientes (a,b,c) de una ecuacion de 2do grado se pide mostrar la naturaleza de sus raices.
#ecuacion de 2do grado:ax^2 + bx + c=0
# D=b^2-4ac
'''a=int(input("ingrese un numero para a:\n"))
b=int(input("ingrese un numero para b:\n"))
c=int(input("ingrese un numero para c:\n"))

D=(b)*(b)-4*(a)*(b)
if D>0:
     print("las raices de la ecuacion son reales y diferentes\t:", D)
elif D==0:
     print("las raices de la ecuacion son reales e diferentes\t:", D)
elif D<0:
     print("las raices de la ecuacion son complejas\t:", D)'''
#3. Dados 3 valores (Horas, minutos y segundos ) se pide sumar un segundo.
hrs=int(input("Ingrese las horas:\t"))
min=int(input("Ingrese los minutos:\t"))
seg=int(input("Ingrese los segundos:\t"))
seg2=int(input("Ingrese los segundos2:\t"))
suma=seg+seg2
if suma>59:
     a=suma//60
     suma=suma%60
     min=min+a
if min>59:
     b=min//60
     min=min%60
     hrs=hrs+b
if hrs>23:
     hrs=hrs%24  
print("La hora es:\t",format(hrs,'02'),':',format(min,'02'),':',format(suma,'2'))
            