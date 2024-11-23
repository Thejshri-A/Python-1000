class ListNode:
    def __init__(self, val =0 , next=None):
        self.val = val
        self.next = next

def palindrome_linked_List(head):
    vals = []
    while head:
        vals.append(head.val)
        head= head.next
        
    return vals == vals[::-1]

# Example usage:
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(palindrome_linked_List(head))  # Output: True