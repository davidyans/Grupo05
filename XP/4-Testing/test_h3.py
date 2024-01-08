import unittest
from unittest.mock import patch
import io
from main import Main

class TestMain(unittest.TestCase):
    def test_mostrar_movimientos_del_hueco(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            Main()

        # Capturamos la salida y eliminamos la primera línea que contiene 'Solución encontrada:'
        output = mock_stdout.getvalue().strip().split('\n', 1)[-1]

        # Verificamos que haya al menos un movimiento
        self.assertTrue(len(output) > 0)

        # Verificamos que cada movimiento sea válido
        movimientos = output.split('\n')
        for movimiento in movimientos:
            self.assertIn(movimiento, ['arriba', 'abajo', 'izquierda', 'derecha'])

if __name__ == '__main__':
    unittest.main()
