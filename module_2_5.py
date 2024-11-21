import random

def get_matrix(n, m, value):
    matrix = [value] * n
    for i in range(n):
        matrix[i] = [value] * m
    return matrix

n = random.randrange(1, 10)
m = random.randrange(1, 10)
value = random.randrange(1, 1000)
result = get_matrix(n, m, value)
print('Матрица из', n , 'строк и', m, 'столбцов, которые заполнены числом', value)
print(result)
