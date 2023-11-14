class Node:
    def __init__(self,data) :
        self.left = None
        self.right = None
        self.data = data

    def insertLeft(self,node):
        if self.left is None:
            self.left = node
        else:
            raise AttributeError("Left Child Already exist")
        
    def insertRight(self,node):
        if self.right is None:
            self.right = node
        else:
            raise AttributeError("Rigth Child Already Exist")
    
def inOrder(node):
    if node is not None:
        inOrder(node.left)
        print(node.data)
        inOrder(node.right)

def postOrder(node):
    if node is not None:
        postOrder(node.left)
        postOrder(node.right)
        print(node.data)

def preOrder(node):
    if node is not None:
        print(node.data)
        preOrder(node.left)
        preOrder(node.right)

def build(pre, ino ):
    
    
    if len(pre) == 0:
        return
    if len(pre) == 1:
        return Node(pre[0])
    root = Node(pre[0])
    in_index = ino.index(pre[0])
    root.left = build( pre[1:in_index +1], ino[:in_index])
    root.right = build(pre[in_index+1:], ino[in_index+1:])
    return root

def buildTree(ino,poso):

    if len(poso) == 0:
        return
    if len(poso) == 1:
        return Node(poso[0])
    root = Node(poso[-1])
    root_index = ino.index(poso[-1])

    root.left = buildTree(ino[:root_index],poso[:root_index])
    root.right = buildTree(ino[root_index+1:],poso[root_index:-1])
    return root


# pre = [1,2,4,5,3]
ino = [4,2,5,1,3]
# tree = build(pre,ino)
# inOrder(tree)
# preOrder(tree)
poso =[4,5,2,3,1]
tree = buildTree(ino,poso)
inOrder(tree)
postOrder(tree)




         

node1 = Node(5)
node2 = Node(6)
node3 = Node(7)
node4 = Node(8)
node5 = Node(9)
node6 = Node(10)
node7 = Node(11)

node1.insertLeft(node2)
node1.insertRight(node3)
node2.insertLeft(node4)
node2.insertRight(node5)
node3.insertLeft(node6)
node3.insertRight(node7)

# inOrder(node1)
# # postOrder(node1)
# preOrder(node1)
        
    
           
        

