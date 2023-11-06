
class Animal():
    def __init__(self):
        print("ANIMAL CREADO")
    def quiensoy(self):
        print("soy un animal")
    def comer(self):
        print("estoy comiendo")


class Perro(Animal):

    def __init__(self, race, name, dots):
        Animal.__init__(self)
        print("Perro Creado")
        self.race =race
        self.name =name
        #esperamos un valor booleano
        self.dots=dots

    def quiensoy(self):
        return super().quiensoy()
    def comer(self):
        return super().comer()




    

