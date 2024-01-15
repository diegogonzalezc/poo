class A:
    def hablar(self):
        print("Hola Desde A")

class B(A):
    def hablar(self):
        print("Hola Desde B")


class C(B):
    def hablar(self):
        print("Hola Desde C")

class D(C,B):
    def hablar(self):
        print ("hola desde D")

d=D()
d.hablar()

print(D.mro())# CON ESTO VEO COMO SE EJECUTA LA CLASE Y CUAL INSTANCIA ESTOY TOMANDO,