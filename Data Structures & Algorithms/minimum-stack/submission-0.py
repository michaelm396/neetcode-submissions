class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        return self.stack.insert(0,val)
    #pushes an element into the stack
        

    def pop(self) -> None:
        del self.stack[0]
    # deletes the top element of the stack

    def top(self) -> int:
        return self.stack[0]
    #returns the top element of stack

    def getMin(self) -> int:
        return min(self.stack)
    #returns minimum element in stack
