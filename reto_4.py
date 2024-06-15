import json

tienda_online = str(input('Ingresa el diccionario del stock de laminas de la tienda: '))
data = json.loads(tienda_online)

laminas_compradas = []

laminas =str(input('Ingresa los códigos de las laminas que quieres comprar: ')).split(' ')
precio_total= 0

for i in laminas:
    if i in data.keys():
        precio_total+= data[i]
        laminas_compradas.append(i)
        
laminas_totales = ",".join(laminas_compradas).replace(",",' ')

print( precio_total)

print(laminas_totales)
