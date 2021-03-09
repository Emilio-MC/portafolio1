# Nombre: contarpares
#Entrada: Numero entero postivo mayor o igual a cero
#Salida: Cantidad de numeros pareas
#Restricciones: Escribir un numero entero positivo

def contarpares(num):
    if isinstance(num,int)and num >=0 :
        if num == 0 :
            return 1
        elif num % 2 == 0 :
            return 1+ contarpares(num//10)
        else:
            return contarpares(num//10)
    else:
        return 'Error, escriba un numero entero '
