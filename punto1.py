agenda = []

import os

def agregar_contacto(lista, nombre, telefono):
    if nombre == '' or telefono == '':
        input('Debe diligenciar toda la información solicitada. Presione <ENTER>')
    else:
        lista.append({'nombre': nombre, 'telefono': telefono})
        input(f'\nEl contacto {nombre} ha sido registrado con éxito. Presione <ENTER>')

def buscar_contacto(lista, nombre):
    encontrado = False
    for contacto in lista:
        if contacto['nombre'] == nombre:
            print(f'\nNúmero de teléfono de {nombre}: {contacto["telefono"]}')
            encontrado = True
            break
    if not encontrado:
        print(f'\nEl contacto {nombre} no existe.')

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Salir")

while True:
    menu()
    opcion = input('\nSeleccione una opción: ')
    
    if opcion == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        nombre = input('Nombre del contacto: ')
        telefono = input('Número de teléfono: ')
        agregar_contacto(agenda, nombre, telefono)
        
    elif opcion == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        nombre = input('Ingrese el nombre del contacto a buscar: ')
        buscar_contacto(agenda, nombre)
        input('\nPresione ENTER para continuar...')
        
    elif opcion == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\nLista de contactos:')
        for contacto in agenda:
            print(f"{contacto['nombre']}: {contacto['telefono']}")
        input('\nPresione ENTER para continuar...')
        
    elif opcion == '4':
        break
        
    else:
        input('Opción no válida. Presione <ENTER>')