class Punto:
    def __init__(self, x, y):
        self.puntoX = x
        self.puntoY = y

    # Creacion del metodo impresion sobrecargando el metodo STR
    def __str__(self):
        return f'''({self.puntoX};{self.puntoY})'''

    # Creacion impresion de eje X

    def ejeX(self):
        return f'La coordenada en X es: {self.puntoX}'

    # Creacion impresion de eje Y
    def ejeY(self):
        return f'La coordenada en Y es: {self.puntoY}'

    def opuesto(self):
        return Punto(-self.puntoX, -self.puntoY)
