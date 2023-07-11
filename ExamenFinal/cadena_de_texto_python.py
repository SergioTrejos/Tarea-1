cadena_de_texto = "hola hola de nuevo y hola por ultima vez para ver si funca hola hola hola hola hola si si si si si siiii si"

def mapeo (texto):
    frecuencia_de_palabras = {}
    texto_a_revisar = texto.split()
    for palabras in texto_a_revisar:
        frecuencia_de_palabras [palabras] = frecuencia_de_palabras.get(palabras, 0) + 1
    return frecuencia_de_palabras
print("Facilito tutorial")
print(mapeo(cadena_de_texto))