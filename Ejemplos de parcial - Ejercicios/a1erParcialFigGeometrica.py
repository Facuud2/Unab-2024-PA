from math import sqrt
from math import pi

class FiguraGeometrica:
    def __init__(self, longitud):
        self._longitud = longitud


class Cuadrado(FiguraGeometrica):
    def perimetro(self):
        return f'Perimetro del cuadrado: {self._longitud * 4}cm'

    def area(self):
        return f'Area del cuadrado: {self._longitud ** 2}'


class Triangulo(FiguraGeometrica):
    ''' Clase padre triangulo contenedora de los futuros metodos a completar segun el tipo de triangulo '''
    def __init__(self, longitud, base, altura):
        super().__init__(longitud)
        self._base = base
        self._altura = altura

    def perimetro(self):
        pass

    def area(self):
        pass


class TrianguloRectangulo(Triangulo):
    ''' Operaciones para un triangulo rectangulo '''
    def __init__(self, longitud, base, altura, hipotenusa):
        super().__init__(longitud, base, altura)
        self._hipotenusa = hipotenusa

    def perimetro(self):
        return f'Perimetro del triangulo rectangulo: {self._base + self._altura + self._hipotenusa}cm'

    def area(self):
        return f'Area del triangulo rectangulo: {(1 / 2) * self._base * self._altura}'


class TrianguloIsosceles(Triangulo):
    def __init__(self, longitud, base, altura, ladosIguales, ladoDistinto):
        super().__init__(longitud, base, altura)
        self._ladosIguales = ladosIguales
        self._ladoDistinto = ladoDistinto

    def perimetro(self):
        return f'Perimetro del triangulo isosceles: {2 * self._ladosIguales + self._ladoDistinto}cm'

    def area(self):
        return f'Area del triangulo rectangulo: {(1 / 2) * self._base * self._altura}'


class TrianguloEquilatero(Triangulo):
    def perimetro(self):
        return f'Perimetro del triangulo equilatero: {self._longitud * 3}cm'

    def area(self):
        return f'Area del triangulo equilatero: {(sqrt(3) / 4) * (self._longitud ** 2)}'


class Circulo(FiguraGeometrica):
    def perimetro(self):
        return f'Circunsferencia del circulo: {2 * pi * self._longitud}'

    def area(self):
        return f'Area del circulo: {pi * self._longitud**2}'

