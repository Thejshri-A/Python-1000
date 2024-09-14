class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

def remove_nth_node_from_end(head, n):
    dummy=ListNode(0)
    dummy.next=head
    first = second = dummy
    
    for _ in range(n+1):
        first = first.next
        
    while first:
        first = first.next
        second = second.next
        
    second.next = second.next.next
    return dummy.next

def print_linkedlist(node):
    while node:
        print(node.val, end = "=>")
        node=node.next
    print("None")
    

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n=2
next_node = remove_nth_node_from_end(head, n)
print_linkedlist(next_node)
    