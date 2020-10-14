import pandas as pd
import numpy as np

# wczytywanie pliku do zmiennej file1

dane = open('australian.txt').read()
dane = [item.split() for item in dane.split('\n')]
danepd = pd.DataFrame(data=dane)

typy = open('australian.txt').read()
typy = [item.split() for item in typy.split('\n')]
typypd = pd.DataFrame(data=typy)



print(np.matrix(dane))

print("#############################")

x = 0

while True:
    print(np.matrix(dane[x][0]))
    x = x+1






