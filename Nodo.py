# Importa la clase Puzzle y la función deepcopy para crear copias de objetos.
from Puzzle import Puzzle
from copy import deepcopy

# Crea una copia del rompecabezas desde el nodo padre y aplica un movimiento.
class Nodo:
    def __init__(self, padre=None, nums=[], dir_movimiento='l'):
        self.padre = padre
        if self.padre is None:
            self.Puzzle = Puzzle(nums)
        else:
            self.Puzzle = deepcopy(self.padre.Puzzle)
            self.Puzzle.se_mueve(dir=dir_movimiento)
        self.g = 0  # Costo hasta el momento
        self.h = self.calcular_heuristica()
        self.f = self.g + self.h  # Función f = g + h

    # Calcula una heurística para estimar el costo restante hasta la solución y poder optimizar las iteraciones.
    def calcular_heuristica(self):
        total_distancia = 0
        for r in range(3):
            for c in range(3):
                numero_actual = self.Puzzle.nums[r][c]
                if numero_actual != 0:
                    r_objetivo, c_objetivo = divmod(numero_actual, 3)
                    distancia = abs(r - r_objetivo) + abs(c - c_objetivo)
                    total_distancia += distancia
        return total_distancia

    # Genera nodos hijos a partir de los movimientos posibles.
    def set_hijos(self):
        self.hijos = []
        for _dir in self.Puzzle.movimientos():
            auxN = Nodo(padre=self, dir_movimiento=_dir)
            auxN.g = self.g + 1
            self.hijos.append(auxN)

    # Realiza la búsqueda en amplitud para encontrar la solución.
    def breadth_first(self):
        agenda = [self]
        historial = set()

        it = 0
        while True:
            it += 1
            agenda.sort(key=lambda nodo: nodo.f)
            nodo_actual = agenda.pop(0)

            if nodo_actual.Puzzle.isSolution():
                break
            else:
                nodo_actual.set_hijos()
                aux_hijos = nodo_actual.hijos

                for hijo in aux_hijos:
                    if tuple(map(tuple, hijo.Puzzle.nums)) not in historial:
                        historial.add(tuple(map(tuple, hijo.Puzzle.nums)))
                        agenda.append(hijo)

            print('iteraciones:', it, 'len agenda:', len(agenda), 'len historial:', len(historial))

        print('______SOLUCION ENCONTRADA (', it, ' iteraciones)______')
        return nodo_actual
