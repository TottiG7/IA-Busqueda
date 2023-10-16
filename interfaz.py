# Importa las bibliotecas necesarias para la interfaz gráfica.
from tkinter import Frame
import tkinter as tk
from Nodo import Nodo, Puzzle
import time

# Define las posibles movimientos para cada casilla en función de la posición de la casilla vacía.
movimientos = [[[1, 3], [0, 2, 4], [1, 5]],
              [[0, 4, 6], [1, 3, 5, 7], [2, 4, 8]],
              [[3, 7], [4, 6, 8], [5, 7]]]

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('650x800')
        self.container = tk.Frame(self, bg='red')
        self.container.place(relx=0, rely=0, relheight=1, relwidth=1)
        fTab = Frame_Puzzle(self.container, self)
        fTab.tkraise()

# Inicializa una ficha en la interfaz gráfica con su posición y número.
class Ficha:
    contador = 0

    def __init__(self, r, c, n, frame):
        self.frame = frame
        self.r = r
        self.c = c
        self.n = n
        self.contador = Ficha.contador
        Ficha.contador += 1
        if n != 0:
            # Crea un botón para representar una ficha con el número.
            self.button = tk.Button(self.frame, text=str(self.n), font=("Impact", 100), command=lambda: self.move(self.contador))
        else:
            # Crea un botón en blanco para representar la casilla vacía.
            self.button = tk.Button(self.frame, text='', font=("Impact", 100), command=lambda: self.move(self.contador))
            # Coloca el botón en su posición en la interfaz gráfica.
        self.button.place(relx=1 / 26 + self.c * (4 / 13), rely=0.05 + self.r * (1 / 4), relheight=1 / 4, relwidth=4 / 13)

    # Maneja el movimiento de una ficha al hacer clic en ella.
    def move(self, icontador):
        if not self.frame.solving:
            er, ec = self.frame.aux_puzzle.empty()
            for ficha in self.frame.fichas:
                if ficha.contador == icontador:
                    fr, fc = ficha.r, ficha.c
                    break

            if icontador in movimientos[er][ec]:
                if er == fr:
                    if fc < ec:
                        auxm = 'l'
                    else:
                        auxm = 'r'
                else:
                    if fr < er:
                        auxm = 'u'
                    else:
                        auxm = 'd'

                # Realiza el movimiento en la matriz y actualiza la interfaz gráfica.
                self.frame.aux_puzzle.se_mueve(auxm)
                self.frame.actualizar(self.frame.aux_puzzle.nums)

class Frame_Puzzle(tk.Frame):
    def __init__(self, parent, root):
        self.root = root
        tk.Frame.__init__(self, parent, bg='black')
        self.place(relx=0, rely=0, relheight=1, relwidth=1)
        b_solve = tk.Button(self, text="Resolver", command=self.solve_puzzle, background='black', fg='white', padx=10)
        b_solve.place(relx=0.3, rely=0.85, relheight=0.1, relwidth=0.4)
        self.nums = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
        self.aux_puzzle = Puzzle(self.nums)
        self.fichas = []
        for ir, r in enumerate(self.nums):
            for ic, c in enumerate(r):
                aux = Ficha(ir, ic, c, self)
                self.fichas.append(aux)
        self.solving = False

    # Inicia la resolución del rompecabezas.
    def solve_puzzle(self):
        if not self.solving:
            self.solving = True
            nodo = Nodo(nums=self.aux_puzzle.nums)
            result = self.solve(nodo)
            self.animate_solution(result)

    # Realiza la búsqueda en amplitud para encontrar la solución.
    def solve(self, root):
        solucion = root.breadth_first()
        steps = []
        aux = solucion
        contador = 0
        while True:
            steps.insert(0, aux)
            aux = aux.padre
            if aux is None:
                break
            contador += 1
        print("*******Pasos para resolver el rompecabezas*******")
        print("-----------------------",contador,"-----------------------")
        return steps

    # Actualiza la interfaz gráfica con la configuración actual del rompecabezas.
    def actualizar(self, nums):
        aux = 0
        for ir, r in enumerate(nums):
            for ic, c in enumerate(r):
                if c != 0:
                    self.fichas[aux].button.config(text=str(c), background='black', fg='white', borderwidth=10, relief="flat")
                else:
                    self.fichas[aux].button.config(text='', background='white', borderwidth=10, relief="flat")
                aux += 1

    # Anima la solución del rompecabezas.
    def animate_solution(self, steps):
        for step in steps:
            if step.padre:
                self.aux_puzzle.nums = step.Puzzle.nums
                self.actualizar(self.aux_puzzle.nums)
                self.update()
                time.sleep(1)  # Pausa entre movimientos
        self.solving = False

if __name__ == '__main__':
    APP = App()
    APP.mainloop()
