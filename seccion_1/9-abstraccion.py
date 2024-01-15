class Auto():
    def __init__(self) -> None:
        self.estado="apagado"

    def encender(self):
        self._estado="encendido"
        print("El auto está encendido")

    def conducir(self):
        if self.estado== "apagado":
            self.encender()
        print("conduciendo el auto")

mi_auto= Auto()

mi_auto.conducir()

#dar al usuario solo las funciones importantes, el usuario no sabra que se enciendo ni como.
#dentro de la clase hay metodos para usarse.
#para usar un celular solo necesito apretar botones, no saber que pasa al interior.