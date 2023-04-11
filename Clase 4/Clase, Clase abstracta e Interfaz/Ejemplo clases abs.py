from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("Guau Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")

class Vaca(Animal):
    def sonido(self):
        print("Moooo")

P_perro=Perro()
P_gato=Gato()
P_vaca=Vaca()

P_perro.sonido()
P_gato.sonido()
P_vaca.sonido()


