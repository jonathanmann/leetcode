# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:	
	def mergeTwoLists(self,l1,l2): 
		if l1 is None: return l2
		if l2 is None: return l1
		if l1.val < l2.val:
			head = l1
			l1 = l1.next
		else:
			head = l2
			l2 = l2.next

		node = head
		while l1 is not None and l2 is not None:
			if l1.val < l2.val:
				node.next = l1
				l1 = l1.next
			else:
				node.next = l2
				l2 = l2.next
			node = node.next
		if l1 is not None:
			node.next = l1
		if l2 is not None:
			node.next = l2
		return head
	
		
s = Solution()
print s.mergeTwoLists(l1,l2)



