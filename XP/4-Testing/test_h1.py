import unittest
import numpy as np
from unittest.mock import patch
from puzzle import Puzzle
from puzzle_solver import PuzzleSolver
from dibujante import Dibujante

class TestPuzzle(unittest.TestCase):
    def setUp(self):
        inicio = np.array([[2, 8, 3],
                           [1, 6, 4],
                           [7, 0, 5]])
        objetivo = np.array([[1, 2, 3],
                             [8, 0, 4],
                             [7, 6, 5]])
        self.puzzle = Puzzle(inicio, objetivo)

    @patch('builtins.print')
    @patch.object(Dibujante, 'dibujar_estado', wraps=Dibujante.dibujar_estado)
    def test_mostrar_opciones_de_movimiento(self, mock_dibujar_estado, mock_print):
        puzzle_solver = PuzzleSolver(self.puzzle)
        result = puzzle_solver.resolver()
        
        # Verifica que dibujar_estado fue llamado al menos una vez
        self.assertGreaterEqual(mock_dibujar_estado.call_count, 1)

        # Muestra todos los bloques que fueron dibujados durante la resolución
        print("Bloques mostrados durante la resolución:")
        for call_args in mock_dibujar_estado.call_args_list:
            print(call_args.args[0])  # Imprime el bloque (estado) dibujado

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
