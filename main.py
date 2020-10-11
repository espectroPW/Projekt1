import pandas as pd
# wczytywanie pliku do zmiennej file1

matrix = open('australian.txt').read()
matrix = [item.split() for item in matrix.split('\n')]


xx = len(matrix[1])
print("X:{}".format(xx))
yy = 0

df = pd.DataFrame(data=d)

xy = 0


while True:

    if matrix[xy][0] == 0 or matrix[xy][0] == 1:
        yy = yy + 1
        xy = xy + 1








