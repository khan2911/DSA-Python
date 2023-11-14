"""
5 - Number of Vertex
a b c d e - vertices
12 - number of edges
a b
a d 
a e
b a
b c
c b
c d
d a
d c
d e
e a
e c
 
"""
numV = int(input())
V = [i for i in input().split()] 
adjacencyList = dict()
for i in range(len(V)):
    adjacencyList[V[i]] = []

adj = dict()
numE = int(input())
for i in range(numE):
    u,v =[i for i in input().split()]
    adjacencyList[u].append(v)
    adjacencyList[v].append(u)
print(adjacencyList)

    

