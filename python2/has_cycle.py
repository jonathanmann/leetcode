# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
	def hasCycle(self, head):
		if head is None: return False
		if head.next is None: return False
		if head.next.next is None: return False
		
		r1 = head
		r2 = head.next.next
		while r2 is not None:
			if r2.next is None: return False
			if r2.next.next is None: return False
			if r2 == r1: return True
			r1 = r1.next
			r2 = r2.next.next
		return False
		
