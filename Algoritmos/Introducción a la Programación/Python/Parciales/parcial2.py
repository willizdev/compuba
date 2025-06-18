# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

def ultima_aparicion(s: list, e: int) -> int:
    for i in range(len(s) - 1, -1, -1):
        if s[i] == e:
            return i

# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }

def indice(s: list[int], n: int) -> int:
    for i in range(0, len(s)):
        if s[i] == n:
            return i
    return -1

def elementos_exclusivos(s: list[int], t: list[int]) -> list[int]:
    res: list[int] = s
    for i in range(0, len(t)):
        j: int = indice(res, t[i])
        if j != -1:
            res.pop(j)
            continue
        res.append(t[i])
    return res

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

def contar_traducciones_iguales(ingles: dict[str, str], aleman: dict[str, str]) -> int:
    res: int = 0
    for clave, valor in ingles.items():
        if not clave in aleman.keys():
            continue
        if ingles[clave] == aleman[clave]:
            res += 1
    return res

# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

def convertir_a_diccionario(lista: list[int]) -> dict[int, int]:
    res: dict[int, int] = {}

    for numero in lista:
        if not numero in res.keys():
            res[numero] = 0
        res[numero] += 1

    return res
