class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next= next
def reverselist(head):
    prev=None
    current= head
    
    while current:
        next_node = current.next
        current.next= prev
        prev = current
        current = next_node
    return prev

head= ListNode(1, ListNode(2, ListNode(3)))
reverse_list = reverselist(head)

while reverse_list:
    print(reverse_list.val, end="->")
    reverse_list = reverse_list.next