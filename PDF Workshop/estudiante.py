from persona import Persona

class Estudiante(Persona):
    if __name__ == 'Estudiante':
        ocupacion = 'Estudiante'

    def __init__(self, sede, carrera, cantidadMaterias, nombre, edad, sexo, dni):
        super().__init__(nombre, edad, sexo, dni, 'Estudiante')
        self._sede = sede
        self._carrera = carrera
        self._cantidadMaterias = cantidadMaterias

    def cambiarCarrera(self, nuevaCarrera):
        self._carrera = nuevaCarrera
        print(f'La carrera fue cambiada exitosamente. Nueva carrera: {self._carrera}')

    def __str__(self):
        return super().__str__() + f'''
Sede de cursada: {self._sede}
Carrera: {self._carrera}
Cantidad de materias cursando actualmente: {self._cantidadMaterias}'''



