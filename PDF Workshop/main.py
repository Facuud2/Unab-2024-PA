from estudianteProgramacion import EstudianteProgramacion
from estudianteEnfermeria import EstudianteEnfermeria
from bartender import Bartender

estudiante1 = EstudianteProgramacion('Pedro Gonzalez', 27,'M',39402737,'Python','Avellaneda',4)
estudiante2 = EstudianteEnfermeria('Pepe Flores',21,'No binario',41365747,'Camillero','Roca',7)

estudiante2.cambiarCarrera('Protesis Dental')

print(estudiante2)

estudiante1.cambiarLenguaje('JavaScript')
print(estudiante1)

bartender1 = Bartender('Florencio Vazquez', 18, 'M',44222111,79,200000,'Manana','Cocteleria de autor', True)
print(bartender1)
bartender1.verificar()