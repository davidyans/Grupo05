import matplotlib.pyplot as plt
import numpy as np

class Dibujante:
    @staticmethod
    def dibujar_estado(estado):
        plt.imshow(estado, cmap='gray_r')
        plt.xticks([])
        plt.yticks([])
        for (j, i), label in np.ndenumerate(estado):
            if label > 0:
                plt.text(i, j, int(label), ha='center', va='center', color='black')
        plt.show(block=False)
        plt.pause(0.1)
        plt.clf()