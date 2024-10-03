class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def isCycle(head):
    slow , fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False


# Example usage:
head = ListNode(3)
second = ListNode(2)
third = ListNode(0)
fourth = ListNode(-4)
head.next = second
second.next = third
third.next = fourth
fourth.next = second  # Creates a cycle

print(isCycle(head))  # Output: True