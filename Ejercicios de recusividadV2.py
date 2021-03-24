#Nombre: corriendoAEntero
#Entradas: Un numero mayor a cero
#Salidas: El numero decimal convertido en entero
#Restricciones: El numero debe ser en forma decimal

def corrimientoAEntero(num):
    if isinstance(num,float):
        if num==0:
            return 0
        else:
            return corrimientoAEnteroAux(num,0)
    else:
        return 'Error: Digite un numero en decimal mayor a cero'

def corrimientoAEnteroAux(num,potencia):
    if (num*10**potencia)%1==0:
        return potencia
    else:
        return num*(10**corrimientoAEnteroAux(num,potencia+1))
#-------------------------------------------------------------------------------------------
#Nombre: contarDigitos
#Entradas: Un numero mayor o menor a cero
#Salidas: Retorna la cantidad de digitos del numero ingresado
#Restricciones: El numero debe ser en forma decimal
def contarDigitos(num):
    if isinstance(num,float):
        if num<0:
            res= num*-1
            res=res%10**10*100000
            res=int(res)
            return contarDigitosNAux(res)
        else:
            num=num%10**10*100000
            num=int(num)
            return contarDigitosAux(num)
    else:
        return 'Error: Digite un numero en decimal'

def contarDigitosAux(num):
     if num<10:
            return 1
     elif num%10==0:
         return contarDigitosAux(num//10)
     else:
         return 1+contarDigitosAux(num//10)
    
def contarDigitosNAux(res):
     if res<10:
            return 1
     elif res%10==0:
         return contarDigitosAux(res//10)
     else:
         return 1+contarDigitosAux(res//10)

#-----------------------------------------------------------------------------------------------------------
#Nombre: indiceNumero
#Entradas: Un numero entero y un indice entero
#Salidas: Retorna un numero segun el indice ingresado
#Restricciones: Tanto el numero como el indice deben ser enteros positivos

def indiceNumero(num,indice):
    if isinstance (num,int) and (num>0):
        if isinstance(indice,int) and (indice>=0):
            return indiceNumero_Aux(num,indice)
        else:
            return 'Error: el indice debe ser un digito entero positivo'

    else:
        return 'Error: Digite un numero entero positivo mayor a cero'

def indiceNumero_Aux(num,indice):
    if indice>=0:
        num=str(num)
        return print(int(num[indice]))

#--------------------------------------------------------------------------------------------------------------
#Nombre: cortarNumero
#Entradas: Un numero y dos indices enteros
#Salidas: Retorna un nuevo numero segun sus indices
#Restricciones: Tanto el numero como los indices deben ser numero enteros positivos

def cortarNumero(num,indice1,indice2):
    if isinstance(num,int) and (num>=0):
        if isinstance(indice1,int):
            if isinstance(indice2,int):
                return cortarNumero_Aux(num,indice1,indice2)
            else:
                return 'Error: El indice 2 debe ser un numero entero positivo'
        else:
            return 'Error: El indice 1 debe ser un numero entero positivo'
    else:
        return 'Error: El numero debe ser entero positivo'

def cortarNumero_Aux(num,in1,in2):
    if in1>=0 and in2>=0:
        num=str(num)
        return print(int(num[in1])*10+(int(num[in2])))
    
