import sys
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

    @patch('sys.stdout.write')
    @patch.object(Dibujante, 'dibujar_estado', wraps=Dibujante.dibujar_estado)
    def test_coordenadas_desplazamiento(self, mock_dibujar_estado, mock_stdout_write):
        puzzle_solver = PuzzleSolver(self.puzzle)
        with patch.object(Dibujante, 'dibujar_estado') as patched_dibujar_estado:
            result = puzzle_solver.resolver()

        # Verifica que dibujar_estado fue llamado al menos una vez
        self.assertGreaterEqual(patched_dibujar_estado.call_count, 1)

        # Verifica que las coordenadas x y y fueron escritas en la salida estándar
        for call_args in mock_stdout_write.call_args_list:
            call_args = call_args[0] if sys.version_info.major == 2 else call_args.args
            x, y = call_args[0].strip('()').split(', ')
            self.assertTrue(x.isdigit() and y.isdigit())

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
