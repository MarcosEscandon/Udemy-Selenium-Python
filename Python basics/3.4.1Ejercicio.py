# pedir dos palabras y ver si riman o no
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print("No riman, porque una de ellas tiene menos de 3 letras")
elif palabra1[-3:] == palabra2[-3:]:
    print("Las palabras riman")
elif palabra1[-2:] == palabra2[-2:]:
    print("Las palabras riman un poco")
else:
    print("No riman")