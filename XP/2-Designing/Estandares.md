# ESCUELA POLITÉCNICA NACIONAL

---

**Integrantes:**

- Simbaña Ivan
- Suntasig Ariel
- Terán José
- Torres Jeremy
- Verdezoto José
- Yanez David

---

# Estándares de codificación Puzzle

**1. Convenciones de nomenclatura:**

- Usar nombres descriptivos para variables y métodos.
- Utilizar convenciones de nombres como snake_case para variables y lower_case para funciones/métodos en Python.

  Ejemplo:

  ```
  class PuzzleSolver:
    def __init__(self, puzzle_instance):
        self.puzzle_instance = puzzle_instance
        self.drawer = Dibujante()
    
    def solve_puzzle(self):
        states_queue = deque([self.puzzle_instance.start])
        visited_states = set([self.puzzle_instance.start.tobytes()])
        paths = {self.puzzle_instance.start.tobytes(): []}
  ```

---
**2. Espacios en blanco y formato:**

- Mantener una consistencia en el uso de espacios en blanco y formato en el código.
- Evitar líneas largas y dividirlas para mejorar la legibilidad.

  Ejemplo:

  ```
  class Dibujante:
    @staticmethod
    def draw_state(state):
        plt.imshow(state, cmap='Blues')
        plt.title("Puzzle")
  ```

---
**3. Nombres de variables y funciones:**

- Utilizar nombres descriptivos.
- Usar snake_case para nombres de funciones y variables.

  Ejemplo

  ```
  def dibujar(self, estado):
      plt.imshow(estado, cmap='gray_r')
  ```

---

**4. Imports:**

- Agrupar los imports al principio del archivo.
- Importar solo lo necesario desde los módulos.
  
  Ejemplo
  ```
  import numpy as np
  import matplotlib.pyplot as plt
  from collections import deque
  ```
---
**5. Organización del código**

- Dividir lógicamente el código en secciones y clases para una mejor organización.
- Ordenar las importaciones y mantener una estructura jerárquica para facilitar la comprensión.

  Ejemplo
  ```
  class Main:
    def __init__(self):
        # ...
  
  class Puzzle:
    def __init__(self, start, goal):
        # ...

    def move(self, state, direction):
        # ...
  
  class Dibujante:
    @staticmethod
    def draw_state(state):
        # ...
  
  class PuzzleSolver:
    def __init__(self, puzzle_instance):
        # ...

    def solve_puzzle(self):
        # ...
  ```

---