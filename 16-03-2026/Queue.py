class Queue:
    def __init__(self,size,name):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = [0]*size
        self.name = name
        print(f'Successfully initialized to - {self.name}')

    def enqueue(self,item):
        if self.front > self.rear or self.rear == len(self.queue)-1:
            print(f'({self.name}) - Queue is Full')
            return
        if self.front == -1:
            self.front += 1
        self.rear += 1
        self.queue[self.rear] = item
        print(f'({self.name}) - {self.queue[self.rear]} Successfully added to queue')

    def dequeue(self):
        if self.rear == self.front == -1:
            print(f'({self.name}) - Queue is Empty')
            return
        print(f'({self.name}) - {self.queue[self.front]} Successfully removed from queue')
        self.front += 1

    def display(self):
        if self.rear == self.front == -1:
            print(f'({self.name}) - Queue is Empty')
            return
        print(f'({self.name})- Values in queue are : ', end=' ')
        for i in range(self.front, self.rear+1 ):
            print(self.queue[i],end=' ')
        print()

    def top(self):
        if self.rear == self.front == -1:
            print(f'({self.name}) - Queue is Empty')
            return
        print(f'({self.name})- top value from queue is : {self.queue[self.front]}')

    def last(self):
        if self.rear == self.front == -1:
            print(f'({self.name}) - Queue is Empty')
            return
        print(f'({self.name})- top value from queue is : {self.queue[self.rear]}')
syam = Queue(5,'Syam')
syam.enqueue(1)
syam.enqueue(2)
syam.display()
syam.dequeue()
syam.top()
syam.last()


# queue is a linear data structure
# follows FIFO rule
# operations - enqueue, dequeue
# deque - double ended queue
# circular queue
