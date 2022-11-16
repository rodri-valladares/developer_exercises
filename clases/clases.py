import math



class Circulo():
    
    def __init__(self, radio):
        if radio <= 0:
            raise Exception("El radio no puede tomar valores menores a 0")
        self.radio_value = radio

    @property
    def radio(self):
        return self.radio_value

    @radio.setter
    def radio(self, radio):
        if radio <= 0:
            raise Exception("El radio no puede tomar valores menores a 0")
        self.radio_value = radio

    @property
    def perimetro(self):
        return 2.0*math.pi*self.radio_value

    @property
    def area(self):
        return math.pi*self.radio_value**2

    def __str__(self):
        return (f'Circulo \nradio: {self.radio_value}\nperimetro: {self.perimetro}\narea: {self.area}\n')

    def __mul__(self, num):
        if num <= 0:
            print(f'El radio no puede tomar valores menores o iguales a 0')
            return
        new_radio = self.radio_value * num
        return Circulo(new_radio)


circulo1 = Circulo(2)
#circulo1 = Circulo(0)
print(circulo1)

circulox = circulo1 * 2
print(circulox)
