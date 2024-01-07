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

**1. Identación:**

- Utilizar espacios, no tabulaciones.
- Usar 4 espacios para la sangría en cada nivel.

  Ejemplo:

  ```
  class Puzzle:
      def __init__(self, inicio, objetivo):
  ```

---
**2. Espacios en blanco:**

- Agregar un espacio después de las comas en listas y tuplas
- Agregar espacios alrededor de los operadores binarios.

  Ejemplo:

  ```
  self.direcciones = ['arriba', 'abajo', 'izquierda', 'derecha']
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

- Agrupar métodos relacionados y mantener una estructura lógica en la clase.

  Ejemplo
  ```
  class Puzzle:
    def __init__(self, inicio, objetivo):
        # ...

    def mover(self, estado, direccion):
        # ...

    def dibujar(self, estado):
        # ...

    def resolver(self):
        # ...
  ```

---