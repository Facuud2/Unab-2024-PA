from math import pi

class FiguraGeometrica:
    def __init__(self, longitud):
        self._longitud = longitud


class Cuadrado(FiguraGeometrica):
    def perimetro(self):
        return f'Perimetro del cuadrado: {self._longitud*4}cm'

    def area(self):
        pass

class Triangulo(FiguraGeometrica):
    def __init__(self, lado1, lado2, lado3, longitud, base, altura):
        super().__init__(longitud)
        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3
        self._base = base
        self._altura = altura

    def perimetro(self):
        return f'El perimetro del triangulo es: {self._lado1 + self._lado2 + self._lado3}cm'

    def area(self):
        return f'El area de un triangulo es: {(self._base * self._altura) / 2}cm'

class Circulo(FiguraGeometrica):
    pass