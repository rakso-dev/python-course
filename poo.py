class Perro:

    def __init__(self, nombre, raza, color): # constructor
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.entrenado = False

    def entrenar(self): # metodo de instancia
        print("Acabas de entrenar a", self.nombre)
        self.entrenado = True

    def dar_pata(self):
        if self.entrenado:
            print(f"{self.nombre} te dio la pata".format(self.nombre))
        else:
            print(f"{self.nombre} te mira extrañado")

    def ladrar(): # metodo de clase
        print("guaf guaf")

firulais = Perro("Firulais", "Labrador", "chocolate")
solovino = Perro("Solovino", "Mestizo", "negro")
solovino.entrenar()
solovino.dar_pata()
firulais.dar_pata()
Perro.ladrar()