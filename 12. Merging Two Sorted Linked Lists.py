class LinkedList:
    def __init__(self, val =0 , next=None):
        self.val = val
        self.next = next
        
def merge_two_lists(l1, l2):
    if not l1: return l2
    if not l2: return l1
    
    if(l1.val < l2.val):
        l1.next = merge_two_lists(l1.next, l2)
        return l1
        
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2
    
def print_list(node):
    while node:
        print(node.val, end="=>" if node.next else "\n")
        node=node.next
        
l1= LinkedList(1)
l1.next= LinkedList(2)
l1.next.next = LinkedList(4)

l2= LinkedList(1)
l2.next=LinkedList(3)
l2.next.next = LinkedList(5)
    
merge_list = merge_two_lists(l1, l2)

print(print_list(merge_list))