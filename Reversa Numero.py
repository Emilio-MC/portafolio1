"""
Entrada:
    Un numero entero mayor o igual a 0
Salida:
    La cantidad de digitos del numero
Restricciones:
    Tiene que ser un numero entero positivo mayor o igual a 0
"""
def CantidadDigitos(num):
    if (isinstance (num,int) and num >=0):
        if (num<10):
            return 1
        else:
            return 1+CantidadDigitos(num//10)
    else:
        print ('Error, digite un numero entero positivo')
#-----------------------------------------------------------------------------------------------------------------------

#Nombre: reversaNumero
#Entradas: Numero entero positivo mayor o igual a cero
#Salidas: Entero  mayor a cero que el numero este en orden inversa a su representacion origianal 
#Restricciones: Entero posito mayor o igual a cero
def reversaNum(num):
    if isinstance (num,int):
        if (num>= 0):
            if (num<= 10):
                return num
            else:
                return reversaNum_aux(num,CantidadDigitos(num))
        else:
            print ('El numero debe ser positivo')
    else:
        print ('Error: el numero no es entero')

def reversaNum_aux(num,largo):
    if largo == 0 :
        return 0
    else:
        return (num%10)*(10**(largo-1))+reversaNum_aux(num//10, largo-1)

