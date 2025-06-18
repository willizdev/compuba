from queue import Queue as Cola

# Ej 1

# defino una auxiliar para buscar el máximo aparte
def max_apariciones(n: int, lista: list[int]) -> int:
    """
    Dado un entero y una lista, busca la secuencia mas larga de ese entero
    """
    # acá vamos a ir guardando la cantidad de apariciones de la subsecuencia mas larga
    # encontrada hasta el momento
    maximo:int = 0

    # acá vamos a ir guardando la cantidad de apariciones de la subsecuencia actual
    contador:int = 0
    for elem in lista:
        # si el elemento es igual al que estamos buscando, incrementamos el contador
        if elem == n:
            contador += 1
            # si el contador es mayor al maximo encontrado hasta el momento,
            # lo actualizamos
            if contador > maximo:
                maximo = contador

        # si el elemento no es igual al que estamos buscando
        # reiniciamos el contador
        else:
            contador = 0
    return maximo


# función pertenece

def pertenece(n: int, v: list[int]) -> bool:
    for elem in v:
        if elem == n:
            return True
    return False

# función principal
def maximas_cantidades_consecutivos(v: list[int]) -> dict[int, int]:
    """
    Nos dan una lista de enteros, por ej [1,2,3,1,1,0,0,0,98]

    res es un diccionario con los numeros que aparecen en la lista v
    como clave y los valores asociados son la maxima cantidad de k consecutivos .

    ej:[1,2,3,1,1,0,0,0,98]
    res {1:2, 2:1, 3:1, 0:3, 98:1}

    """
    res: dict[int, int] = {}
    # agregamos todas las claves que va a tener el diccionario

    for elem in v:
        if not pertenece(elem, list(res.keys())):
            res[elem] = 1
    
    for clave in res.keys():
        res[clave] = max_apariciones(clave, v)

    return res


# Ej 2

# función auxiliar para saber si un número es primo
def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# función auxiliar para buscar el máximo de una lista
def maximo(s: list[int]) -> int:
    """
    Recibimos una lista de enteros
    Devolvemos el maximo de la lista
    requiere |s| > 0
    """

    maximo:int = s[0]
    for elem in s:
        if elem > maximo:
            maximo = elem
    return maximo

# función principal
def maxima_cantidad_primos( A: list[list[int]]) -> int:
    """
    Todas las columnas de A tienen a lo sumo res elementos que son primos 
    Existe alguna columna c en A para la cual res de sus elementos son primos

    Es todas las columnas van a tener k primos <= res
    y una columna va a tener k = res

    Es un problema de 1) Contar cantidad de numeros primos en una columna
                      2) Ver el maximo de todos esos
    """
    lista_de_primos: list[int] = []
    largo_fila: int = len(A)

    # si la matriz está vacía no devuelve nada
    if largo_fila == 0:
        return 0
    
    largo_columna: int = len(A[0])

    for j in range(largo_columna):
        cant_primos_en_columna = 0
        for i in range(largo_fila):
            if es_primo(A[i][j]):
               cant_primos_en_columna+=1
        lista_de_primos.append(cant_primos_en_columna)
    
    return maximo(lista_de_primos)

# Ej 3
def tuplas_positivas_y_negativas(c: Cola[tuple[int, int]]) -> None:
    """
    c no tiene tuplas repetidas

    c tiene exactamente las mismas tuplas pos y neg can las que entró
    pero NO contiene las nulas

    No hay ninguna tupla negativa antes que una positiva

    Las tuplas preservan su orden relativo en el que entraron

    tupla pos: producto de elems > 0
    tupla neg: producto de elems < 0
    tupla nula: producto de elems = 0

    """
    pos: Cola[tuple[int, int]] = Cola()
    neg: Cola[tuple[int, int]] = Cola()

    while not c.empty():
        elem = c.get()
        if elem[0]*elem[1] > 0:
            pos.put(elem)
        elif elem[0]*elem[1] < 0:
            neg.put(elem)

    # primero ponemos todas las tuplas positivas
    # luego las negativas 

    while not pos.empty():
        c.put(pos.get())

    while not neg.empty():
        c.put(neg.get())
    

# Ej 4

def resolver_cuenta(s: str) -> float:
    """
    un s valido es '+1.1'

    s -> '1.1'-> 1.1
    s -> '-1.1' -> -1.1
    s -> '+1.1+26' -> 27.1
    s -> '-1.1+4.6' -> 3.5
    """
    # si el string es vacio
    if len(s) == 0:
        return 0
    
    cuenta:int = 0
    numero:str = ""
    operaciones:dict[str, int] = {"+": 0, "-": 0}
    es_negativo:bool = False

    for elem in s:
        if elem != "+" and elem != "-":
            numero += elem
        else:
            if numero != "" and es_negativo:
                operaciones["-"] -= float(numero)
                es_negativo = False
            elif numero != "":
                operaciones["+"] += float(numero)

            # reseteamos el valor booleano que nos va a decir
            # si el numero que viene es negativo o positivo
            if numero != "" and elem == "-":
                es_negativo = True
            
            # Si el primer número es negativo
            if numero == "" and elem == "-":
                es_negativo = True
            
            numero = ""

    # Para agregar el último número
    # Es como el ejercicio visto en clase de ver las palabras de una oración
    # que nos quedaba la última palabra sin procesar
    if numero != "" and es_negativo:
        operaciones["-"] -= float(numero)
    elif numero != "":
        operaciones["+"] += float(numero)

    # sumamos las operaciones
    cuenta = operaciones["+"] + operaciones["-"]

    return cuenta