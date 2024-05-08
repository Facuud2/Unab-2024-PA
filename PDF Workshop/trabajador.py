from persona import Persona

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, dni, ocupacion, rubro, id, sueldo, turno):
        super().__init__(nombre, edad, sexo, dni, ocupacion)
        self._rubro = rubro
        self._id = id
        self._sueldo = sueldo
        self._turno = turno

    def __str__(self):
        return super().__str__() + f'''
Rubro: {self._rubro}
Identificador: {self._id}
Ingresos mensuales: ${self._sueldo}
Turno: {self._turno}'''