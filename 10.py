#BUCLES / LOOPS
# While va a estar repitien hasta una condicion

numero = 1
#while numero < 10:
    #print(numero) # va a estar en bucle hasta que numero sea igual a 10 / como jamas va a ser igual a 10 va a estar en bucle infinito
    
while numero < 10:
    numero += 1 # lo que va hacer es sumar 1 a numero cada vez que se repite el bucle / esto hace que el bucle no sea infinito porque numero va a ir aumentando hasta llegar a 10 y ahi se va a detener el bucle
    print(numero)
    if numero == 5:
        print('es 5')# lo que va hacer es mostrar el texto cuando numero sea igual a 5
        break # lo que va hacer es detener el bucle cuando numero sea igual a 5




# vamos a ver el for / se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena de texto)

lista = [76,43,4.5,3,24]
for numero in lista:
    print(numero) # lo que va hacer es mostrar cada numero de la lista uno por uno
    
# ultima cosa y ya
for n in range(111):
    print(n)
    if n == 5:
        print('es 5')# lo que va hacer es mostrar el texto cuando numero sea igual a 5
        break
       
       
    
