from collections import deque

class Queue:
    def __init__(self,initialList= []):
        self.container = deque(initialList)
    def enqueue(self,value):
        self.container.appendleft(value)
        return str(value)
    def dequeue(self):
        if self.isEmpty():
            return "list is Empty"
        return self.container.pop()
    def front(self):
        if self.isEmpty():
            print(self.container)
            return "list is Empty"
        return self.container[-1]
    def size(self):
        return len(self.container)
    def isEmpty(self):
        return self.size() <= 0






    
