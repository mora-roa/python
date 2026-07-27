#LISTAS

my_list = ['python',53,'false']# lo que va hacer es crear una lista con diferentes tipos de datos / tiene que contener valores validos

# el type va a hacer una lista
print(type(my_list))#list

print(my_list)# lo que va hacer es mostrar la lista completa
print(my_list[1])# lo que va hacer es mostrar el valor de la pocision 1 que es "53"
# en la programacion se empienza a contar desde el 0 y no por el 1

print(my_list[-1])# lo que va hacer es mostrar el valor de la ultima pocision que es "false"
print(my_list)

my_list.append('53')# lo que va hacer es agregar un nuevo valor a la lista
print(my_list)

my_list.insert(3,'hola')# lo que va hacer es agregar un nuevo valor a la lista en la pocision 3
print(my_list)

my_list.remove('53')# lo que va hacer es eliminar el valor "53" de la lista
print(my_list)

my_list.pop(2)# lo que va hacer es eliminar el valor de la pocision 2 que es "hola"
print(my_list.pop(2))# lo que va hacer es eliminar el valor de la pocision 2 que es "hola" y mostrarlo
print(my_list)
 
 print(my_list.count('53'))# lo que va hacer es contar la cantidad de veces que se repite el valor "53" en la lis