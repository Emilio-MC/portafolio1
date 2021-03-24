#Nombre: divisores
#Entradas: Un numero entero
#Salidas: La cantidad de divisores del numero
#Restricciones: El numero tiene que ser entero positivo mayor a cero

def divisores(num):
    if isinstance(num,int) and (num>0):
        return divisoresAux(num,num)
    else:
        return "El número debe ser positivo mayor a cero"

def divisoresAux(num,divisores):
    if divisores==0:
        return 0
    else:
        if num%divisores==0:
            print (divisores)
        return divisoresAux(num,divisores-1)

#------------------------------------------------------------------------------------------------------
#Nombre: multiplicarRecursivo
#Entradas: Dos numero 
#Salidas: El resultado de la multiplicacion
#Restricciones: Ambos numeros deben ser enteros positivos

def multiplicarRecursivo(num,factor):
    if isinstance(num,int) and isinstance(factor,int):
        return multiplicarRecursivoAux(num,factor)
    else:
        return print ("Ambos números debe ser un enteros positivos")

def multiplicarRecursivoAux(num,factor):
    if factor==0:
        return 0
    else:
        return num+multiplicarRecursivoAux(num,factor-1)
#--------------------------------------------------------------------------------------------------------
#Nombre: divisionRecursivo
#Entradas: Dos numeros
#Salidas: El resultado de la multiplicacion
#Restricciones: Los numeros deben ser enteros positivos
def divisionRecursivo(divisor,dividendo):
    if(isinstance(divisor,int) and isinstance(dividendo,int)):
        return divisionRecursivoAux(divisor,dividendo,0)
    else:
        return ("Ambos numeros deben ser enteros positivos")

def divisionRecursivoAux(divisor,dividendo,potencia):
    if(potencia>divisor):
        return 0
    else:
        return 1+divisionRecursivoAux(divisor,dividendo,potencia+divisor)

    
    
    

