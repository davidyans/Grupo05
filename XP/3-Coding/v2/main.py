import numpy as np
from puzzle import Puzzle
from puzzle_solver import PuzzleSolver

class Main:
     def __init__(self):
        inicio = np.array([[2, 8, 3],
                           [1, 6, 4],
                           [7, 0, 5]])
        objetivo = np.array([[1, 2, 3],
                             [8, 0, 4],
                             [7, 6, 5]])
        puzzle = Puzzle(inicio, objetivo)
        solucion = PuzzleSolver(puzzle).resolver()

        if solucion is not None:
            print('Solución encontrada:')
            for paso in solucion:
                print(paso)
        else:
            print('No se encontró una solución')

main = Main()