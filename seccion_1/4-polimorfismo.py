# polimorfismo de herenncia tomar un metodo y usarlo dependiendo del objeto creado,

def hacer_sonido(animal):
    print(animal.sonido())

class Perro:
    def sonido (self):
        return "Guau"

class Gato:
    def sonido (self):
        return "Miau"


perro=Perro()

hacer_sonido(perro)

gato=Gato()

hacer_sonido(gato)