class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
    def get_nombre(self): #funcion que accede a un valor privado de una clase getters
        return self.__nombre
    
    def set_nombre(self,new_nombre): # lo que hacemos es que modificamos el valor privado
        self.__nombre=new_nombre
        return new_nombre
        
    
persona1=Persona("diego",30)

#print(persona1.__nombre) # no se podrría deberiamos usar un metodo getter

nombre=persona1.get_nombre()

print(nombre)

nombre1=persona1.set_nombre("Diego") 
print(nombre1)