#SETS

my_set = {}
print(type(my_set))# lo que va hacer es mostrar el tipo de dato que es el set


my_set = {'python', 'javaScript', 'c++'}
print(type(my_set))# lo que va hacer es mostrar el tipo de dato que es el
print(my_set)# lo que va hacer es mostrar el set completo / cuando lo imprimes NO TIENE UN ORDEN ESPECIFICO lo que hace que siempere sea alatorio

# print(my_set[o]) type error porque los set no tienen pocisiones

my_set.add('python')
print(my_set)
# esto no va a hacer nada porque el set no permite valores repetidos

my_set.add('c#')
print(my_set)
# ya aqui si va a agregar el valor "c#" porque no esta repetido

#una funcion mas :) / (.difference_update) lo que hace es mostrar la diferencia entre dos sets pillen ps
my_set2 = {'python', 'java', 'c++'}
my_set.difference_update(my_set2)
print(my_set)

