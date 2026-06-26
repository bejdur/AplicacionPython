import requests

def valor_dolar():
    url= "https://mindicador.cl/api/dolar"
    respuesta= requests.get(url)
    recibido= respuesta.json()
    dolar_actual= recibido["serie"][0]["valor"]
    return dolar_actual
def ingresar_producto(lista,nombre,categoria,precio):
    dolar= valor_dolar()
    preusd= round(precio/dolar)
    producto= { "nombre": nombre,
               "categoria": categoria,
               "precio clp": precio,
               "precio usd": preusd} 
    lista.append(producto)
    return lista