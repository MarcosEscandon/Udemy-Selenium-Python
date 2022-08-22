# pedir un pais, mostrar la capital, si no avisar

Capitales = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", 
"Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

Pais = input("Ingrese un pais para saber su capital: ")
Letra = Pais.capitalize() in Capitales

if Letra == True:
    print(Capitales[Pais.capitalize()])
else:
    print("Su pais no esta dentro del diccionario")
