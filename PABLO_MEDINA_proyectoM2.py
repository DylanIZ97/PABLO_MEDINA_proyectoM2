# Programa para verificar la longitud de una palabra ingresada por el usuario.

# Solicita al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")

# Calcula la longitud de la palabra ingresada
longitud = len(palabra)

# Verifica la longitud de la palabra y muestra el mensaje correspondiente
if 4 <= longitud <= 8:
    print(f"La palabra es correcta tiene {longitud} letras.")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
else:  # longitud > 8
    print(f"Sobran letras. Tiene {longitud} letras.")