from collections import Counter

def fibonacci_sequence_up_to(n):
    sequence = [1, 2]
    while sequence[-1] <= n:
        sequence.append(sequence[-1] + sequence[-2])
    if sequence[-1] > n:
        sequence.pop()
    return sequence

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

def decode_fibonacci(code):
    fibonacci = [1, 2]
    while len(fibonacci) < len(code) - 1:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    n = 0
    for i in range(len(code) - 1):  # excluir el último '1'
        if code[i] == '1':
            n += fibonacci[i]
    return n

def contar_simbolos(cadena):
    return Counter(cadena)

# cadena:
cadena = "Dr.Ezhilarasu Umadevi Palani obtained his Post Graduate Degree in Computer Science and Engineering from Anna University, Chennai"
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

# Asignar la codificación Fibonacci como valor extra en el diccionario ordenado
cont = 1
for simbolo, probabilidad in probabilidades_ordenadas.items():
    probabilidades_ordenadas[simbolo] = (probabilidad, encode_fibonacci(cont))
    cont += 1

# Mostrar los resultados
for simbolo, (probabilidad, codificacion_fibonacci) in probabilidades_ordenadas.items():
    print(f"'{simbolo}': Probabilidad {probabilidad:.4f}, Codificación Fibonacci: {codificacion_fibonacci}")

# Guardar las codificaciones en una lista
codificaciones = [codificacion_fibonacci for _, (_, codificacion_fibonacci) in probabilidades_ordenadas.items()]

print("\nCodificaciones:")
print(codificaciones)

string_codificaciones = "".join(codificaciones)
print(string_codificaciones)