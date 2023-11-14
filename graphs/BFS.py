def BFS(adjacencyMatrix):
    visited = set()
    queue = []
    for i in range(len(adjacencyMatrix)):
        if i not in visited:
           bfs(i,adjacencyMatrix,visited)

def bfs(v,adjacencyMatrix,visited):
    queue = []
    queue.append(v)
    visited.add(v)
    print(v)
    while len(queue) != 0:
        i = queue.pop(0)
        for j in range(len(adjacencyMatrix[i])):
                if adjacencyMatrix[i][j] == 1:
                    if j not  in visited:
                        queue.append(j)
                        visited.add(j)
                        print(j)

adjacencyMatrix1 = [
    [0,1,0,0,1],
    [0,1,0,1,0],
    [1,0,1,0,0],
    [1,0,0,0,1],
    [0,0,1,1,0]]
BFS(adjacencyMatrix1)



                

           