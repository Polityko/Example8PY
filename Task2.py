# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

from random import randint
import statistics

size = 4
mat = [0] * size

for i in range(size):
    mat[i] = list(randint(1, 15) for a in range(size))

for i in mat:
    print(i)

sum_diagonal = 0

for i in range(size):
    for j in range(size):
        if i == j:
            print(mat[i][j], end= ' ')
            sum_diagonal += mat[i][j]
print(sum_diagonal)

sum_rows = []
for i in mat:
    sum_rows.append(sum(i))
print(sum_rows)

for i in range(len(sum_rows)):
    if sum_rows[i] > sum_diagonal:
        print(f'В {i+1} группе  сумма больше, чем сумма эл-ов диагонали')