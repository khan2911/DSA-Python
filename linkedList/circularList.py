class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None

class CircularList:
    def __init__(self) -> None:
        self.tail = None

    def insertInBegining(self,node:Node):
        
        if self.tail is None:
            self.tail = node
            node.next = node
        else:
            node.next = self.tail.next
            self.tail.next = node

    def insertInEnd(self,node:Node):
        if self.tail is None:
            self.tail = node
            node.next = node
        node.next = self.tail.next
        self.tail.next = node
        self.tail = node

    def deleteInBegining(self):
        if self.tail is None:
            return
        curr = self.tail
        curr.next = curr.next.next 
        del curr

    def deleteInEnd(self):
        if self.tail is None:
            return
        
        curr = self.tail.next
        prev = None
        while curr.next != self.tail.next:
            prev = curr
            curr = curr.next
        prev.next = self.tail.next
        self.tail = prev
        del curr

    # def searchAndDelete(self,val):

        

    def display(self):
        if self.tail is None:
            return
        curr = self.tail.next
        returnString =" "
        while curr != self.tail:
            returnString = returnString + str(curr.data) + " -> "
            curr = curr.next
        returnString = returnString + str(curr.data) + " -> "
        return returnString

    


link = CircularList()
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
node4 = Node(50)
link.insertInBegining(node1)
print(link.display())
link.insertInBegining(node2)
print(link.display())
link.insertInEnd(node3)
print(link.display())
link.insertInEnd(node4)
print(link.display())
link.deleteInBegining()
print(link.display())
link.deleteInEnd()
print(link.display())




        
