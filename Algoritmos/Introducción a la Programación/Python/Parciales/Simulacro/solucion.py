from queue import Queue as Cola

# ejercicio 1
def maximas_cantidades_consecutivos(v: list[int]) -> dict[int, int]:
    res: dict[int, int] = {}

    for i in range(0, len(v)):

        numero: int = v[i]
        consec: int = 0

        for j in range(i, len(v)):
            if v[j] != numero:
                break
            consec += 1
        
        if not numero in res.keys():
            res[numero] = consec
        elif consec > res[numero]:
            res[numero] = consec

    return res

# ejercicio 2
def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def maximo(lista: list[int]) -> int:
    m: int = lista[0]
    for numero in lista:
        if numero > m:
            m = numero
    return m

def maxima_cantidad_primos(A: list[list[int]]) -> int:

    if len(A) == 0 or len(A[0]) == 0:
        return 0

    primos_col: list[int] = []

    for col in range(0, len(A[0])):
        primos: int = 0
        for fila in range(0, len(A)):
            if es_primo(A[fila][col]):
                primos += 1
        primos_col.append(primos)

    return maximo(primos_col)

# ejercicio 3
def multiplicar_tupla(tupla: (int, int)) -> int:
    return tupla[0] * tupla[1]

def tuplas_positivas_y_negativas(c: Cola[(int, int)]) -> None:
    aux_1: Cola[(int, int)] = Cola()
    aux_2: Cola[(int, int)] = Cola()

    while not c.empty():
        aux_1.put(c.get())

    while not aux_1.empty():
        t: (int, int) = aux_1.get()
        if t[0] * t[1] > 0:
            c.put(t)
        elif t[0] * t[1] < 0:
            aux_2.put(t)
    
    while not aux_2.empty():
        c.put(aux_2.get())

# ejercicio 4
def sumar(lista: list[float]) -> float:
    res: float = 0
    for numero in lista:
        res += numero
    return res

def lexer(s: str) -> list[str]:
    res: list[str] = []
    buff: str = ""

    for c in s:
        if c == '+' or c == '-':
            if len(buff) > 0:
                res.append(buff)
                buff = ""
            res.append(c)
            continue
        buff += c
        
    if len(buff) > 0:
        res.append(buff)
    return res

def parser(tokens: list[str]) -> list[float]:
    multiplier: int = 1
    res: list[float] = []

    for token in tokens:
        print(token)
        if token == '+':
            multiplier = 1
            continue
        if token == '-':
            multiplier = -1
            continue
        res.append(multiplier * float(token))
    
    return res

def resolver_cuenta(s: str) -> float:
    return sumar(parser(lexer(s)))
