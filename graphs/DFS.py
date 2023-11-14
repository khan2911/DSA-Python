adjacencyMatrix1 = [
    [0,1,0,0,1],
    [0,1,0,1,0],
    [1,0,1,0,0],
    [1,0,0,0,1],
    [0,0,1,1,0]]



def DFS(adjacencyMatrix):
    visited = set()
    for i in range(len(adjacencyMatrix)):
        if i not in visited:
            dfs(i,adjacencyMatrix,visited)

def dfs(v,adjacencyMatrix,visited):
    print(v)
    visited.add(v)
    for i in range(len(adjacencyMatrix[v])):
        if adjacencyMatrix[v][i] == 1 and i not in visited:
            dfs(i,adjacencyMatrix,visited)

DFS(adjacencyMatrix1)

 