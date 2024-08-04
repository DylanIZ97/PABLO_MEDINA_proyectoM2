# Función para identificar el cuadrante
def identificar_cuadrante(x, y):
    # Verifica si alguna de las coordenadas es cero
    if x == 0 or y == 0:
        return "Las coordenadas no deben ser cero."
    
    # Determina en qué cuadrante se encuentra el punto
    if x > 0 and y > 0:
        return "El punto se encuentra en el cuadrante I"
    elif x < 0 and y > 0:
        return "El punto se encuentra en el cuadrante II"
    elif x < 0 and y < 0:
        return "El punto se encuentra en el cuadrante III"
    elif x > 0 and y < 0:
        return "El punto se encuentra en el cuadrante IV"

# Solicitar las coordenadas al usuario
try:
    x = float(input("Ingrese X: "))  # Solicita la coordenada X y la convierte a flotante
    y = float(input("Ingrese Y: "))  # Solicita la coordenada Y y la convierte a flotante
    
    # Identifica el cuadrante y muestra el resultado
    resultado = identificar_cuadrante(x, y)
    print(resultado)
except ValueError:
    # Captura errores si la entrada no es un número válido
    print("Por favor, ingrese números válidos.")

