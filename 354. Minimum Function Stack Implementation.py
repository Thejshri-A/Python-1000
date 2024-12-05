class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, x):
        self.stack.append(x)
        self.min_stack.append(x if not self.min_stack else min(x, self.min_stack[-1]))
    
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self):
        return self.stack[-1]
    
    def get_min(self):
        return self.min_stack[-1]
    
minStack = MinStack()
minStack.push(3)
minStack.push(5)
print(minStack.get_min())