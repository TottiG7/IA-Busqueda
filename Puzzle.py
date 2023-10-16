solucion = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
lista_de_movimientos = [[['r', 'd'], ['l', 'r', 'd'], ['l', 'd']],
                        [['r', 'u', 'd'], ['l', 'r', 'u', 'd'], ['l', 'u', 'd']],
                        [['r', 'u'], ['l', 'r', 'u'], ['l', 'u']]]
# Inicializa un rompecabezas con el tablero solucion.
class Puzzle:
    def __init__(self, nums=[[1, 2, 3], [4, 5, 6], [7, 8, 0]]):
        self.nums = nums

    # Comprueba si la matriz actual coincide con la solución (todos los números están en su lugar).
    def isSolution(self):
        return self.nums == solucion
    
    # Encuentra la posición de la casilla vacía (0) en la matriz.
    def empty(self):
        for ir, r in enumerate(self.nums):
            for ic, c in enumerate(r):
                if c == 0:
                    return ir, ic

    # Devuelve los movimientos posibles para la casilla vacía en función de su posición.
    def movimientos(self):
        r, c = self.empty()
        return lista_de_movimientos[r][c]

    # Realiza un movimiento en la dirección especificada (izquierda, derecha, arriba o abajo).
    def se_mueve(self, dir):
        r, c = self.empty()

        if dir == 'l':
            aux = self.nums[r][c]
            self.nums[r][c] = self.nums[r][c - 1]
            self.nums[r][c - 1] = aux
        elif dir == 'r':
            aux = self.nums[r][c]
            self.nums[r][c] = self.nums[r][c + 1]
            self.nums[r][c + 1] = aux
        elif dir == 'u':
            aux = self.nums[r][c]
            self.nums[r][c] = self.nums[r - 1][c]
            self.nums[r - 1][c] = aux
        elif dir == 'd':
            aux = self.nums[r][c]
            self.nums[r][c] = self.nums[r + 1][c]
            self.nums[r + 1][c] = aux
