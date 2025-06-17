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

# ejercicio 16
def dict_contiene(d: dict[any], k: any) -> bool:
    for key in d.keys():
        if k == key:
            return True
    return False

def calcular_promedio_por_estudiante(notas: list[(str, float)]) -> dict[str, float]:
    promedios: dict[str, float] = {}
    contador: dict[str, int] = {}

    for estudiante in notas:
        nombre: str = estudiante[0]
        nota: float = estudiante[1]

        if not dict_contiene(contador, nombre):
            contador[nombre] = 1
            promedios[nombre] = nota
            continue
        
        contador[nombre] += 1
        promedios[nombre] += nota

    for nombre, nota in promedios.items():
        promedios[nombre] = nota / contador[nombre]

    return promedios

# ejercicio 17
historiales: dict[str, Pila[str]] = {}

def visitar_sitio(historiales: dict[str, Pila[str]], usuario: str, sitio: str) -> None:
    if not dict_contiene(historiales, usuario):
        historiales[usuario] = Pila()
    historiales[usuario].put(sitio)

def navegar_atras(historiales: dict[str, Pila[str]], usuario: str) -> str:
    return historiales[usuario].get()

# ejercicio 18
def agregar_producto(inventario: dict[str, int | float], nombre: str, precio: float, cantidad: int) -> None:
    inventario[nombre] = {
        "precio": precio,
        "cantidad": cantidad
    }

def actualizar_stock(inventario: dict[str, int | float], nombre: str, cantidad: int) -> None:
    inventario[nombre]["cantidad"] = cantidad

def calcular_valor_inventario(inventario: dict[str, int | float]) -> float:
    valor: float = 0
    for producto in inventario.values():
        valor += producto["cantidad"] * producto["precio"]
    return valor

# ejercicio 19
def contar_lineas(nombre_archivo: str) -> int:
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    return len(lineas)

def palabras(texto: str) -> list[str]:
    def es_palabra(caracter: chr) -> bool:
        minusculas: str = "abcdefghijklmnopqrstuvwxyz"
        mayusculas: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeros: str = "0123456789"
        letras: str = minusculas + mayusculas + numeros + "-_"
        for c in letras:
            if caracter == c:
                return True
        return False

    lista: list[str] = []
    buff: str = ""

    for c in texto:
        if es_palabra(c):
            buff += c
            continue
        if len(buff) > 0:
            lista.append(buff)
            buff = ""

    if len(buff) > 0:
        lista.append(buff)
    return lista

def existe_palabra(nombre_archivo: str, palabra: str) -> bool:
    archivo = open(nombre_archivo, "r")
    lista_palabras: list[str] = palabras(archivo.read())
    
    for p in lista_palabras:
        if palabra == p:
            return True

    archivo.close()
    return False

def cantidad_de_apariciones(nombre_archivo: str, palabra: str) -> int:
    archivo = open(nombre_archivo, "r")
    lista_palabras: list[str] = palabras(archivo.read())
    apariciones: int = 0
    
    for p in lista_palabras:
        if palabra == p:
            apariciones += 1

    archivo.close()
    return apariciones

# ejercicio 20
def agrupar_por_longitud(nombre_archivo: str) -> dict[int, int]:
    archivo = open(nombre_archivo, "r")
    lista_palabras: list[str] = palabras(archivo.read())
    longitud: dict[int, int] = {}

    for p in lista_palabras:
        if not dict_contiene(longitud, len(p)):
            longitud[len(p)] = 1
            continue
        longitud[len(p)] += 1

    archivo.close()
    return longitud

# ejercicio 21
def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    archivo = open(nombre_archivo, "r")
    lista_palabras: list[str] = palabras(archivo.read())
    dict_palabras: dict[str, int] = {}
    
    for p in lista_palabras:
        if not dict_contiene(dict_palabras, p):
            dict_palabras[p] = 1
            continue
        dict_palabras[p] += 1

    palabra: str = ""
    frecuencia: int = 0

    for p, f in dict_palabras.items():
        if f > frecuencia:
            palabra = p
            frecuencia = f

    archivo.close()
    return palabra

