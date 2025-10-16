#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

# ===============================
# Parámetros del algoritmo
# ===============================
objetivo = "algoritmo genetico"
poblacion = 100000       # tamaño de la población
letras = "abcdefghijklmnopqrstuvwxyz "
tasa_elimina = 0.2     # porcentaje de eliminación
tasa_padres = 0.3      # porcentaje de padres
tasa_mutacion = 0.1    # probabilidad de mutación
generaciones = 50000     # número máximo de generaciones

# ===============================
# Funciones principales
# ===============================

def generar_poblacion():
    """Genera la población inicial de cadenas aleatorias."""
    return [[0, "".join(random.choice(letras) for _ in range(len(objetivo)))] for _ in range(poblacion)]

def comparar(poblacion, objetivo):
    """Evalúa qué tan cerca está cada individuo del objetivo."""
    for individuo in poblacion:
        palabra = individuo[1]
        individuo[0] = sum(1 for i in range(len(objetivo)) if palabra[i] == objetivo[i])

def eliminar(poblacion):
    """Elimina a los individuos menos aptos."""
    poblacion.sort(key=lambda x: x[0])
    return poblacion[int(len(poblacion)*tasa_elimina):]

def cruza(padre, madre):
    """Crea un hijo mezclando genes del padre y la madre."""
    hijo = ""
    for i in range(len(padre)):
        hijo += padre[i] if random.random() > 0.5 else madre[i]
    # posible mutación
    if random.random() < tasa_mutacion:
        pos = random.randint(0, len(objetivo)-1)
        hijo = hijo[:pos] + random.choice(letras) + hijo[pos+1:]
    return hijo

def crear_hijos(poblacion):
    """Genera nuevos individuos (hijos) a partir de los mejores padres."""
    padres = poblacion[-int(len(poblacion)*tasa_padres):]
    nuevos = []
    for _ in range(int(len(poblacion)*tasa_elimina)):
        padre = random.choice(padres)[1]
        madre = random.choice(padres)[1]
        hijo = cruza(padre, madre)
        nuevos.append([0, hijo])
    poblacion.extend(nuevos)

# ===============================
# Ejecución del algoritmo
# ===============================

def algoritmo_genetico():
    pobl = generar_poblacion()

    for gen in range(1, generaciones + 1):
        comparar(pobl, objetivo)
        pobl = eliminar(pobl)
        crear_hijos(pobl)

        mejor = max(pobl, key=lambda x: x[0])
        print(f"Gen {gen:03d} | Mejor: {mejor[1]} ({mejor[0]}/{len(objetivo)})")

        if mejor[0] == len(objetivo):
            print("Objetivo alcanzado.")
            break

if __name__ == "__main__":
    algoritmo_genetico()
