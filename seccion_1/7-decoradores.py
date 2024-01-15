# toma una función la modifica y devueleve una función modificada.

def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("después de llamar la funcion")
    return funcion_modificada


# def saludo ():
#     print("Diego")

# saludo_modificado=decorador(saludo)

# saludo_modificado()

#la forma optima de hacer lo que hicimos arriba es:
@decorador
def saludo ():
     print("Diego")

saludo()