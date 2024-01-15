#Crear un sustema para una escuela. En el sistema, vamos a tener dos clases:
#Persona y Estudiante. La clase persona tendrá atributos nombre y edad y un metodo que imprima el nombre y la edad.
#La clase Estudiante heredará de la clase Persona y tendra un atributo adicional llamado grado u un metodo que lo imprima.

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def edad_persona(self):
        return(f"Hola soy {self.nombre} y tengo {self.edad} años")


class Estudiante(Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado=grado

    def atributos_estudiante(self):
        print(super().edad_persona()+ " "+ f"y estoy en grado {self.grado}")
        #return super.edad_persona() 

diego=Estudiante("Diego",30, 11)
diego.atributos_estudiante()