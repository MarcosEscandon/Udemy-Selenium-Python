Lista = [20,50,"Curso","Python",3.14] 
# Mostrar valores al usuario, pedir datos y sustituir con dichos datos el primero/segundo lugar
print(Lista)

Word1 = input("Ingrese el primer valor a modificar dentro de la lista: ")    
Word2 = input("Ingrese el segundo valor a modificar dentro de la lista: ") 

Lista[0] = Word1
Lista[1] = Word2

print("El nuevo valor de la lista es: {}".format(Lista))