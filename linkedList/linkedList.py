class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return str(self.data) + " " + str(self.next)
    

class LinkedList:
    def __init__(self) -> None:
        self.head = None 

    def insertInBegining(self, node: Node):
        if self.head is None: #list is empty
            self.head = node
        else:
            node.next = self.head
            self.head =  node


    def insertInEnd(self, node: Node):
        newNode = node
        last = self.head
        newNode.next = None
        if self.head is None:
            self.head = newNode
            return 
        while last.next is not None:
            last = last.next
        
        last.next = newNode

    def insertInMiddle(self,node:Node,index):
        newNode = node
        if(self.head) == None:
            self.head = newNode
            return
        prev = None
        count = 0
        curr = self.head
        while curr and count < index  :
            prev = curr
            curr = curr.next
            count += 1 
        if not curr:
            print("Index out of Bound")
            prev.next = newNode
            return
        prev.next =  newNode
        newNode.next = curr            

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
    
    def deleteInMiddle(self,index):
        curr = self.head
        prev = None
        count = 0
        while curr and count < index:
            prev = curr
            curr = curr.next
            count += 1
        if curr:
            prev.next = curr.next
            del curr

    def deleteDuplicate(self):
        curr = self.head
        seen_value = set()
        prev = None
        while curr:
            if curr.data in  seen_value:
                prev.next = curr.next
                del curr
            else:
                seen_value.add(curr.data)
                print(seen_value)
                prev = curr
            curr = prev.next




    def search(self, val):
        curr = self.head
        while curr != None:
            if curr.data == val:
                return True
            
            curr = curr.next

        return False

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        self.head = prev

    def middleNode(self):
        curr = self.head
        length = 0
        while(curr):
            curr = curr.next
            length += 1
        middle = length // 2
        print(middle,length)
        curr = self.head
        i = 0
        while i < middle:
            curr = curr.next
            i +=1
        return curr.data
    
    def middleNode2(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr is not None and fast_ptr.next is not None :
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr
    
    def sorting(self):
        if self.head is None:
            return
        swapped = True
        while swapped :
            swapped = False
            curr = self.head
            while curr.next:
                if curr.data > curr.next.data:
                    curr.data , curr.next.data = curr.next.data , curr.data
                    swapped = True
                curr = curr.next
                



    def __repr__(self) -> str:
        node = self.head
        returnString = ""
        while node is not None:
            returnString = returnString + str(node.data) + " -> "
            node = node.next
        return returnString
    
    def __printRecursion(self,node:Node):  
        if node is None:
            return
        self.__printRecursion(node.next) 
        print(node.data,end = "->")

    def printRecursion(self):
        self.__printRecursion(self.head)

def merging(list1,list2):
    mergedList = LinkedList()
    node1 = list1.head
    node2 = list2.head
    count = 0
    while node1 is not None and node2 is not None:
        node = Node(0)
        if count % 2 == 0:
            node.data = node1.data
            node1 = node1.next
        else:
            node.data = node2.data
            node2 = node2.next
        mergedList.insertInEnd(node)
        count += 1
    
    if node1 is not None:
        while node1 is not None:
            node = Node(0)
            node.data = node1.data
            node1 = node1.next 
            mergedList.insertInEnd(node)

    if node2 is not None:
        while node2 is not None:
            node = Node(0)
            node.data = node2.data
            node2 = node2.next 
            mergedList.insertInEnd(node)

    return mergedList

if __name__ == "__main__":
    # linkedList = LinkedList()
    #  node1 = Node(4)
    #  node2 = Node(5)
    # node3 = Node(6)
    # node4 = Node(3)
    # node5 = Node(7)
    # node6 = Node(7)
    # node7 = Node(8)
    # linkedList.insertInEnd(node1)
    # print(linkedList)
    # linkedList.insertInBegining(node2)
    # print(linkedList)
    # linkedList.insertInBegining(node3)
    # print(linkedList)
    # linkedList.insertInEnd(node4)
    # print(linkedList)
    # linkedList.insertInMiddle(node5,7)
    # print(linkedList)
    # linkedList.insertInBegining(node7)
    # # linkedList.printRecursion()
    # # print(linkedList)
    # # linkedList.reverse()
    # # print(linkedList)
    # #print(linkedList.middleNode())
    # # print(linkedList)
    # # linkedList.deleteInMiddle(2)
    # # print(linkedList)
    # linkedList.insertInEnd(node6)
    # print(linkedList)
    # linkedList.sorting()
    # # linkedList.deleteDuplicate()
    # # print(linkedList)
    # mid = linkedList.middleNode2()
    # curr = linkedList.head
    # while curr.next is not None:
    #     curr = curr.next
    # curr.next = mid
    # # print(linkedList)
    # fast_ptr = linkedList.head
    # slow_ptr = linkedList.head
    # while fast_ptr is not None and fast_ptr.next is not None:
    #     fast_ptr = fast_ptr.next.next
    #     slow_ptr  = slow_ptr.next
    #     if slow_ptr == fast_ptr:
    #         print(True)
    #         break
    linkedList1 = LinkedList()
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node4 = Node(7)
    linkedList1.insertInBegining(node4)
    linkedList1.insertInBegining(node3)
    linkedList1.insertInBegining(node2)
    linkedList1.insertInBegining(node1)
    print(linkedList1)

    linkedList2 = LinkedList()
    node1 = Node(2)
    node2 = Node(4)
    node3 = Node(6)
    node4 = Node(8) 
    linkedList2.insertInBegining(node4)
    linkedList2.insertInBegining(node3)
    linkedList2.insertInBegining(node2)
    linkedList2.insertInBegining(node1)
    print(linkedList2)
    MergedList =  merging(linkedList1,linkedList2)
    print(MergedList)



    
    
 

    
    