from pylab import *
from Ciclo import Ciclo

frenado = int(input("Ingrese el valor de la desaceleración en km/h^2 (debe ser un valor negativo, antes del número agregue -): "))
aceleracion = int(input("Ingrese el valor de la aceleración en km/h^2: "))
tramos = int(input("Ingrese la cantidad de tramos: "))
dist_tramos = int(input("Ingrese la distancia entre los tramos en metros: "))

c = Ciclo(frenado, aceleracion, tramos, dist_tramos)
cv = c.velocidad()

def grafico():
    velocidad = cv
    plt.plot(velocidad)
    plt.title("Distancia vs Velocidad")
    plt.xlabel("Distancia (km)")
    plt.ylabel("Velocidad (km/h)")

    return plt.show()

i = 0

while i == 0:
    pregunta1 = input("¿Desea saber la velocidad alcanzada en cada uno de los tramos? ")
    if (pregunta1 == "si" or pregunta1 == "Si"):
        print("La velocidad total en cada tramo del ciclo fue de ",cv)
        i += 1
    elif (pregunta1 == "no" or pregunta1 == "No"):
        i += 1
    else:
        print("Ingrese una respuesta valida")
    
l = 0

while l == 0:
    pregunta2 = input("¿Desea ver el gráfico velocidad vs distancia? ")
    if (pregunta2 == "si" or pregunta2 == "Si"):
        print(grafico())
        l += 1
    elif (pregunta1 == "no" or pregunta1 == "No"):
        l += 1
    else:
        print("Ingrese una respuesta valida")

a = input("Presione ENTER para cerrar")
        


