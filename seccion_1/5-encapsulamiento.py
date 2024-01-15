# proteger los elementos de una clase.

class Miclase:
    def __init__(self):
        self._atributo_privado="valor" #con_ al inicio de atributo privado le digo a python que es una clase privada
        self.__atributo_muy_ptivado="valor+"
    
    def _hablar(self): # de igual manera hay metodos privados y muyy privados
        print("Qué onda?")
    
    def __hablar_privado(self):
        print("Top secret")

privado=Miclase()
print(privado._atributo_privado) # en este caso lo imprime, es una señal el_ pero lo imprime.
privado._hablar()


muy_privado=Miclase()
#print(privado.__atributo_muy_ptivado) # imprime un error pues la clase lo oculta por tener __ doble.
#muy_privado.__hablar_privado()

# esto sirve para proteger atributos internos de la clase y mejora la lectura del codigo.