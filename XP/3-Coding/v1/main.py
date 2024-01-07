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
        puzzle_solver = PuzzleSolver(puzzle)

        if puzzle_solver.resolver() is True:
            print('Una solución fue encontrada')
        else:
            print('No se encontró una solución')

main = Main()