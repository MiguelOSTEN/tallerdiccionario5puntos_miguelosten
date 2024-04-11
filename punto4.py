peliculas = {}
import os

def agregar_pelicula(diccionario, titulo, genero, año):
    if titulo == '' or genero == '' or año == '':
        input('Debe diligenciar toda la información solicitada. Presione <ENTER>')
    else:
        diccionario[titulo] = {'genero': genero, 'año': año}
        input(f'\nLa película "{titulo}" ha sido registrada con éxito. Presione <ENTER>')

def buscar_pelicula(diccionario, titulo):
    if titulo in diccionario:
        print(f'\nInformación de la película "{titulo}":')
        print(f"Género: {diccionario[titulo]['genero']}")
        print(f"Año: {diccionario[titulo]['año']}")
    else:
        print(f'\nLa película "{titulo}" no está registrada.')


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Mostrar todas las películas")
    print("4. Salir")

while True:
    menu()
    opcion = input('\nSeleccione una opción: ')
    
    if opcion == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo = input('Título de la película: ')
        genero = input('Género de la película: ')
        año = input('Año de la película: ')
        agregar_pelicula(peliculas, titulo, genero, año)
        
    elif opcion == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo = input('Ingrese el título de la película a buscar: ')
        buscar_pelicula(peliculas, titulo)
        input('\nPresione ENTER para continuar...')
        
    elif opcion == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\nLista de películas:')
        for titulo, info in peliculas.items():
            print(f"Título: {titulo}, Género: {info['genero']}, Año: {info['año']}")
        input('\nPresione ENTER para continuar...')
        
    elif opcion == '4':
        break
        
    else:
        input('Opción no válida. Presione <ENTER>')