class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(root):
    vals = []
    while root:
        vals.append(root.val)
        root = root.next
    return vals[int(len(vals)/2)] if len(vals)%2!=0 else vals[int((len(vals)/2)-1): int((len(vals)/2)+1)]

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(13)))))
print(middle_of_linked_list(head)) 