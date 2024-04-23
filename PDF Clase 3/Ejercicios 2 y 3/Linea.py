# Ejercicio 3:
# Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que
# pasa la línea en un espacio de dos dimensiones.
# La clase dispondrá de los siguientes métodos:
# ● Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clase
# Punto, que son utilizados para inicializar los atributos.
# ● mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
# ● mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
# ● mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
# ● mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique.

from Punto import Punto




class Linea():
    def __init__(self, punto_a, punto_b):
        self._puntoA = punto_a
        self._puntoB = punto_b

    def __str__(self):
        return f'La linea comienza en {self._puntoA} y termina {self._puntoB}'

    # SIEMPRE USAR puntoX en lugar del atributo que recibe la clase Punto

    def mueve_derecha(self, distancia):
        self._puntoA.puntoX += distancia
        self._puntoB.puntoX += distancia

        return f'La linea luego del cambio realizado se encuentra en {self._puntoA} y termina en {self._puntoB}'

    def mueve_izquierda(self, distancia):
        self._puntoA.puntoX -= distancia
        self._puntoB.puntoX -= distancia

        return f'La linea luego del cambio realizado se encuentra en {self._puntoA} y termina en {self._puntoB}'

    def mueve_arriba(self, distancia):
        self._puntoA.puntoY += distancia
        self._puntoB.puntoY += distancia

        return f'La linea luego del cambio realizado se encuentra en {self._puntoA} y termina en {self._puntoB}'

    def mueve_abajo(self, distancia):
        self._puntoA.puntoY -= distancia
        self._puntoB.puntoY -= distancia

        return f'La linea luego del cambio realizado se encuentra en {self._puntoA} y termina en {self._puntoB}'


puntoInicio = Punto(2, 2)
puntoFin = Punto(3, 7)

linea1 = Linea(puntoInicio, puntoFin)
print(linea1)

print(linea1.mueve_derecha(3))
print(linea1.mueve_izquierda(8))
print(linea1.mueve_arriba(1))
print(linea1.mueve_abajo(11))
