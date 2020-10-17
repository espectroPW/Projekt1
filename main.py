import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

# wczytywanie pliku do zmiennej file1

dane = open('australian.txt').read()
dane = [item.split() for item in dane.split('\n')]
danepd = pd.DataFrame(data=dane)

typy = open('australian.txt').read()
typy = [item.split() for item in typy.split('\n')]
typypd = pd.DataFrame(data=typy)

print(np.matrix(dane))


# A[1] <- drugi wiersz
# A[1][2] <- 3 element w 2 wierszu
# A[Y][X]  <-

print("#############################")

wiersze = len(dane[:][:])

kolumny = len(dane[0][:])

print("Wiersze: {}. Kolumny: {}".format(wiersze, kolumny))

x = 0


def wyswietl(tablica, x, y):

    for x in range(0, wiersze):
        print(np.matrix(dane[0][x]))



jeden = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],# GIT
        [0,0,1,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0],# GIT
        [0,1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0],# GIT
        [1,0,1,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0],#       G
        [0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0],# Git
        [0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],#       G
        [0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0],# Git
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #       G
         ]



plt.imshow(jeden)
plt.colorbar()
plt.show(block=False)
plt.pause(1)
plt.close()

jeden[1][2] = 5

plt.imshow(jeden)
plt.colorbar()
plt.show(block=False)
plt.pause(1)
plt.close()