# ejercicio 22
def clonar_sin_comentarios(nombre_archivo_entrada: str, nombre_archivo_salida: str) -> None:
    entrada = open(nombre_archivo_entrada, "r")
    salida = open(nombre_archivo_salida, "w")
    lineas: list[str] = []

    for linea in entrada.readlines():
        if linea[0] == '#':
            continue
        lineas.append(linea)
    
    salida.writelines(lineas)
    entrada.close()
    salida.close()

# ejercicio 23
def invertir_lineas(nombre_archivo_entrada: str, nombre_archivo_salida: str) -> None:
    entrada = open(nombre_archivo_entrada, "r")
    salida = open(nombre_archivo_salida, "w")
    lineas: list[str] = []
    buff: str = ""

    for caracter in entrada.read():
        if caracter == '\n':
            lineas.append(buff)
            buff = ""
            continue
        buff += caracter
    lineas.append(buff)

    for i in range(0, int(len(lineas) / 2)):
        temp: str = lineas[i]
        lineas[i] = lineas[len(lineas) - 1 - i]
        lineas[len(lineas) - 1 - i] = temp

    for i in range(0, len(lineas) - 1):
        lineas[i] += '\n'
    
    salida.writelines(lineas)
    entrada.close()
    salida.close()

# ejercicio 24
def agregar_frase_al_final(nombre_archivo: str, frase: str) -> None:
    archivo = open(nombre_archivo, "a")
    archivo.write('\n' + frase)
    archivo.close()

# ejercicio 25
def agregar_frase_al_principio(nombre_archivo: str, frase: str) -> None:
    archivo_leer = open(nombre_archivo, "r")
    contenido: str = archivo_leer.read()
    archivo_leer.close()

    archivo_escribir = open(nombre_archivo, "w")
    archivo_escribir.write(frase + '\n' + contenido)
    archivo_escribir.close()

# ejercicio 26
def listar_textos_de_archivo(nombre_archivo: str) -> list[str]:

    def es_legible(caracter: chr) -> bool:
        minusculas: str = "abcdefghijklmnopqrstuvwxyz"
        mayusculas: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeros: str = "0123456789"
        letras: str = minusculas + mayusculas + numeros + " _"
        for c in letras:
            if caracter == c:
                return True
        return False

    archivo = open(nombre_archivo, "rb")
    secuencia: list[bytes] = archivo.read()
    textos: list[str] = []
    buff: str = ""

    for c in secuencia:
        if es_legible(chr(c)):
            buff += chr(c)
            continue
        if len(buff) >= 5:
            textos.append(buff)
        buff = ""
    if len(buff) >= 5:
        textos.append(buff)

    archivo.close()
    return textos

# ejercicio 27
def calcular_promedio_por_estudiantes(nombre_archivo_notas: str, nombre_archivo_promedio: str) -> None:
    archivo_notas = open(nombre_archivo_notas, "r")
    archivo_promedio = open(nombre_archivo_promedio, "w")

    def split_csv(texto: str) -> list[str]:
        lista: list[str] = []
        buff: str = ""
        for c in texto:
            if c == ',':
                lista.append(buff)
                buff = ""
                continue
            buff += c
        lista.append(buff)
        return lista

    notas: dict[str, float] = {}
    contador: dict[str, int] = {}
    promedios: list[str] = []

    for linea in archivo_notas.readlines():
        estudiante: list[str] = split_csv(linea)
        if not dict_contiene(notas, estudiante[0]):
            notas[estudiante[0]] = 0
            contador[estudiante[0]] = 0
        notas[estudiante[0]] += float(estudiante[3])
        contador[estudiante[0]] += 1

    for k in notas.keys():
        promedios.append(k + ',' + str(notas[k] / contador[k]))
    for i in range(0, len(promedios) - 1):
        promedios[i] += '\n'
    archivo_promedio.writelines(promedios)

    archivo_notas.close()
    archivo_promedio.close()
