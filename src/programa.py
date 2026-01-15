#Prototipo programa
"""
Daniel Vicente Moya 15/01/2025
*********************************************
Programa para la toma de datos de puntos y
su representación en una gráfica.
*********************************************
"""
#Importado de módulos

#Declaración de funciones
def menu_programa():
    """
    Función que muestra las opciones disponibles
    en un menú.
    """
    print("Opciones disponibles:")
    print("1- Añadir puntos.")
    print("2- Muestra diagrama de puntos.")
    print("3- Cerrar programa.")
    return

#Programa principal
while True:
    #Muestra menú
    menu_programa()
    #Acción de menú
    opcion = input("Elige una opción: ")
    if opcion == "1":
        #Función para añadir puntos.
    elif opcion == "2":
        #Función para muestra de diagrama
    elif opcion == "3": #Cierra programa
        sys.exit(0)
    else:
        print("Opción no disponible.")
