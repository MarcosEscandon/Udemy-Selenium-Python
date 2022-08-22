# solicitar una letra, si es vocal mostrar mensaje
letra = input("Ingrese una letra: ")

if letra in "aeiou":
    print("Es vocal")
else:
    print("No es vocal")