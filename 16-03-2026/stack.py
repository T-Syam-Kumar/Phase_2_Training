"""stack = []
top = -1
while True:
    def push(item,top = top):
        if top == -1:
            top = len(stack)
            stack.append(item)
        else:
            stack[top] = item
    def pop (top = top):
        if len(stack)>0:
            top = stack.pop()
            return top
        else:
            return -1
    def peek():
        if len(stack) > 0:
            return stack[-1]
        else:
            return -1
    def check():
        if len(stack)>0:
            return stack[-1]
        else:
            return -1
    def clear():
        stack.clear()
    def reverse():
        stack.reverse()
    """

###################################### Stack using Class ######################################################
class Stack:

    def __init__(self,size,name):
        self.size = size
        self.stack = [0]*size
        self.top = -1
        self.name = name
        print(f'Assigned Successfully to {self.name}')

    def push(self,item):
        if self.top+1 == self.size:
            print(f'({self.name}) - Stack is Overflow !!')
            return
        else:
            self.top += 1
            self.stack[self.top] = item
            print(f'({self.name}) - Success.. added {self.stack[self.top]}')

    def pop(self):
        if self.top == -1:
            print(f'({self.name}) - Stack is underflow !!')
            return
        else:
            print(f'({self.name}) - Success.. removed {self.stack[self.top]}')
            self.top -= 1

    def peek(self):
        if self.top == -1:
            print(f'({self.name}) -  Stack is underflow !!')
            return
        else:
            print(f'({self.name}) - Peek value is {self.stack[self.top]}')

    def isEmpty(self):
        if self.top == -1:
            print(f'({self.name}) - Stack is Empty !!')
        else:
            print(f'({self.name}) - Stack is not empty ')

    def isFull(self):
        if self.top+1 == self.size:
            print(f'({self.name}) - Stack is Full !!')
        else:
            print(f'({self.name}) - Stack is not Full !!')

    def clear(self):
        self.stack.clear()

    def reverse(self):
        return self.stack.reverse()

    def display(self):
        if not self.top == -1:
            print(f'({self.name}) - Stack contains : ', end=' ')
            for i in range(self.top,-1,-1):
                print(self.stack[i],end=' ')
        print()

syam = Stack(5,"Syam")
syam.push(1)
syam.push(2)
syam.push(3)
syam.push(4)
syam.push(5)
syam.display()
syam.pop()
syam.display()
syam.peek()
syam.isEmpty()
syam.push(5)
syam.isFull()


# Stack is a linear data structure
# follows LIFO rule
# operations - push, pop, peek