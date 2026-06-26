from funcproducto import *


def main():
    prodregistrados=[]
    while True:
        print("\nMENU DE REGISTRAR COMPRAS\n1-Añadir artículo\n2-Ver productos registrados\n3-Eliminar artículo\n4-Continuar sesión\n5-Salir y guardar datos\n")
        try:
         opc= int(input("Ingresa una opción: "))
         if opc==1:
            print("Añadir articulo")
            nomb= input("Ingresa nombre del producto a registrar: ")
            cat= input("Ingresa categoría del producto a registrar: ")
            preclp= int(input("Ingresa precio en CLP del artículo a registrar: "))
            prodregistrados= ingresar_producto(prodregistrados,nomb,cat,preclp)

         elif opc==2:
            print(f"Productos registrados: {prodregistrados}")
         elif opc==3:
            if prodregistrados ==[]:
               print("No hay artículos para eliminar")
            else:
               print("Productos disponibles para eliminar: ")
               for b, i in enumerate(prodregistrados):
                  print(f"{b} - {i["nombre"]}, {i["categoria"]}")
               ind= int(input("Ingresa el índice de lo que deseas eliminar: "))
               elim= ()
         elif opc==4:
            print("")
         elif opc==5:
            print()
         else:
            print("Opción fuera del rango")
        except ValueError:
           print("Ingresa una opción válida")
main()