#EXCEPCIONES
#Las excepciones son errores que ocurren durante la ejecución de un programa.

try:
    print(5 + '3') # lo que va hacer es mostrar un error porque no se pueden sumar un numero con una cadena de texto
except TypeError as e:
    print(f"Error: {e}")