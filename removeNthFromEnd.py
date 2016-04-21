class ListNode:
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution:	
	def removeNthFromEnd(self,head,n):
		if head is None: return None
		if n == 0 : return head
		node = head
		follower = None
		i = 1
		if n == 1 and node.next is None:return None
		while node is not None:
			if i == n:
				follower = head
			if node.next is None:
				if follower is None:
					return head
				if follower.next is not None:
					follower.next = follower.next.next
				return head

			if i > n:
				follower = follower.next	

			i += 1
			node = node.next
		return head

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
s = Solution()
s.removeNthFromEnd(l,5)
print l.next.next.next.val
print l.next.next.val
print l.next.val
print l.val




			
