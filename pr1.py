"""
Asignatura: GIW
Práctica 1
Grupo: 11
Autores: RISHI PURSNANI MIRPURI, ALBA BASTIDA ÁLVAREZ, LUCAS SÁNCHEZ MARTÍN

Declaramos que esta solución es fruto exclusivamente de nuestro trabajo personal. No hemos
sido ayudados por ninguna otra persona o sistema automático ni hemos obtenido la solución
de fuentes externas, y tampoco hemos compartido nuestra solución con otras personas
de manera directa o indirecta. Declaramos además que no hemos realizado de manera
deshonesta ninguna otra actividad que pueda mejorar nuestros resultados ni perjudicar los
resultados de los demás.
"""

# Ejercicio 1

def dimension(matriz):
    if not isinstance(matriz, list) or not matriz:
        return None
    if not isinstance(matriz[0], list):
        return None
    columnas = len(matriz[0])

    # revisamos que las tpdas las filas tienen el mismo tamaño
    for fila in matriz:
        if not isinstance(fila, list) or len(fila) != columnas:
            return None
    return len(matriz), columnas


def es_cuadrada(matriz):
    tamano = dimension(matriz)
    if tamano is None:
        return False
    
    if tamano[0] == tamano[1]:
        return True
    return False


def es_simetrica(matriz):
    if not es_cuadrada(matriz):
        return False
    
    # revisamos los dos lados de la diagonal para ver si son iguales o no
    for fila, valores in enumerate(matriz):
        #empezamos en fila+1 ya que comparamos los elementos por encima de la diagonal para no repetir comparaciones ya hechas
        for columna in range(fila + 1, len(matriz)):
            if valores[columna] != matriz[columna][fila]:
                return False
    return True


def multiplica_escalar(matriz, k):
    if dimension(matriz) is None:
        return None
    
    # crea filas nuevas para no cambiar la matriz original
    res = []
    for fila in matriz:
        nueva_fila = []

        for elemento in fila:
            nueva_fila.append(elemento * k)
        res.append(nueva_fila)
    return res


def suma(matriz1, matriz2):
    tamano = dimension(matriz1)

    # comprobamos que las matrices sonb del mismo tamaño ya que sino no se peude
    if tamano is None or tamano != dimension(matriz2):
        return None
    resultado = []

    filas, columnas = tamano
    for fila in range(filas):

        nueva_fila = []
        for columna in range(columnas):
            nueva_fila.append(matriz1[fila][columna] + matriz2[fila][columna])
        resultado.append(nueva_fila)
    return resultado


# Ejercicio 2
def validar(grafo):
    if not isinstance(grafo, dict):
        return False

    if "nodos" not in grafo or "aristas" not in grafo:
        return False

    nodos = grafo["nodos"]
    aristas = grafo["aristas"]

    if not isinstance(nodos, list) or not isinstance(aristas, dict):
        return False

    if not nodos or len(nodos) != len(set(nodos)):
        return False

    # revisamos que cada nodo tenga su lista de aristassa
    for nodo in nodos:
        if nodo not in aristas or not isinstance(aristas[nodo], list):
            return False

        destinos = aristas[nodo]

        if len(destinos) != len(set(destinos)):
            return False

        for destino in destinos:
            if destino not in nodos:
                return False
    return True


def grado_entrada(grafo, nodo):
    if not validar(grafo) or nodo not in grafo["nodos"]:
        return -1
    grado = 0

    # cada lista que contiene el nodo aporta una arista de entrada.
    for destinos in grafo["aristas"].values():
        if nodo in destinos:
            grado += 1
    return grado

# los nodos los procesamos a la que se descubren, asi recorremos primero los que esten a menos distancia a mas
def distancia(grafo, nodo):
    if not validar(grafo) or nodo not in grafo["nodos"]:
        return None
    distancias = {}

    for destino in grafo["nodos"]:
        distancias[destino] = -1
    distancias[nodo] = 0

    pendientes = [nodo]
    indice = 0

    # vamos recorriendo los nodos por niveles para ver los caminos mas cortos 
    while indice < len(pendientes):
        origen = pendientes[indice]
        indice += 1
        
        for destino in grafo["aristas"][origen]:
            # si descrubrimos un nodo lo añadimos
            if distancias[destino] == -1:
                distancias[destino] = distancias[origen] + 1
                pendientes.append(destino)
    return distancias
