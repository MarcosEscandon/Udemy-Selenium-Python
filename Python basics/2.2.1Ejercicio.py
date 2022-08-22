# Solicitar vocal minuscula y letra mayuscula. Debe invertir dichos inputs y luego concatenarlos.

vocal = input("Ingrese una vocal en minuscula: ")
letra = input("Ingrese una letra en mayuscula: ")

print("Tu vocal es {}, tu letra es {}, y ambas juntas suenan como: {}".format(vocal.upper(),letra.lower(), vocal.upper()+letra.lower()))