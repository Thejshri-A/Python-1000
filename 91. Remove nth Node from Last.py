class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def remove_nth_node_from_last(head, n):
    dummy=ListNode(0)
    dummy.next = head
    first = second = dummy
    for _ in range(n+1):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head= head.next
    print(result)
    
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
result = remove_nth_node_from_last(head, n)
print_list(result)  # Output: [1, 2, 3, 5]