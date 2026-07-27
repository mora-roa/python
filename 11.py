#FUNCIONES
# una función es un bloque de código que se ejecuta cuando es llamada, las funciones pueden recibir argumentos y devolver valores

def Sum_numbers(num1,num2 = 10):# lo que va hacer es crear una función llamada "Sum_numbers" que recibe dos argumentos "num1" y "num2"
    print(num1 + num2)# lo que va hacer es mostrar la suma de los dos argumentos
    
Sum_numbers(5,10)# lo que va hacer es llamar a la función "Sum_numbers" con los argumentos 5 y 10
Sum_numbers(3)
#tambien podemos hacer si no existe tal numero que ese tal numero sea igual a tal numero puesto despus del igual
 
 # return es una palabra reservada que se utiliza para devolver un valor desde una función, cuando se ejecuta un return la función se detiene y devuelve el valor especificado
def Sum_numbers(num1,num2):
    return num1 + num2 # lo que va hacer es devolver la suma de los dos argumentos
result = Sum_numbers(5,10) # lo que va hacer es llamar a la función "Sum_numbers" con los argumentos 5 y 10 y guardar el resultado en la variable "result"
print(result) # lo que va hacer es mostrar el resultado de la suma de los dos argumentos
