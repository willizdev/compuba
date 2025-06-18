from queue import LifoQueue as Pila
from queue import Queue as Cola

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
def stock_productos(stock_cambios: list[(str, int)]) -> dict[str, (int, int)]:
    productos: dict[str, (int, int)] = {}

    for stock in stock_cambios:
        nombre: str = stock[0]
        cantidad: str = stock[1]

        if nombre not in productos.keys():
            productos[nombre] = (cantidad, cantidad)
            continue
        if cantidad > productos[nombre][1]:
            productos[nombre] = (productos[nombre][0], cantidad)
            continue
        if cantidad < productos[nombre][0]:
            productos[nombre] = (cantidad, productos[nombre][1])
            continue
    return productos

# ejercicio 2
def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    def es_primo(numero: int) -> bool:
        if numero < 2:
            return False
        for i in range(numero - 1, 1, -1):
            if numero % i == 0:
                return False
        return True

    codigos_primos: list[int] = []

    for codigo in codigos_barra:
        if es_primo(codigo % 1000):
            codigos_primos.append(codigo)

    return codigos_primos

# ejercicio 3
def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    indice: int = 0
    subsecuencia: int = 1

    for i in range(0, len(tipos_pacientes_atendidos)):
        mascota: str = tipos_pacientes_atendidos[i]
        if mascota != "perro" and mascota != "gato":
            continue
        s: int = 0
        for j in range(i, len(tipos_pacientes_atendidos)):
            if tipos_pacientes_atendidos[j] != mascota:
                break
            s += 1
        if s > subsecuencia:
            subsecuencia = s
            indice = i

    return indice

# ejercicio 4
def transpose(matriz: list[list[any]]) -> list[list[any]]:
    res: list[list[any]] = []
    for i in range(0, len(matriz[0])):
        fila: list[any] = []
        for j in range(0, len(matriz)):
            fila.append(matriz[j][i])
        res.append(fila)
    return res

def un_responsable_por_turno(grilla_horaria: list[list[str]]) -> list[(bool, bool)]:
    tabla: list[list[str]] = transpose(grilla_horaria)
    turnos: list[(bool, bool)] = []

    for dia in tabla:
        turno_maniana: bool = dia[0] == dia[1] and dia[0] == dia[2] and dia[0] == dia[3]
        turno_tarde: bool = dia[4] == dia[5] and dia[4] == dia[6] and dia[4] == dia[7]
        turnos.append((turno_maniana, turno_tarde))

    return turnos

# ejercicio 5
def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, (int, float)]:
    promedio: dict[str, (int, float)] = {}
    for nombre, salidas in registro.items():
        salas: int = 0
        minutos: int = 0
        for s in salidas:
            if 0 < s and s < 61:
                salas += 1
                minutos += s
        promedio[nombre] = (salas, minutos / salas)
    return promedio

# ejercicio 6
def tiempo_mas_rapido(tiempos_salas: list[int]) -> int:
    indice: int = -1
    record: int = 61
    for i in range(0, len(tiempos_salas)):
        tiempo: int = tiempos_salas[i]
        if tiempo < 1 or tiempo > 60:
            continue
        if tiempo < record:
            indice = i
            record = tiempo
    return indice

# ejercicio 7
def racha_mas_larga(tiempos: list[int]) -> (int, int):
    racha: int = 0
    inicio: int = 0
    fin: int = 0
    for i in range(0, len(tiempos)):
        escapes: int = 0
        f: int = i
        for j in range(i, len(tiempos)):
            if not (1 <= tiempos[j] and tiempos[j] <= 60):
                break
            f = j
            escapes += 1
        if escapes > racha:
            racha = escapes
            inicio = i
            fin = f
    return (inicio, fin)

# ejercicio 8
def escape_en_solitario(amigos_por_salas: list[list[int]]) -> list[int]:
    indices: list[int] = []

    for i in range(0, len(amigos_por_salas)):
        sala = amigos_por_salas[i]
        if sala[0] + sala[1] + sala[3] == 0 and sala[2] != 0:
            indices.append(i)

    return indices

