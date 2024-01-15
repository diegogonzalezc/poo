class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad

    @property    
    def nombre(self): #funcion que accede a un valor privado de una clase getters
        return self.__nombre
    
    @nombre.setter #asi se llama al setter
    def nombre(self,new_nombre): # lo que hacemos es que modificamos el valor privado
        self.__nombre=new_nombre
        return new_nombre
        
    
persona1=Persona("diego",30)

#print(persona1.__nombre) # no se podrría deberiamos usar un metodo getter

#nombre=persona1.get_nombre()  se usan los parentesis pero si usamos @property no es necesario

nombre_persona=persona1.nombre # asi lo llamamos como si fuera una propiedad, es mas podemos llamar el setter y getter como la propiedad que queremos cambiar
print(nombre_persona)

persona1.nombre=("Diego") 
nombre_persona=persona1.nombre
print(nombre_persona)

#con la notación del punto entramos a las propiedades por ser getter y setter