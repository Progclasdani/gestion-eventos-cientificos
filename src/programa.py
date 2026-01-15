#Prototipo programa
"""
Daniel Vicente Moya 15/01/2025
*********************************************
Programa para la toma de datos de puntos y
su representación en una gráfica.
*********************************************
"""
#Importado de módulos
import matplotlib.pyplot as plt

#Decalaración de variables globales
x_data = []
y_data = []

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

def tomar_puntos():
    """
    Función para tomar los datos de las
    coordenas de los puntos.
    """
    #Declaración de Variables
    x_aux = []
    y_aux = []
    #Bucle toma de datos
    while True:
        #Toma de datos
        print("Introduce punto")
        #Comprobamos datos introducidos
        while True: #Valor de x
            x_in = input("Valor en x: ")
            try:
                x_in = float(x_in)
                break
            except ValueError:
                print("No es un número válido.")
        while True: #Valor de y
            y_in = input("Valor en y: ")
            try:
                y_in = float(y_in)
                break
            except ValueError:
                print("No es un número válido.")
        #Montamos el punto
        x_aux.append(x_in)
        y_aux.append(y_in)
        #Colsulta si desea finalizar la entrada de puntos
        finalizar = input("Desea introducir otro punto(s/n): ")
        if (finalizar == "n" or finalizar == "N" or
            finalizar == "no" or finalizar == "No" or
            finalizar == "NO"):
            break
    return x_aux, y_aux

def mostrar_diagrama(x_aux, y_aux):
    """
    Función para mostrar los valores de los puntos
    introducidos en una gráfica de nube de puntos.
    """
    plt.scatter(x_aux, y_aux)
    plt.show()
    return

#Programa principal
while True:
    #Muestra menú
    menu_programa()
    #Acción de menú
    opcion = input("Elige una opción: ")
    if opcion == "1":
        (x_data, y_data) = tomar_puntos()
    elif opcion == "2":
        mostrar_diagrama(x_data, y_data)
    elif opcion == "3": #Cierra programa
        sys.exit(0)
    else:
        print("Opción no disponible.")