# ejercicio 9
def torneo_de_gallinas(estrategias: dict[str, str]) -> dict[str, int]:
    resultados: dict[str, int] = {}

    def desvio(estrategia: str) -> bool:
        if estrategia == "me desvío siempre":
            return True
        if estrategia == "me la banco y no me desvío":
            return False

    for jugador in estrategias.keys():
        resultados[jugador] = 0

    e: list[(str, str)] = list(estrategias.items())

    for i in range(0, len(e)):
        jugador: str = e[i]

        for j in range(i + 1, len(e)):
            oponente: str = e[j]

            if desvio(jugador[1]) and desvio(oponente[1]):
                resultados[jugador[0]] -= 10
                resultados[oponente[0]] -= 10

            elif not desvio(jugador[1]) and not desvio(oponente[1]):
                resultados[jugador[0]] -= 5
                resultados[oponente[0]] -= 5

            elif not desvio(jugador[1]) and desvio(oponente[1]):
                resultados[jugador[0]] += 10
                resultados[oponente[0]] -= 15

            elif desvio(jugador[1]) and not desvio(oponente[1]):
                resultados[jugador[0]] -= 15
                resultados[oponente[0]] += 10
    
    return resultados

# ejercicio 10
def reordenar_cola_priorizando_vips(filaClientes: Cola[(str, str)]) -> Cola[str]:
    aux: Cola[(str, str)] = Cola()
    comun: Cola[str] = Cola()
    vip: Cola[str] = Cola()

    while not filaClientes.empty():
        e: (str, str) = filaClientes.get()
        aux.put(e)
        if e[1] == "vip":
            vip.put(e[0])
            continue
        comun.put(e[0])
    
    while not comun.empty():
        vip.put(comun.get())

    while not aux.empty():
        filaClientes.put(aux.get())

    return vip

# ejercicio 11
def cuantos_sufijos_son_palindromos(texto: str) -> int:
    def invertir(s: str) -> str:
        res: str = ""
        for i in range(len(s) - 1, -1, -1):
            res += s[i]
        return res

    def palindromo(s: str) -> bool:
        return s == invertir(s)

    def sufijos(s: str) -> list[str]:
        res: list[str] = []
        for i in range(0, len(s)):
            buff: str = ""
            for j in range(i, len(s)):
                buff += s[j]
            res.append(buff)
        return res      

    res: int = 0
    for sufijo in sufijos(texto):
        if palindromo(sufijo):
            res += 1
    return res

# ejercicio 12
def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> int:

    def transpose(matriz: list[list[str]]) -> list[list[str]]:
        res: list[list[str]] = []
        for i in range(0, len(matriz[0])):
            fila: list[str] = []
            for j in range(0, len(matriz)):
                fila.append(matriz[j][i])
            res.append(fila)
        return res
    
    def tres_consecutivas(matriz: list[list[str]], c: chr) -> bool:
        for fila in matriz:
            for i in range(0, len(fila) - 2):
                if fila[i] == c and fila[i + 1] == c and fila[i + 2] == c:
                    return True
        return False
    
    tab: list[list[str]] = transpose(tablero)
    print(tab)
    ana: bool = tres_consecutivas(tab, "X")
    beto: bool = tres_consecutivas(tab, "O")

    if ana and beto:
        return 3
    if not ana and beto:
        return 2
    if ana and not beto:
        return 1
    return 0

# ejercicio 13
def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    res: Cola[int] = Cola()
    aux_urgentes: Cola[int] = Cola()
    aux_postergables: Cola[int] = Cola()

    while not urgentes.empty():
        u: int = urgentes.get()
        p: int = postergables.get()
        res.put(u)
        res.put(p)
        aux_urgentes.put(u)
        aux_postergables.put(p)

    while not aux_urgentes.empty():
        urgentes.put(aux_urgentes.get())
        postergables.put(aux_postergables.get())

    return res

# ejercicio 14
def alarma_epidemiologica(registros: list[(int, str)], infecciosas: list[str], umbral: float) -> dict[str, float]:
    contador: dict[str, int] = {}
    res: dict[str, float] = {}

    for registro in registros:
        enfermedad: str = registro[1]
        if enfermedad in infecciosas:
            if not enfermedad in contador.keys():
                contador[enfermedad] = 0
            contador[enfermedad] += 1

    for enfermedad, positivos in contador.items():
        porcentaje: float = positivos / len(registros)
        if porcentaje >= umbral:
            res[enfermedad] = porcentaje
    return res

# ejercicio 15
def empleados_del_mes(horas: dict[int, list[int]]) -> list[int]:

    def suma(l: list[int]) -> int:
        s: int = 0
        for i in l:
            s += i
        return s

    res: list[int] = []
    maximo: int = 0

    for h in horas.values():
        s: int = suma(h)
        if s > maximo:
            maximo = s

    for empleado, tiempo in horas.items():
        if suma(tiempo) == maximo:
            res.append(empleado)

    return res

# ejercicio 16
def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    res: list[float] = []
    for piso in camas_por_piso:
        ocupadas: int = 0
        for cama in piso:
            if cama:
                ocupadas += 1
        res.append(ocupadas / len(piso))
    return res
    