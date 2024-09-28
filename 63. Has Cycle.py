class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
   slow = fast = head
   
   while fast and fast.next:
       slow = slow.next
       fast = fast.next.next
       if fast == slow:
           return True
       return False

head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
head.next = node2
node2.next = node3
node3.next= node4
node4.next = None

print(has_cycle(head))