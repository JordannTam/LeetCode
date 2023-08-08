class MinStack:

    def __init__(self):
        self.stack = []
        self.minLs = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minLs.append(val if not self.minLs == [] else min(self.minLs[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minLs.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minLs[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    s = MinStack()
    print(MinStack.isValid(s,"()[]{}"))
