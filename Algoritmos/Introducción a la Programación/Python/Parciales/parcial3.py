from queue import Queue as Cola
from queue import LifoQueue as Pila

# Ejercicio 1 (2,25 puntos)
# Implementar la función subsecuencia_mas_larga especificada (todos_consecutivos no es testeado)

# problema subsecuencia_mas_larga (in v: seq⟨Z⟩) : ZxZ {
#   requiere: { La longitud de v es distinto de 0 }
#   asegura: { Sea x la primera subsecuencia más larga en v tal que vale todos_consecutivos(x), la primera componente de res es igual a |x| y la segunda es igual al índice en v donde comenzaría x }
# }

# problema todos_consecutivos (in v: seq⟨Z⟩) : Bool {
#   asegura: { res == True <==> cada par de elementos adyacentes en v son números consecutivos, es decir, que su diferencia es igual a 1 }
# }

def absoluto(n: int) -> int:
    if n < 0:
        return -1 * n
    return n

def armar_subsecuencia(v: list[int]) -> list[list[int]]:
    res: list[list[int]] = []
    sub: list[int] = []

    for numero in v:
        if len(sub) > 0 and absoluto(sub[len(sub) - 1] - numero) != 1:
            res.append(sub)
            sub = []
        sub.append(numero)

    res.append(sub)
    return res

def subsecuencia_mas_larga(v: list[int]) -> tuple[int, int]:
    max_longitud: int = 1
    max_indice: int = 0

    indice: int = 0

    for s in armar_subsecuencia(v):
        if len(s) > max_longitud:
            max_longitud = len(s)
            max_indice = indice
        indice += len(s)

    return (max_longitud, max_indice)

# Ejercicio 2 (2,25 puntos)
# Ana tiene exámenes de respuesta Verdadero ó Falso. Ella sabe que en cada examen la cantidad 
# de respuestas correctas cuyo valor es Falso es igual a la cantidad de respuestas correctas 
# cuyo valor es Verdadero. Tenemos el historial de las respuestas de cada exámen dados por Ana 
# en una cola. En cada uno Ana respondió todas las preguntas.

# problema mejor_resultado_de_ana (in examenes: Cola⟨ seq⟨Bool⟩ ⟩) : seq⟨Z⟩ {
#   requiere:{ Cada elemento de examenes es no vacío y tiene longitud par }
#   asegura: { res tiene la misma cantidad de elementos que examenes }
#   asegura: { res[i] es igual a la máxima cantidad de respuestas correctas que Ana podría haber respondido en el i-ésimo exámen resuelto en examenes, para 0 <= i < cantidad de elementos de examenes }
# }

def minimo(a: int, b: int) -> int:
    if a <= b:
        return a
    return b

def verdaderas(e: list[bool]) -> int:
    res: int = 0
    for i in e:
        if i: res += 1
    return res

def mejor_resultado_de_ana(examenes: Cola[list[bool]]) -> list[int]:
    aux: Cola[list[bool]] = Cola()
    res: list[int] = []

    while not examenes.empty():
        examen: list[bool] = examenes.get()
        aux.put(examen)
        v: int = verdaderas(examen)
        f: int = len(examen) - v
        res.append(2 * minimo(v, f))
    
    while not aux.empty():
        examenes.put(aux.get())

    return res

# Ejercicio 3 (2,25 puntos)
# problema cambiar_matriz(inout A: seq⟨seq⟨Z⟩⟩) {
#   requiere: { Todas las filas de A tienen la misma longitud }
#   requiere: { El mínimo número que aparece en A es igual a 1 }
#   requiere: { El máximo número que aparece en A es igual a #filas de A por #columnas de A }
#   requiere: { No hay enteros repetidos en A }
#   requiere: { Existen al menos dos enteros distintos en A }
#   modifica: { A }
#   asegura: { A tiene exactamente las mismas dimensiones que A@pre }
#   asegura: { El conjunto de elementos que aparecen en A es igual al conjunto de elementos que aparecen en A@pre }
#   asegura: { A[i][j] != A@pre[i][j] para todo i, j en rango }
# }

def cambiar_matriz(A: list[list[int]]) -> None:
    maximo: int = len(A) * len(A[0])
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            if A[i][j] == maximo:
                A[i][j] = 1
                continue
            A[i][j] += 1

# Ejercicio 4 (2,25 puntos)
# Tenemos un texto que contiene palabras. Por simplicidad, las palabras están separadas únicamente por uno o más espacios.

# problema palabras_por_vocales (in texto: string): Diccionario⟨Z,Z⟩ {
#   requiere: { Si existe una letra vocal en texto, esta no lleva tildes, diéresis, ni ningún otro símbolo }
#   asegura: { Si existe una palabra en texto con x vocales en total, x es clave de res }
#   asegura: { Las claves de res representan la cantidad total de vocales de una palabra, y cada valor corresponde a la cantidad de palabras en texto con ese número de vocales. }
#   asegura: { Los valores de res son positivos }
# }

def esVocal(caracter: chr) -> bool:
    for c in "aeiouAEIOU":
        if caracter == c:
            return True
    return False

def vocales(palabra: str) -> int:
    res: int = 0
    for letra in palabra:
        if esVocal(letra):
            res += 1
    return res

def palabras(texto: str) -> list[str]:
    res: list[str] = []
    buff: str = ""
    for caracter in texto:
        if caracter == ' ':
            if len(buff) > 0:
                res.append(buff)
                buff = ""
            continue
        buff += caracter
    if len(buff) > 0:
        res.append(buff)
    print(res)
    return res

def palabras_por_vocales(texto: str) -> dict[int, int]:
    res: dict[int, int] = {}
    for palabra in palabras(texto):
        clave: int = vocales(palabra)
        if clave not in res.keys():
            res[clave] = 0
        res[clave] += 1
    return res

# Ejercicio 5 (1 punto)
# ¿Por qué en Paradigma Imperativo no existe la transparencia referencial?
# [ ] Utilizamos otro mecanismo de repetición de código, en lugar de recursión usamos la iteración (FOR, WHILE, DO WHILE).
# [x] Tenemos una nueva instrucción, la asignación, que nos permite cambiar el valor de una variable
# [ ] El orden en que se ejecutan las instrucciones del programa es diferente
