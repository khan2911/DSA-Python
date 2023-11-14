class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def add(self,node:Node):
        if self.head is not None:
            node.next = self.head
            self.head.prev = node
        self.head = node

    def addInEnd(self,node:Node):
        if self.head is None:
            self.head  = node
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node

        
    def deleteInBegining(self):
        if self.head is None:
            return  
        node = self.head
        self.head = self.head.next
        del node

    def deleteInEnd(self):
        if self.head is None:
            return
        curr = self.head
        prev = None
        while curr.next is not None:
            prev = curr
            curr = curr.next
        if prev == None:
            self.head = None
        
        else:
            prev.next = None
        del curr

    def searchAndDelete(self,val):
        curr = self.head
        while curr != None:
            if curr.data == val:
               
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                del curr
                return
            curr = curr.next 



    def __repr__(self) -> str:
        curr = self.head
        returnString = ""
        while curr is not None:
            returnString = returnString+str(curr.data)+" <-> "
            curr = curr.next
        return returnString
        
# if __name__ == "__main__":
#     doublyLinkedList = DoublyLinkedList()
#     for i in range(10):
#         doublyLinkedList.insertionInBegining(Node(i))
#     print(doublyLinkedList) 

linkedList = DoublyLinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
linkedList.add(node1)
print(linkedList)
linkedList.add(node2)
print(linkedList)
linkedList.add(node3)
print(linkedList)
linkedList.add(node4)
print(linkedList)
linkedList.deleteInBegining()
print(linkedList)
linkedList.deleteInEnd()
print(linkedList)
linkedList.addInEnd(node5)
print(linkedList)
linkedList.searchAndDelete(2)
print(linkedList)
