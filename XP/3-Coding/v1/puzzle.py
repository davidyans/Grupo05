import numpy as np

class Puzzle:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.objetivo = objetivo
        self.direcciones = ['arriba', 'abajo', 'izquierda', 'derecha']

    def mover(self, estado, direccion):
        estado = estado.copy()
        i, j = np.where(estado == 0)
        if direccion == 'arriba' and i > 0:
            estado[i, j], estado[i - 1, j] = estado[i - 1, j], estado[i, j]
        elif direccion == 'abajo' and i < 2:
            estado[i, j], estado[i + 1, j] = estado[i + 1, j], estado[i, j]
        elif direccion == 'izquierda' and j > 0:
            estado[i, j], estado[i, j - 1] = estado[i, j - 1], estado[i, j]
        elif direccion == 'derecha' and j < 2:
            estado[i, j], estado[i, j + 1] = estado[i, j + 1], estado[i, j]
        else:
            return None
        return estado
