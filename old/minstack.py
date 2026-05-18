class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None: 
        min=self.getMin()
        if val<min:
            min=val
        self.st.append([val,min])

    def pop(self) -> None:
        return self.st.pop()[0]

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.push(4)
obj.push(5)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()