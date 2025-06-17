import math

# ejercicio 1
def imprimir_hola_mundo() -> None:
    print("¡Hola mundo!")

def imprimir_un_verso() -> None:
    print("Hola\nmundo")

def raizDe2() -> float:
    return round(math.sqrt(2), 4)

def factorial_2() -> int:
    return 2

def perimetro() -> float:
    return 2 * math.pi

# ejercicio 2 
def imprimir_saludo(nombre: str) -> None:
    print("Hola", nombre)

def raiz_cuadrada_de(numero: int) -> float:
    return math.sqrt(numero)

def fahrenheit_a_celsius(temp_far: int) -> float:
    return ((temp_far - 32) * 5) / 9

def imprimir_dos_veces(estribillo: str) -> None:
    print(estribillo * 2)

def es_multiplo_de(n: int, m: int) -> bool:
    return n % m == 0

def es_par(numero: int) -> bool:
    return es_multiplo_de(numero, 2)

def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    porciones: int = comensales * min_cant_de_porciones
    while porciones % 8 != 0:
        porciones += 1
    return porciones / 8

# ejercicio 3
def alguno_es_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 or numero2 == 0

def ambos_son_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 and numero2 == 0

def es_nombre_largo(nombre: str) -> bool:
    return 3 <= len(nombre) and len(nombre) <= 8

def es_bisiesto(año: int) -> bool:
    return es_multiplo_de(año, 400) or (es_multiplo_de(año, 4) and not es_multiplo_de(año, 100))

# ejercicio 4
def peso_pino(altura_m: int) -> int:
    if altura_m <= 3:
        return altura_m * 300
    return (altura_m - 3) * 200 + 900

def es_peso_util(peso_kg: int) -> bool:
    return 400 < peso_kg and peso_kg < 1000

def sirve_pino(altura_m: int) -> bool:
    return es_peso_util(peso_pino(altura_m))

# ejercicio 5
def devolver_el_doble_si_es_par(numero: int) -> int:
    if es_par(numero):
        return 2 * numero
    return numero

def devolver_valor_si_es_par_si_no_el_que_sigue(numero: int) -> int:
    if es_par(numero):
        return numero
    return numero + 1

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if es_multiplo_de(numero, 3):
        return 2 * numero
    if es_multiplo_de(numero, 9):
        return 3 * numero
    return numero

def lindo_nombre(nombre: str) -> str:
    if len(nombre) >= 5:
        "Tu nombre tiene muchas letras!"
    return "Tu nombre tiene menos de 5 caracteres"

def elRango(numero: int) -> None:
    if numero < 5:
        print("Menor a 5")
    elif 10 < numero and numero < 20:
        print("Entre 10 y 20")
    elif numero > 20:
        print("Mayor a 20")

def vacaciones_o_trabajar(sexo: chr, edad: int) -> None:
    if edad < 18 or edad >= 65 or (edad >= 60 and sexo == 'F'):
        print("Andá de vacaciones")
    else:
        print("Te toca trabajar")

# ejercicio 6
def while_imprimir_1_al_10() -> None:
    indice: int = 1
    while indice <= 10:
        print(indice)
        indice += 1

def while_imprimir_pares_entre_10_y_40() -> None:
    indice: int = 10
    while indice <= 40:
        print(indice)
        indice += 2

def while_imprimir_eco_10_veces() -> None:
    indice: int = 0
    while indice < 10:
        print("eco")

def while_cuenta_regresiva(numero: int) -> None:
    while numero > 0:
        print(numero)
        numero -= 1
    print("Despegue")

def while_monitorear_viaje(partida: int, llegada: int) -> None:
    while partida > llegada:
        partida -= 1
        print("Viajó un año al pasado, estamos en el año:", partida)

def while_viaje_hacia_aristoteles(partida: int) -> None:
    while partida > -384 + 10:
        partida -= 20
        print("Viajó 20 años al pasado, estamos en el año:", partida)

# ejercicio 7
def range_imprimir_1_al_10() -> None:
    for i in range(1, 11, 1):
        print(i)

def range_imprimir_pares_entre_10_y_40() -> None:
    for i in range(10, 41, 2):
        print(i)

def range_imprimir_eco_10_veces() -> None:
    for i in range(0, 10, 1):
        print("eco")

def range_cuenta_regresiva(numero: int) -> None:
    for i in range(numero, 0, -1):
        print(i)
    print("Despegue")

def range_monitorear_viaje(partida: int, llegada: int) -> None:
    for año in range(partida - 1, llegada - 1, -1):
        print("Viajó un año al pasado, estamos en el año:", año)

def range_viaje_hacia_aristoteles(partida: int) -> None:
    for año in range(partida - 20, -384 + 10 - 20, -20):
        print("Viajó 20 años al pasado, estamos en el año:", año)

# ejercicio 8
def ejecucion_simbolica_1():
    x = 5
    y = 7
    x = x + y # x = 5 + 7
    # x = 13
    # y = 7

def ejecucion_simbolica_2():
    x = 5
    y = 7 
    z = x + y # z = 5 + 7
    # z = 13
    y = z * 2 # y = 13 * 2
    # y = 26
    # x = 5

def ejecucion_simbolica_3():
    x = 5
    y = 7 
    x = "hora"
    y = x * 2 # y = "hora" * 2
    # y = "horahora"
    # x = "hora"

def ejecucion_simbolica_4():
    x = False
    res = not(x) # res = True
    # x = False

def ejecucion_simbolica_5():
    x = False
    x = not(x) # x = not(False)
    # x = True

def ejecucion_simbolica_6():
    x = True
    y = False
    res = x and y # res = True and False
    # res = False
    x = res and x # x = False and True
    # x = False
    # y = False

# ejercicio 9
def ejercicio_9():
    def rt(x: int, g: int) -> int:
        g = g + 1
        return x + g
    g: int = 0
    def ro(x: int) -> int:
        global g
        g = g + 1
        return x + g
    # 1. al evaluar ro(1) 3 veces seguidas, g = 3
    #    el resultado que retorna es: 2, 3, 4
    # 2. al evaluar rt(1, 0) 3 veces seguidas, g = 0
    #    el resultado que retorna es: 2, 2, 2

# ejecucion simbolica ejercicio 9

# 1. evaluar ro(1) 3 veces seguidas
# g = 0 -> primera llamada
# g = g + 1
# return 2
# g = 1 -> segunda llamada
# g = g + 1
# return 3
# g = 2 -> tercera llamada
# g = g + 1
# return 4
# g = 3 -> resultado final

# 2. evaluar rt(1, 0) 3 veces seguidas
# g = 0 (g global)
# g = g + 1 (g local)
# g = 0 + 1
# g = 1
# return 1 + g
# return 2
# como no modifica la variable g global
# ocurre lo mismo para las tres llamadas
