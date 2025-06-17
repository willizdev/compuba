from queue import LifoQueue as Pila
from queue import Queue as Cola
from random import randint

# funciones auxiliares
def print_pila(p: Pila[int]) -> None:
    p_aux: Pila[int]= Pila()
    
    while not p.empty():
        elem: int = p.get()
        p_aux.put(elem)
        print(elem, end=" - ")
    print()
 
    while not p_aux.empty():
        p.put(p_aux.get())

def print_cola(c: Cola[int]) -> None:
    c_aux: Cola[int]= Cola()
    
    while not c.empty():
        elem: int = c.get()
        c_aux.put(elem)
        print(elem, end=" | ")
 
    while not c_aux.empty():
        c.put(c_aux.get())

# ejercicio 1
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    p: Pila[int] = Pila()
    for i in range(0, cantidad):
        p.put(randint(desde, hasta))
    return p

# ejercicio 2
def cantidad_elementos(p: Pila[int]) -> int:
    p_aux: Pila[int] = Pila()
    cantidad: int = 0

    while not p.empty():
        p_aux.put(p.get())
        cantidad += 1

    while not p_aux.empty():
        p.put(p_aux.get())

    return cantidad

# ejercicio 3
def buscar_el_maximo(p: Pila[int]) -> int:
    p_aux: Pila[int] = Pila()
    maximo: int = p.get()
    p_aux.put(maximo)

    while not p.empty():
        n: int = p.get()
        p_aux.put(n)
        if n > maximo:
            maximo = n

    while not p_aux.empty():
        p.put(p_aux.get())

    return maximo

# ejercicio 4
def buscar_nota_maxima(p: Pila[(str, int)]) -> (str, int):
    p_aux: Pila[(str, int)] = Pila()
    nota_maxima: (str, int) = p.get()
    p_aux.put(nota_maxima)

    while not p.empty():
        n: int = p.get()
        p_aux.put(n)
        if n[1] > nota_maxima[1]:
            nota_maxima = n

    while not p_aux.empty():
        p.put(p_aux.get())

    return nota_maxima

# ejercicio 5
def esta_bien_balanceada(s: list[chr]) -> bool:
    parentesis: Pila[char] = Pila()
    for c in s:
        if c == '(':
            parentesis.put(c)
            continue
        if c == ')':
            if parentesis.empty():
                return False
            parentesis.get()
            continue
    return parentesis.empty()

# ejercicio 6
def is_operator(s: str) -> bool:
    for c in "+-*/":
        if c == s:
            return True
    return False

def evaluar_expresion(s: list[chr]) -> int:

    tokens: list[str] = []
    buff: str = ""
    for c in s:
        if c == ' ':
            tokens.append(buff)
            buff = ""
            continue
        buff += c
    tokens.append(buff)

    ops: Pila[int] = Pila()
    for t in tokens:
        if not is_operator(t):
            ops.put(int(t))
            continue

        derecha: int = ops.get()
        izquierda: int = ops.get()

        if t == '+':
            ops.put(izquierda + derecha)
            continue
        if t == '-':
            ops.put(izquierda - derecha)
            continue
        if t == '*':
            ops.put(izquierda * derecha)
            continue
        if t == '/':
            ops.put(izquierda / derecha)
            continue

    return ops.get()

# ejercicio 7
def intercalar(p1: Pila[any], p2: Pila[any]) -> Pila[any]:
    p1_aux: Pila[any] = Pila()
    p2_aux: Pila[any] = Pila()
    res: Pila[any] = Pila()

    while not p1.empty():
        p1_aux.put(p1.get())
        p2_aux.put(p2.get())

    while not p1_aux.empty():
        e1: any = p1_aux.get()
        e2: any = p2_aux.get()
        p1.put(e1)
        p2.put(e2)
        res.put(e1)
        res.put(e2)
    
    return res

# ejercicio 8
def cola_generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    c: Cola[int] = Cola()
    for i in range(0, cantidad):
        c.put(randint(desde, hasta))
    return c

# ejercicio 9
def cola_cantidad_elementos(c: Cola[int]) -> int:
    c_aux: Cola[int] = Cola()
    cantidad: int = 0

    while not c.empty():
        c_aux.put(c.get())
        cantidad += 1

    while not c_aux.empty():
        c.put(c_aux.get())

    return cantidad

# ejercicio 10
def cola_buscar_el_maximo(c: Cola[int]) -> int:
    c_aux: Cola[int] = Cola()
    maximo: int = c.get()
    c_aux.put(maximo)

    while not c.empty():
        n: int = c.get()
        c_aux.put(n)
        if n > maximo:
            maximo = n

    while not c_aux.empty():
        c.put(c_aux.get())

    return maximo

# ejercicio 11
def buscar_nota_minima(c: Cola[(str, int)]) -> (str, int):
    c_aux: Cola[(str, int)] = Cola()
    nota_minima: (str, int) = c.get()
    c_aux.put(nota_minima)

    while not c.empty():
        n: int = c.get()
        c_aux.put(n)
        if n[1] < nota_minima[1]:
            nota_minima = n

    while not c_aux.empty():
        c.put(c_aux.get())

    return nota_minima

# ejercicio 12
def cola_intercalar(c1: Cola[any], c2: Cola[any]) -> Cola[any]:
    c1_aux: Cola[any] = Cola()
    c2_aux: Cola[any] = Cola()
    res: Cola[any] = Cola()

    while not c1.empty():
        c1_aux.put(c1.get())
        c2_aux.put(c2.get())

    while not c1_aux.empty():
        e1: any = c1_aux.get()
        e2: any = c2_aux.get()
        c1.put(e1)
        c2.put(e2)
        res.put(e1)
        res.put(e2)
    
    return res

# ejercicio 13
def armar_secuencia_de_bingo() -> Cola[int]:
    numeros: list[int] = []
    for i in range(0, 100):
        numeros.append(i)

    res: Cola[int] = Cola()
    while len(numeros) > 0:
        i: int = randint(0, len(numeros) - 1)
        n: int = numeros.pop(i)
        res.put(n)

    return res

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:

    jugadas: int = 0
    bingo: int = 0

    def pertenece(lista: list[int], numero: int):
        for n in lista:
            if n == numero:
                return True
        return False

    while not bolillero.empty() and bingo < 12:
        if pertenece(carton, bolillero.get()):
            bingo += 1
        jugadas += 1
    return jugadas

# ejercicio 14
def pacientes_urgentes(c: Cola[(int, str, str)]) -> int:
    urgentes: int = 0
    for paciante in c:
        if paciante[0] < 4:
            urgentes += 1
    return urgentes

# ejercicio 15
def atencion_a_clientes(c: Cola[(str, int, bool, bool)]) -> Cola[(str, int, bool, bool)]:
    c_aux1: Cola[(str, int, bool, bool)] = Cola()
    c_aux2: Cola[(str, int, bool, bool)] = Cola()

    c_res: Cola[(str, int, bool, bool)] = Cola()

    while not c.empty():
        c_aux1.put(c.get())
    
    while not c_aux1.empty():
        e: (str, int, bool, bool) = c_aux1.get()
        c.put(e)
        c_aux2.put(e)

    while not c_aux2.empty():
        e: (str, int, bool, bool) = c_aux2.get()
        if e[3]:
            c_res.put(e)
            continue
        c_aux1.put(e)

    while not c_aux1.empty():
        e: (str, int, bool, bool) = c_aux1.get()
        if e[2]:
            c_res.put(e)
            continue
        c_aux2.put(e)

    while not c_aux2.empty():
        c_res.put(c_aux2.get())

    return c_res
