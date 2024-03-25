class MyQueue:

    def __init__(self):
        self.data = []
        self.pop_data = []
        
    def push(self, x: int) -> None:
        self.data.append(x)
    def pop(self) -> int:
        while self.data:
            self.pop_data.append(self.data.pop())
        temp = self.pop_data.pop()
        while self.pop_data:
            self.data.append(self.pop_data.pop())
        return temp
    def peek(self) -> int:
        while self.data:
            self.pop_data.append(self.data.pop())
        temp = self.pop_data[-1]
        while self.pop_data:
            self.data.append(self.pop_data.pop())
        return temp
    def empty(self) -> bool:
        if len(self.data) == 0:
            return True
        return False