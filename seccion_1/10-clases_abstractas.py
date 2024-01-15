from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,genero,actividad):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.actividad=actividad

    @abstractclassmethod

    def trabajar(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años.")


#Diego=Persona("Diego",30,"Masculino","CEO") # esto no se puede hacer por ser una clase abstracta no la puedo definir

class Trabajador(Persona):
    def __init__(self,nombre,edad,genero,actividad):
        super().__init__(nombre,edad,genero,actividad)

    def trabajar(self):
        print(f"Mi trabajo es :{self.actividad}")

class Estudiante(Persona):
    def __init__(self,nombre,edad,genero,actividad):
        super().__init__(nombre,edad,genero,actividad)

    def trabajar(self):
        print(f"Estoy estudiando:{self.actividad}")

diego=Trabajador("Diego",30,"Masculino","CEO")
marti=Estudiante("Marti",16,"Femenino","Cine")

diego.presentarse()
diego.trabajar()

marti.presentarse()
marti.trabajar()

#basicamente no puedo crear objetos con la clase personas es como una plantilla para llamar desde otra clase
        