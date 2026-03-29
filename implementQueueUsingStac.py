class MyQueue:
    def __init__(self):
        # stack1 is used for enqueue (push operations)
        self.stack1 = []
        # stack2 is used for dequeue (pop and peek operations)
        self.stack2 = []
        
    def push(self, x:int) -> None:
        self.stack1.append(x)
    
    def pop(self) -> int:
        # If stack2 is empty, move all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Pop the element from stack2 (which is the front of the queue)
        return self.stack2.pop()
           
    def peek(self) -> int:
        # If stack2 is empty, move all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Return the top of stack2 (the front of the queue)
        return self.stack2[-1]
    
    def empty(self) -> bool:
        return len(self.stack1)==0 and len(self.stack2)==0