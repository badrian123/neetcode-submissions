class MinStack:
    #Need to build a stack and make sure all function run in o(1) time
    #I am just going to create a stack.
    #For the min part, I am just going to do work in advance that way, when the function is requested, the time is o(1)
    def __init__(self):
        self.stack = []
        #Keeping track of min value will result in o(1) time because the work is already done in advance
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #This is where the extra work needs to be done for min function
        minValue = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minValue)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
