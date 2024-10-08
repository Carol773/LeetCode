class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        if self.stack1:
            return self.stack1.pop(0)
        else:
            return -1
        

    def peek(self) -> int:
        if self.stack1:
            return self.stack1[0]
        else:
            return -1
        

    def empty(self) -> bool:
        if self.stack1:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()