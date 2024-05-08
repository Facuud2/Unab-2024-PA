from trabajador import Trabajador

class Bartender(Trabajador):
    def __init__(self, nombre, edad, sexo, dni, id, sueldo, turno, especialidad, flair = bool):
        super().__init__(nombre, edad, sexo, dni, 'Bartender', 'Gastronomia', id, sueldo, turno)
        self._flair = flair
        self._especialidad = especialidad

    def verificar(self):
        if self._especialidad == 'Cocteleria de autor' and self._flair == True:
            print(f'El bartender {self._nombre} NO es apto para el cargo.')
        else:
            print(f'El bartender {self._nombre} SI es apto para el cargo.')

