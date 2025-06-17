import random

# ejercicio 1
def pertenece(s: list[int], e: int) -> bool:
    for i in s:
        if e == i:
            return True
    return False

def divide_a_todos(s: list[int], e: int) -> bool:
    for i in s:
        if e % i != 0:
            return False
    return True

def suma_total(s: list[int]) -> int:
    suma: int = 0
    for i in s:
        suma += i
    return suma

def maximo(s: list[int]) -> int:
    l: list[int] = s.copy()
    m: int = l.pop()
    for i in l:
        if i > m:
            m = i
    return m

def minimo(s: list[int]) -> int:
    l: list[int] = s.copy()
    m: int = l.pop()
    for i in l:
        if i < m:
            m = i
    return m

def ordenados(s: list[int]) -> bool:
    for i in range(0, len(s) - 1):
        if s[i] >= s[i + 1]:
            return False
    return True

def pos_maximo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    m: int = maximo(s)
    for i in range(0, len(s)):
        if s[i] == m:
            return i

def pos_minimo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    m: int = minimo(s)
    for i in range(0, len(s)):
        if s[i] == m:
            return i

def long_mayorASiete(s: list[str]) -> bool:
    for i in s:
        if len(i) > 7:
            return True
    return False

def es_palindroma(s: str) -> bool:
    l: int = len(s)
    for i in range(0, int(l / 2)):
        if s[i] != s[l - i - 1]:
            return False
    return True

def iguales_consecutivos(s: list[int]) -> bool:
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 1] and s[i] == s[i + 2]:
            return True
    return False

def vocales_distintas(s: str) -> bool:
    vocales: list[int] = [0, 0, 0, 0, 0]
    for i in s:
        if i == 'a': vocales[0] = 1
        if i == 'e': vocales[1] = 1
        if i == 'i': vocales[2] = 1
        if i == 'o': vocales[3] = 1
        if i == 'u': vocales[4] = 1
    return suma_total(vocales) >= 3

def pos_secuencia_ordenada_mas_larga(s: list[int]) -> int:

    def elementos_ordenados_desde_pos(l: list[int], p: int) -> int:
        contador: int = 0
        previo: int = l[p]
        for i in range(p, len(l)):
            if l[i] >= previo:
                contador += 1
                previo = l[i]
            else:
                break
        return contador

    posiciones: list[int] = []
    for i in range(0, len(s)):
        posiciones.append(elementos_ordenados_desde_pos(s, i))
    
    return pos_maximo(posiciones)

def cantidad_digitos_impares(s: list[int]) -> int:
    digitos_impares: int = 0

    for numero in s:
        while numero > 0:
            if (numero % 10) % 2 != 0:
                digitos_impares += 1
            numero = int(numero / 10)

    return digitos_impares

# ejercicio 2
def CerosEnPosicionesPares(s: list[int]) -> None:
    for i in range(0, len(s), 2):
        s[i] = 0

def CerosEnPosicionesPares2(s: list[int]) -> list[int]:
    res: list[int] = []
    for i in range(0, len(s)):
        if i % 2 == 0:
            res.append(0)
            continue
        res.append(s[i])

def sin_vocales(s: str) -> str:
    res: str = ""
    for c in s:
        if not pertenece("aeiou", c):
            res += c
    return res

def reemplaza_vocales(s: str) -> str:
    res: str = ""
    for c in s:
        if pertenece("aeiou", c):
            res += '_'
            continue
        res += c
    return res

def da_vuelta_str(s: str) -> str:
    res: str = ""
    for i in range(len(s) - 1, -1, -1):
        res += s[i]
    return res

def eliminar_repetidos(s: str) -> str:

    def pertenece_sub(l: str, start: int, end: int, char: chr) -> bool:
        for i in range(start, end + 1):
            if l[i] == char:
                return True
        return False

    res: str = ""
    for i in range(0, len(s)):
        if not pertenece_sub(s, 0, i - 1, s[i]):
            res += s[i]
    return res

# ejercicio 3
def resultadoMateria(notas: list[int]) -> int:
    promedio: float = suma_total(notas) / len(notas)
    aprobados: int = 0

    for nota in notas:
        if nota >= 4:
            aprobados += 1
    
    if aprobados == len(notas):
        if promedio >= 7:
            return 1
        if promedio >= 4:
            return 2
    return 3

