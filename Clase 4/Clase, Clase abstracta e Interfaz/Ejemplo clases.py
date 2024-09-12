class Vehiculo:
    def __init__(self,marca,modelo,velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
    
    def acelerar(self,incremento):
        self.velocidad_actual += incremento
        if self.velocidad_actual > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
    
    def frenar(self,decremento):
        self.velocidad_actual -= decremento
        if self.velocidad_actual < 0:
            self.velocidad_actual = 0
    
    def mostrar(self):
        print(f"La velocidad actual del {self.marca} {self.modelo} es {self.velocidad_actual} kh/h.")


auto =Vehiculo("Ford","Mustang",250)
auto.acelerar(40)
auto.frenar(5)
auto.mostrar()
