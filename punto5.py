libros = {}

import os

def agregar_libro(diccionario, titulo, autor, genero):
    if titulo == '' or autor == '' or genero == '':
        input('Debe diligenciar toda la información solicitada. Presione <ENTER>')
    else:
        diccionario[titulo] = {'autor': autor, 'genero': genero}
        input(f'\nEl libro "{titulo}" ha sido registrado con éxito. Presione <ENTER>')

def buscar_libro(diccionario, titulo):
    if titulo in diccionario:
        print(f'\nInformación del libro "{titulo}":')
        print(f"Autor: {diccionario[titulo]['autor']}")
        print(f"Género: {diccionario[titulo]['genero']}")
    else:
        print(f'\nEl libro "{titulo}" no está registrado.')


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Salir")

while True:
    menu()
    opcion = input('\nSeleccione una opción: ')
    
    if opcion == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo = input('Título del libro: ')
        autor = input('Autor del libro: ')
        genero = input('Género del libro: ')
        agregar_libro(libros, titulo, autor, genero)
        
    elif opcion == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo = input('Ingrese el título del libro a buscar: ')
        buscar_libro(libros, titulo)
        input('\nPresione ENTER para continuar...')
        
    elif opcion == '3':
        break
        
    else:
        input('Opción no válida. Presione <ENTER> para continuar...')