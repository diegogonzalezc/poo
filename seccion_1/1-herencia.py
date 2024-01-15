class Persona:
    def __init__(self,nombre,edad,nacionalidad) :
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self): #funciones dentro de clases se llaman metodos
        return("holaa")

class Artista:
    def __init__(self,habilidad) :
        self.habilidad=habilidad

    def mostrar_habilidad(self):
        return(f"mi habilidad es: {self.habilidad}")
    


class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario): 
        super().__init__(nombre,edad,nacionalidad) # tomamos de una clase sus caracteristicas
        self.trabajo=trabajo
        self.salario=salario

class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas, universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas=notas
        self.universidad=universidad


class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario=salario
        self.empresa=empresa

    def presentarse(self):
        print (f"{super().hablar()},soy {self.nombre},{super().mostrar_habilidad()} y trabajo en {self.empresa}")
  


diego=EmpleadoArtista("Diego",30,"Colombiano","Programar","2000 usd","Galilei Learning")
diego.presentarse()

