'''Implementa un sistema para un supermercado, que  le permita a los usuarios ingresar clientes(nombre, apellido, dni) a la base de datos sqlite3 por consola, editar, eliminar y mostrar todos clientes, de acuerdo a la opción seleccionada.'''
print("Bienvenido al sistema de supermercado")
opcion=0
while(opcion!="5"):
  try:
    opcion=input("Escoge una opción \n 1. Agregar cliente \n 2. Editar cliente \n 3. Eliminar cliente \n 4. Mostrar clientes \n 5. Salir \n")
  except:
      print("Ingresa una opción válida")
  if(opcion=="1"):
    nombre=input("Ingrese el nombre del cliente: ")
    apellido=input("Ingrese el apellido del cliente: ")
    dni=input("Ingrese el dni del cliente: ")
    print("Cliente agregado")
  if(opcion==5):
    print("Saliendo")

    
  
print("Estás fuera del sistema")  
