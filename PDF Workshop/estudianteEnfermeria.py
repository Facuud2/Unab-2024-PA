from estudiante import Estudiante

class EstudianteEnfermeria(Estudiante):
    def __init__(self, nombre, edad, sexo, dni, rama, sede, cantidadMaterias):
        super().__init__(sede, 'Enfermeria', cantidadMaterias, nombre, edad, sexo, dni)
        self._rama = rama

    def cambiarRama(self, nuevaRama):
        self._nuevaRama = nuevaRama

    def __str__(self):
        return (super().__str__() +
                f'''Rama: {self._rama}''')