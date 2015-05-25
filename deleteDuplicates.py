class ListNode:
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution:
	def deleteDuplicates(self,head):
		if head is None: return None
		s = set()
		s.add(head.val)
		node = head.next
		prev = head
		while node is not None: 
			if node.val in s:
				prev.next = node.next
			else:
				s.add(node.val)
				prev = node
			node = node.next
		return head

s = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(2)
s.deleteDuplicates(l)

print l.next.next

	
					
