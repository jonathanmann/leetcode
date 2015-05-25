class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param {ListNode} head
	# @param {integer} val
	# @return {ListNode}
	def removeElements(self, head, val):
		if head is not None:
			while head.val == val:
				head = head.next
				if head is None: return head
			curr = head
			while curr.next is not None:
				if curr.next.val == val:
					if curr.next.next is not None:
						curr.next = curr.next.next
					else:
						curr.next = None
				else:
					curr = curr.next
		return head

seq = ListNode(1)
#seq.next = ListNode(1)
#seq.next.next = ListNode(3)
#seq.next.next.next = ListNode(4)

s = Solution()
s.removeElements(seq,1)
print seq.val
#print seq.next.val
#print seq.next.next.val


