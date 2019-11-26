class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, node):
        while node.next is not None:
            node.val = node.next.val
            if node.next.next is None:
                node.next = None
            else:
                node = node.next

z = ListNode(1)
z.next = ListNode(2)
z.next.next = ListNode(3)
z.next.next.next = ListNode(4)

Solution().deleteNode(z.next)

print z.val
print z.next.val
print z.next.next.val
print z.next.next.next