# ejercicio 4
def saldoActual(movimientos: list[(chr, int)]) -> int:
    saldo: int = 0
    for movimiento in movimientos:
        if movimiento[0] == 'I':
            saldo += movimiento[1]
        elif movimiento[0] == 'R':
            saldo -= movimiento[1]
    return saldo

# ejercicio 5
def pertenece_a_cada_uno_version_1(s: list[list[int]], e: int, res: list[bool]) -> None:
    res.clear()
    for l in s:
        res.append(pertenece(l, e))

def pertenece_a_cada_uno_version_2(s: list[list[int]], e: int, res: list[bool]) -> None:
    res.clear()
    for l in s:
        res.append(pertenece(l, e))

def pertenece_a_cada_uno_version_3(s: list[list[int]], e: int) -> list[bool]:
    res: list[bool] = []
    for l in s:
        res.append(pertenece(l, e))
    return res

# ejercicio 6
def es_matriz(s: list[list[int]]) -> bool:
    if len(s) == 0:
        return False
    if len(s[0]) == 0:
        return False
    for i in s:
        if len(i) != len(s[0]):
            return False
    return True

def filas_ordenadas(m: list[list[int]], res: list[bool]):
    res.clear()
    for c in m:
        res.append(ordenados(c))

def columna(m: list[list[int]], c: int) -> list[int]:
    res: list[int] = []
    for i in range(0, len(m)):
        res.append(m[i][c])
    return res

def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
    res: list[bool] = []
    for i in range(0, len(m[0])):
        res.append(ordenados(columna(m, i)))
    return res

def transponer(m: list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []
    for i in range(0, len(m[0])):
        res.append(columna(m, i))
    return res

def quien_gana_tateti(m: list[list[int]]) -> int:
    O: list[chr] = ['O', 'O', 'O']
    X: list[chr] = ['X', 'X', 'X']

    def diagonal_izq(matriz: list[list[int]]) -> list[int]:
        res: list[int] = []
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[0])):
                if i == j:
                    res.append(matriz[i][j])
        return res

    def diagonal_der(matriz: list[list[int]]) -> list[int]:
        res: list[int] = []
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[0])):
                if i == j:
                    res.append(matriz[i][len(matriz[0]) - 1 - j])
        return res

    def generar_listas(matriz: list[list[int]]) -> list[list[int]]:
        listas: list[list[int]] = matriz.copy()
        for i in range(0, len(listas[0])):
            listas.append(columna(matriz, i))
        listas.append(diagonal_izq(matriz))
        listas.append(diagonal_der(matriz))
        return listas
    
    for f in generar_listas(m):
        if f == O: return 0
        if f == X: return 1
    return 2

# ejercicio 7
def construir_lista_de_nombres() -> list[str]:
    res: list[str] = []
    while True:
        nombre: str = input()
        if nombre == '' or nombre == "listo":
            break
        res.append(nombre)
    return res

def historial_monedero_electronico() -> list[(chr, int)]:
    res: list[str] = []
    while True:
        accion: str = input()
        if accion == 'X':
            break
        if accion == 'C' or accion == 'D':
            monto: int = int(input())
            res.append((accion, monto))
    return res

def siete_y_medio() -> list[int]:
    historial: list[int] = []
    cartas: list[int] = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    puntos: float = 0
    while True:
        print("Ingrese 1 para sacar una carta o 2 para plantarse")
        eleccion: int = int(input())
        if eleccion == 1:
            carta = random.choice(cartas)
            historial.append(carta)
            if carta > 7:
                puntos += 2.5
            else:
                puntos += carta
            print("Carta:", carta)
            print("Puntos:", puntos)
            if puntos > 7.5:
                print("Perdiste!")
                break
        else:
            print("Puntos:", puntos)
            break
    return historial

def fortaleza_de_contrasena(contrasena: str) -> str:
    longitud: int = len(contrasena)

    if longitud < 5:
        return "ROJA"
    
    minusculas: bool = False
    mayusculas: bool = False
    numeros: bool = False

    def existe(c: chr, s: str) -> bool:
        for i in s:
            if c == i:
                return True
        return False

    for caracter in contrasena:
        if existe(caracter, "abcdefghijklmnñopqrstuvwxyz"):
            minusculas = True
        elif existe(caracter, "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
            mayusculas = True
        elif existe(caracter, "0123456789"):
            numeros = True

    if longitud > 8 and minusculas and mayusculas and numeros:
        return "VERDE"
    
    return "AMARILLA"
