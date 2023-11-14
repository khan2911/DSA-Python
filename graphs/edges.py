def print_edges(matrix, vertex):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                print(vertex[i],vertex[j])


matrix1 = [
    [0, 1, 1, 0],  
    [1, 0, 0, 1],  
    [1, 0, 0, 1],  
    [0, 1, 1, 0]   
]

vertex = ['a', 'b', 'c', 'd']

print_edges(matrix1, vertex)
