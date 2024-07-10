from collections import Counter

# creación de los numeros de fibonacci
def fibonacci_sequence_up_to(n):
    sequence = [1, 2]
    while sequence[-1] <= n:
        sequence.append(sequence[-1] + sequence[-2])
    if sequence[-1] > n:
        sequence.pop()
    return sequence

# codificación de fibonacci
def encode_fibonacci(n):
    if n == 0:
        return '11'  # caso especial

    fibonacci = fibonacci_sequence_up_to(n)[::-1]  # invertimos la secuencia

    result = []
    for f in fibonacci:
        if f <= n:
            result.append('1')
            n -= f
        else:
            result.append('0')
    result = result[::-1]
    result.append('1')  # se añade el último '1' para la terminación
    return ''.join(result)

def decode_string(cadena):
    buscador = ""
    cadena_auxiliar = []
    for i in cadena:
        buscador += i
        for simbolo, (_, codificacion_fibonacci, _) in probabilidades_ordenadas.items():
            if buscador == codificacion_fibonacci:
                print(f"Encontrado: {simbolo}")
                buscador = ""
                cadena_auxiliar.append(simbolo)
    return cadena_auxiliar

def encode_string(cadena):
    resultado = ""
    for i in cadena:
        for simbolo, (_, codificacion_fibonacci, _) in probabilidades_ordenadas.items():
            if i == simbolo:
                resultado += codificacion_fibonacci
    return resultado

# contar los simbolos
def contar_simbolos(cadena):
    return Counter(cadena)

# cadena:
cadena = "Nos vamos a cinquear este proyecto"

# guardar el resultado de la función contar_simbolos en una variable
resultado = contar_simbolos(cadena)

# Diccionario para almacenar las probabilidades
probabilidades = {}

# Calcular la probabilidad de cada símbolo
longitud_cadena = len(cadena)
for simbolo, cuenta in resultado.items():
    probabilidad = cuenta / longitud_cadena
    probabilidades[simbolo] = probabilidad

# Ordenar el diccionario por probabilidades de mayor a menor
probabilidades_ordenadas = dict(sorted(probabilidades.items(), key=lambda item: item[1], reverse=True))

# Asignar la codificación Fibonacci como valor extra en el diccionario ordenado así como el índice
cont = 1
for simbolo in probabilidades_ordenadas:
    probabilidad = probabilidades_ordenadas[simbolo]
    codificacion_fibonacci = encode_fibonacci(cont)
    probabilidades_ordenadas[simbolo] = (probabilidad, codificacion_fibonacci, cont)
    cont += 1

# Mostrar los resultados
for simbolo, (probabilidad, codificacion_fibonacci, indice) in probabilidades_ordenadas.items():
    print(f"'{simbolo}': Probabilidad {probabilidad:.4f}, índice: {indice}, Codificación Fibonacci: {codificacion_fibonacci}")

# Guardar las codificaciones en una lista
codificaciones = [codificacion_fibonacci for _, (_, codificacion_fibonacci, _) in probabilidades_ordenadas.items()]
print("\nCodificaciones:")
print(codificaciones)

string_codificaciones = "".join(codificaciones)
print(string_codificaciones)

decode_string(string_codificaciones)
cadena_codificada = encode_string(cadena)
print("\nCadena codificada:")
print(cadena_codificada)

print("\nDecodificación:")
cadena_descodificada = decode_string(cadena_codificada)
print(cadena_descodificada)

cadena_final = "".join(cadena_descodificada)
print("\nCadena final:")    
print(cadena_final)