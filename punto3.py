estudiantes = {}

import os

def agregar_estudiante(diccionario, nombre, edad, carrera):
    if nombre == '' or edad == '' or carrera == '':
        input('Debe diligenciar toda la información solicitada. Presione <ENTER>')
    else:
        diccionario[nombre] = {'edad': edad, 'carrera': carrera}
        input(f'\nEl estudiante {nombre} ha sido registrado con éxito. Presione <ENTER>')

def buscar_estudiante(diccionario, nombre):
    if nombre in diccionario:
        print(f'\nInformación de {nombre}:')
        print(f"Edad: {diccionario[nombre]['edad']}")
        print(f"Carrera: {diccionario[nombre]['carrera']}")
    else:
        print(f'\nEl estudiante {nombre} no existe.')

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Mostrar todos los estudiantes")
    print("4. Salir")
    
while True:
    menu()
    opcion = input('\nSeleccione una opción: ')
    
    if opcion == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        nombre = input('Nombre del estudiante: ')
        edad = input('Edad del estudiante: ')
        carrera = input('Carrera del estudiante: ')
        agregar_estudiante(estudiantes, nombre, edad, carrera)
        
    elif opcion == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        nombre = input('Ingrese el nombre del estudiante a buscar: ')
        buscar_estudiante(estudiantes, nombre)
        input('\nPresione ENTER para continuar...')
        
    elif opcion == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\nLista de estudiantes:')
        for nombre, info in estudiantes.items():
            print(f"{nombre}: Edad: {info['edad']}, Carrera: {info['carrera']}")
        input('\nPresione ENTER para continuar...')
        
    elif opcion == '4':
        break
        
    else:
        input('Opción no válida. Presione <ENTER>')