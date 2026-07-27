# OPERADORES ARITMETICOS

print(2 + 3) # suma
print(5 - 2) # resta
print(4 * 3) # multiplicacion
print(10 / 2) # division
print(10 // 3) # division flor / lo que hace es dividir y dar el numero entero 
print(10 % 3) # modulo / lo que hace es mostrar el residuo de la division
print(2 ** 3) # potencia / lo que hace es elevar el numero

#CON TEXTO

print('hola' + 'mundo')# lo que va hacer es juntar las pabras o letras
print('hola ' * 6) # lo que va hacer es decir 6 veses "hola" / depediendo del numero es la cantidad de que la palabra se repita


#JUNTAR TEXTO CON NUMERO UTILIZANDO ORERADORES ARTIMETICOS
a = 5 
print('hola ' + str(a)) # lo que va hacer es convertir el numero a texto y luego juntar las palabras
# se utiliza str cuando vas a combinar un texto con una vaiable


# OERADORES COMPARATIVO
# aqui normalmente se utiliza en "booleano" que representa false o true
print(4 < 8)#true
print(4 > 8)#false
print(4 == 8)#false / aqui pregunta se los dos valores son exactaminte iguales
print(4 <= 8)#true / aqui pregunta si es menor o igual
print(4 >= 8)#false / aui pregunta si es  mayor o  igual
print(4 != 8)#true / aqui pregunta si es diferente


#CON TEXTO
#cuenta donde estan pocisonadas las letras en el abecedario
print('hola' > 'mundo')#false
print('c' < 'b')#false
print('aaa' < 'aba')#true 

#para que cuente las cantidad de carcteres tines que usar la funcion "len"
print(len('hola') < len('bolas'))#true / aui es donde cuenta las cantidad de cracteres

#OPERADORES LOGICOS
#and / conque uno de los dos no sea verdadero dara false
print(True and False)#false
print(True and True)#true


#or / conque uno de los dos sea verdadero dara verdadero
print(True or False)#true
print(True or True)#true
print(False or False)#false


#not / invierte de falso a verdadero y de verdadero a falso
print(not(True))#false
print(not(False))#true


