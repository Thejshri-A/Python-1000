class NestedListIterator:
    def __init__(self, nestedlist):
        self.stack = []
        self.flatten(nestedlist)
        
    def flatten(self, nestedlist):
        for elem in reversed(nestedlist):
            if isinstance(elem, list):
                self.flatten(elem)
            else:
                self.stack.append(elem)
    
    def next(self):
        return self.stack.pop()
    
    def hasNext(self):
        return len(self.stack)>0

# Example Usage
nestedlist = [[1, 1], 2, [1, 1]]
iterator = NestedListIterator(nestedlist)
result = []
while iterator.hasNext():
    result.append(iterator.next())
print(result)  # Output: [1, 1, 2, 1, 1]