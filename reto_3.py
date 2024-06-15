def notas(ingresa_notas):
    return[str(x) for x in ingresa_notas.split(',')]


def cuenta_notas(notas): 

    lista_notas =[] 
    n = 1
    secuencia = ""
   
    for i in range(len(notas)):
        if i !=(len(notas))-1:
            if notas[i] == notas[i+1]:
                n= n+1   
            else:
                lista_notas.append(notas[i])
                secuencia = secuencia + " " + str(n)
                n=1
        else:
            lista_notas.append(notas[i])
            secuencia = secuencia + " " + str(n) 
            return lista_notas, secuencia  
          
ingresa_notas = input("Ingrese las notas musicales separadas por coma: ").upper()

lista_notas = notas(ingresa_notas)

conteo_notas, conteo_secuencia= cuenta_notas(lista_notas)
respuesta_notas = ",".join(conteo_notas).replace(",",' ')
print(respuesta_notas )
print(conteo_secuencia)
