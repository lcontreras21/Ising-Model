# Luis Contreras-Orendain
# Ising Imeplementation for PHYS 303: Statistical Mechancis
import time
import random
import matplotlib.pyplot as plt
from math import exp
from collections import Counter
from operator import itemgetter

class Ising_Model:
    def __init__(self, size, T, j=1, h=0):
        self.size = size - 1
        self.T = T
        self.h = h
        self.j = j
        self.i_table = self.initialize(size)
        self.fig = plt.figure()
        self.i_table_plot = self.fig.add_subplot(211).imshow(self.i_table, cmap='gray')
        self.M_plot = self.fig.add_subplot(212)

    def iteration(self):

        # Calculate total energy then add Ediff to it after each iteratation
        U = self.totalU()
        print("Initial U", U, flush=True, end=" ")

        totalM = []
        amount = 1 * (self.size + 1)**2

        for t in range(amount): # visits each node 100 times
            #if t % 100 == 0:
                #print("ON", t, "of", amount,  flush=True)
            i = int(random.random() * self.size)
            j = int(random.random() * self.size)
            Ediff = self.deltaU(i, j)
            if Ediff <= 0:
                self.i_table[i][j] = -1 * self.i_table[i][j]
                self.i_table_plot.set_data(self.i_table)
                self.fig.canvas.draw()
                U += Ediff
            else:
                if random.random() < exp(-1 * (Ediff / self.T)):
                    self.i_table[i][j] = -1 * self.i_table[i][j]
                    self.i_table_plot.set_data(self.i_table)
                    self.fig.canvas.draw()
                    U += Ediff
            runMTotal = sum([sum(self.i_table[i]) for i in range(self.size)])
            totalM.append(runMTotal)


        print("Final U", U, flush=True)
        print("Average Magnetization:", sum(totalM)/len(totalM), flush=True)
        Mcounts = dict(Counter(totalM))
        print("Most Likely Magnetization:", max(Mcounts.items(), key=itemgetter(1))[0], flush=True)
        self.M_plot.bar(list(Mcounts.keys()), Mcounts.values())
        self.fig.canvas.draw()
        
        return (U/amount, max(Mcounts.items(), key=itemgetter(1))[0])




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

        neighbors = top + bottom + left + right
        '''
        Efinal = (self.j * self.i_table[i][j] * neighbors) - (self.h * neighbors)
        Einitial = (-1 * self.j * self.i_table[i][j] * neighbors) - (self.h * neighbors)
        Ediff = Efinal - Einitial   
        '''
        Ediff = (2 * self.j * self.i_table[i][j] * neighbors)
        return Ediff

    def totalU(self):
        U = 0
        for i in range(self.size):
            neighbor = 0
            for j in range(self.size):
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

                neighbor += top + bottom + left + right
            U += neighbor
        return U

def main():
    plt.ion()
    print("Starting Ising Model", flush=True)
    size = 5
    h = 0
    j = -1
    # make T and size command line arguments

    avgUList = []
    mostLikelyMList = []
    TList = []
    '''
    for i in range(2, 0, -1):
        T = 4 - i*0.5
        i_table = Ising_Model(size, T, j, h)
        avgU, mostLikelyM = i_table.iteration()
        TList.append(T)
        avgUList.append(avgU)
        mostLikelyMList.append(avgU)
    '''
    #plt.ioff()
    dataFig = plt.figure()
    print(TList, avgUList, mostLikelyMList)
    dataFig.add_subplot(111).[random.random() for i in range(10)], [random.random() for i in range(10)])
    #dataFig.add_subplot(111).scatter(TList, avgUList)
    #dataFig.add_subplot(212).scatter(TList, mostLikelyMList)
    dataFig.canvas.draw()
    time.sleep(30)
   
    print("Finished Ising Model", flush=True)
if __name__ == "__main__":
    main()
    time.sleep(30)

