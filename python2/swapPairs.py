class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        node = head
        while node.next is not None:
            c = node
            n = node.next
            t = node.val
            c.val = n.val
            n.val = t
            if node.next.next is None:
                return head
            node = node.next.next
        return head

        
seq = [1,2,3,4,5,6]
seq = [1,2]
seq = []
head = ListNode(1)
x = head
for e in seq[1:]:
    y = ListNode(e)
    x.next = y
    x = y
x.next = ListNode(seq[-1])
    
Solution().swapPairs(head)

node_list = []
node = head
while node.next is not None:
    node_list.append(str(node.val))
    node = node.next
    
print ' -> '.join(node_list)
