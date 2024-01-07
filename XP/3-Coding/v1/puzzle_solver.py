import numpy as np
import time
from collections import deque
from dibujante import Dibujante
from puzzle import Puzzle

class PuzzleSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.dibujante = Dibujante()

    def resolver(self):
        cola = deque([self.puzzle.inicio])
        visitados = set([self.puzzle.inicio.tobytes()])

        while cola:
            estado = cola.popleft()
            self.dibujante.dibujar_estado(estado)
            time.sleep(0.7)
            if np.array_equal(estado, self.puzzle.objetivo):
                return True
            for direccion in self.puzzle.direcciones:
                nuevo_estado = self.puzzle.mover(estado, direccion)
                if nuevo_estado is not None and nuevo_estado.tobytes() not in visitados:
                    cola.append(nuevo_estado)
                    visitados.add(nuevo_estado.tobytes())
        return False