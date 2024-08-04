# PABLO_MEDINA_proyectoM2
El programa "longitud de una palabra" nos permite identificar la cantidad de letras incluidas en una palabra, y en este caso damos un parametro para palabras correctas entre cuatro y ocho letras. 
Función verificar_longitud_palabra(palabra):

Calcula la longitud de la palabra usando len(palabra).
Verifica si la longitud está en el rango de 4 a 8. Si es así, retorna un mensaje de que la palabra es correcta.
Si la longitud es menor de 4, retorna un mensaje indicando que faltan letras y muestra el número de letras actuales.
Si la longitud es mayor de 8, retorna un mensaje indicando que sobran letras y muestra el número total de letras.
Función main():

Solicita al usuario que ingrese una palabra.
Llama a la función verificar_longitud_palabra con la palabra ingresada y muestra el mensaje correspondiente.


El programa "encuentra el cuadrante"  determina en qué cuadrante del plano cartesiano se encuentra un punto dado sus coordenadas. A continuación se explica el funcionamiento del código

Función identificar_cuadrante(x, y):

Propósito: Determinar en qué cuadrante del plano cartesiano se encuentra un punto basado en sus coordenadas x e y.
Parámetros:
x (float): Coordenada en el eje X.
y (float): Coordenada en el eje Y.
Proceso:
Primero, verifica si alguna de las coordenadas es igual a cero. En el caso de que esto ocurra, retorna un mensaje indicando que las coordenadas no deben ser cero.
Luego, determina el cuadrante al que pertenece el punto:
Cuadrante I: Cuando x > 0 y y > 0.
Cuadrante II: Cuando x < 0 y y > 0.
Cuadrante III: Cuando x < 0 y y < 0.
Cuadrante IV: Cuando x > 0 y y < 0.
Bloque Principal:

Entrada de Datos:
Utiliza input() para solicitar al usuario las coordenadas x e y. Estos valores se convierten a tipo float para permitir el uso de números decimales.
Llamada a la Función:
Llama a identificar_cuadrante(x, y) con las coordenadas ingresadas y almacena el resultado.
Manejo de Errores:
Un bloque try-except captura y maneja errores de conversión, mostrando un mensaje si el usuario ingresa datos no válidos (por ejemplo, texto en lugar de números).


Los proyectos en este modulo han sido un poco complejos para desarrollarlos por lo que he echado mano no solo del material de ucamp sino de otros recursos como algunas IA y videos en la plataforma de you tube y esto no quedado del todo claro aun.
