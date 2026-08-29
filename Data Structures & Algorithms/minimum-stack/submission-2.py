class MinStack:
    #What do I know.
    #I know that there is going to be two stacks used.
        #One for stack.
        #The other for minStack.
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        #Here I know to keep track of the min in order to save time getting the answer.
        self.stack.append(val)
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]