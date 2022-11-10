n = 4
"""
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
"""
k = (2 * n) - 1
low = 0
high = k - 1
matrix = [[0 for i in range(k)] for j in range(k)]
"""
for i in range(n):
    for j in range(low, high + 1):
        matrix[i][j] = n
    for j in range(low + 1, high + 1):
        matrix[j][i] = n
    for j in range(low + 1, high + 1):
        matrix[high][j] = n
    for j in range(low + 1, high):
        matrix[j][high] = n
    low += 1
    high -= 1
    n -= 1
"""
while n != 0:
    for i in range(low, high + 1):
        for j in range(low, high + 1):
            if i == low or i == high or j == low or j == high:
                matrix[i][j] = n
    low += 1
    high -= 1
    n -= 1

for i in range(k):
    for j in range(k):
        print(matrix[i][j], end=" ")
    print()
