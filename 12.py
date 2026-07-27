# CLASES

class humano:
    def __init__(self, altura, edad, peso):
        self.altura = altura
        self.edad = edad
        self.peso = peso
    def saludar(self):
            print(f'el de {self.edad} años esta saludando') # lo que va hacer es mostrar el mensaje "el de {edad} años esta comiendo" donde {edad} es el valor de la edad del objeto

persona1 = humano(1.80, 30, 80)

print(f'el humano mide {persona1.altura}m pesa {persona1.peso}kg y tiene {persona1.edad} años') # lo que va hacer es mostrar el valor de la altura de persona1
persona1.saludar() # lo que va hacer es llamar al método "saludar" del objeto "persona1"
