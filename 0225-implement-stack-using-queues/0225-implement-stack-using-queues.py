class MyStack:

    def __init__(self):
        self.queue_1=[]
        self.queue_2=[]
        

    def push(self, x: int) -> None:
        self.queue_1.append(x)
        

    def pop(self) -> int:
        if self.queue_1:
            return self.queue_1.pop()
        else:
            return '[]'
        

    def top(self) -> int:
        if self.queue_1:
            return self.queue_1[-1]
        

    def empty(self) -> bool:
        if self.queue_1:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()