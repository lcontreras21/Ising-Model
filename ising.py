# Luis Contreras-Orendain
# Ising Imeplementation for PHYS 303: Statistical Mechancis
import time
import random
import matplotlib.pyplot as plt
from math import exp

class Ising_Model:
    def __init__(self, size, T):
        self.size = size - 1
        self.T = T
        self.i_table = self.initialize(size)
        self.fig = plt.figure()
        self.plot = self.fig.add_subplot(111).imshow(self.i_table, cmap='gray')

    def iteration(self):
        amount = 10 * (self.size + 1)**2
        for t in range(amount): # visits each node 100 times
            if t % 100 == 0:
                print("ON", t, "of", amount,  flush=True)
            i = int(random.random() * self.size)
            j = int(random.random() * self.size)
            Ediff = self.deltaU(i, j)
            print(self.i_table[0][0])
            if Ediff <= 0:
                self.i_table[i][j] = -1 * self.i_table[i][j]
                self.plot.set_data(self.i_table)
                self.fig.canvas.draw()
            else:
                if random.random() < exp(-1 * Ediff / self.T):
                    self.i_table[i][j] = -1 * self.i_table[i][j]
                    self.plot.set_data(self.i_table)
                    self.fig.canvas.draw()
        

    def initialize(self, size):
        i_table = [[0]*size for i in range(size)]
        for i in range(size):
            for j in range(size):
                x = random.random()
                if x > 0.5:
                    i_table[i][j] = -1
                else:
                    i_table[i][j] = 1
        return i_table

    def deltaU(self, i, j,):
        if i == 0:
            top = self.i_table[self.size][j]
        else:
            top = self.i_table[i-1][j]

        if i == self.size:
            bottom = self.i_table[0][j]
        else:
            bottom = self.i_table[i+1][j]

        if j == 0:
            left = self.i_table[i][self.size]
        else:
            left = self.i_table[i][j-1]

        if j == self.size:
            right = self.i_table[i][0]
        else:
            right = self.i_table[i][j+1]

        Ediff = 2 * self.i_table[i][j] * (top + bottom + left + right)
        return Ediff

    # def colorsquare(i, j, ij_value):
        

def main():
    plt.ion()
    print("Starting Ising Model", flush=True)
    T = 1
    size = 10
    # make T and size command line arguments

    i_table = Ising_Model(size, T) 
    i_table.iteration()
   
    print("Finished Ising Model", flush=True)
if __name__ == "__main__":
    main()
    time.sleep(60)
