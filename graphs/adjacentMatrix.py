numV = int(input())
v = [i for i in input().split()]
vertexMap = dict()
for i in range(len(v)):
     vertexMap[v[i]] = i

adjMatrix = [[0]*len(v) for i in range(len(v)) ]
    
numE = int(input())
for i in range(numE):
     u,v = [i for i in input().split()]
     adjMatrix[vertexMap[u]][vertexMap[v]] = 1
     adjMatrix[vertexMap[v]][vertexMap[u]] = 1

print(adjMatrix)


