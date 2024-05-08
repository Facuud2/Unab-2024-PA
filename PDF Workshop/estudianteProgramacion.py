from estudiante import Estudiante

class EstudianteProgramacion(Estudiante):
    def __init__(self, nombre, edad, sexo, dni, lenguajeProgramacion, sede, cantidadMaterias):
        super().__init__(sede, 'Programacion', cantidadMaterias, nombre, edad, sexo, dni)
        self._lenguajeProgramacion = lenguajeProgramacion

    def cambiarLenguaje(self, nuevoLenguaje):
        self._lenguajeProgramacion = nuevoLenguaje

    def __str__(self):
        return super().__str__() + f'''
        Rama: {self._lenguajeProgramacion}'''

