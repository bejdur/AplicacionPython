from funcproducto import *
from funcarchivos import *
from eliminarregistro import *

def main():
    prodregistrados=[]
    while True:
        print("\nMENU DE REGISTRAR COMPRAS\n1-Añadir artículo\n2-Ver productos registrados\n3-Eliminar artículo\n4-Continuar sesión previa\n5-Salir y guardar datos\n")
        try:
         opc= int(input("Ingresa una opción: "))
         if opc==1:
            print("Añadir articulo")
            nomb= input("Ingresa nombre del producto a registrar: ")
            cat= input("Ingresa categoría del producto a registrar: ")
            preclp= int(input("Ingresa precio en CLP del artículo a registrar: "))
            prodregistrados= ingresar_producto(prodregistrados,nomb,cat,preclp)

         elif opc==2:
            if prodregistrados == []:
               print("No hay artículos para mostrar")
            else:
             print("Lista de productos registrados: \n")
             for i in enumerate(prodregistrados):
                print(i)
         elif opc==3:
            if prodregistrados ==[]:
               print("No hay artículos para eliminar")
            else:
               print("Productos disponibles para eliminar: ")
               for b, i in enumerate(prodregistrados):
                  print(f"{b} - {i["nombre"]}, {i["categoria"]}")
               ind= int(input("Ingresa el índice de lo que deseas eliminar: "))
               prodregistrados= eliminar_producto(prodregistrados,ind)
         elif opc==4:
           prodregistrados= cargar_datos()
           if prodregistrados == []:
              print("No se encontraron archivos anteriores para cargar")
           else:
              print("Se han cargado los archivos")
         elif opc==5:
            print("Finalizando sesión")
            guardar_datos(prodregistrados)
            break
         else:
            print("Opción fuera del rango")
        except ValueError:
           print("Ingresa una opción válida")
main()
