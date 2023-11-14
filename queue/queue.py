class Queue:
    def __init__(self):
        self.data = []
         

    def enqueue(self,data):
        self.data.append(data)

    def dequeue(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        return -1

queue = Queue()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.data)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.data)