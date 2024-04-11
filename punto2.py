inventario = {}

import os

def agregar_producto(diccionario, id_producto, nombre, cantidad):
    if id_producto == '' or nombre == '' or cantidad == '':
        input('Debe diligenciar toda la información solicitada. Presione <ENTER>')
    else:
        diccionario[id_producto] = {'nombre': nombre, 'cantidad': cantidad}
        input(f'\nEl producto {nombre} ha sido registrado con éxito. Presione <ENTER>')

def buscar_producto(diccionario, nombre):
    encontrado = False
    for id_producto, producto in diccionario.items():
        if producto['nombre'] == nombre:
            print(f'\nCantidad disponible de {nombre}: {producto["cantidad"]}')
            encontrado = True
            break
    if not encontrado:
        print(f'\nEl producto {nombre} no existe en el inventario.')

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Mostrar todos los productos")
    print("4. Salir")

while True:
    menu()
    opcion = input('\nSeleccione una opción: ')
    
    if opcion == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        nombre = input('Nombre del producto: ')
        cantidad = input('Cantidad disponible: ')
        id_producto = input('ID del producto: ')
        agregar_producto(inventario, id_producto, nombre, cantidad)
        
    elif opcion == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        nombre = input('Ingrese el nombre del producto a buscar: ')
        buscar_producto(inventario, nombre)
        input('\nPresione ENTER para continuar...')
        
    elif opcion == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\nInventario de productos:')
        for id_producto, producto in inventario.items():
            print(f"{id_producto}: {producto['nombre']} - Cantidad: {producto['cantidad']}")
        input('\nPresione ENTER para continuar...')
        
    elif opcion == '4':
        break
        
    else:
        input('Opción no válida. Presione <ENTER>')