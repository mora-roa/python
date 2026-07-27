#SRTING

mi_first__string = "mi string con comillas dobles"
mi_second_string = 'mi string con comillas simples'

print(mi_first__string, mi_second_string)

#para facilitar en proceso hacemos lo siguient
print(f'este es un texto de variable {mi_first__string} hola')# lo que va hacer es mostrar el texto y la variable que esta entre llaves

#lo siguiente que vamos hacer es que un string tenga diferente variables

other_string = 'hola'
a,b,c,d = other_string # lo que va hacer es asignar cada letra a una variable diferente
print(a)
print(b)
print(c)
print(d)

#nose porque lo vayas hacer pero aqui esta la forma unida
print(f'{a}{b}{c}{d}')#