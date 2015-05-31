class ListNode:
	def __init__(self,x):
		self.val = x
		self.next = None
class Solution:	
	def addTwoNumbers(self, l1, l2):
		if l1 is None: return l2
		if l2 is None: return l1
		node1 = l1
		node2 = l2
		rl = ListNode(None)
		head = rl
		carry = 0
		while node1 is not None and node2 is not None:
			rnode = node1.val + node2.val + carry	
			if rnode > 9:
				carry = 1
				rl.val = rnode - 10
			else:
				carry = 0
				rl.val = rnode

			if node1.next is not None or node2.next is not None or carry == 1:
				rl.next = ListNode(None)
				rl = rl.next

			node1 = node1.next
			node2 = node2.next

		if node1 is not None:
			get_remaining(node1,rl,carry)
		else:
			get_remaining(node2,rl,carry)

		if node1 is None and node2 is None:
			if carry == 0:
				return head
			if carry == 1:
				rl.val = 1
				return head
		return head

def get_remaining(node,rl,carry):
	while node is not None:
		rnode = node.val + carry
		if rnode > 9:
			carry = 1
			rl.val = rnode - 10
		else:
			carry = 0
			rl.val = rnode
		node = node.next
		if node is not None:
			rl.next = ListNode(None)
			rl = rl.next
		if node is None and carry == 1:
			rl.next = ListNode(1)
			rl = rl.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(2)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


s = Solution()
head = s.addTwoNumbers(l1,l2)

output = []
while head is not None:
	output.append(str(head.val))
	head = head.next
print ''.join(output)

l1 = ListNode(0)
l2 = ListNode(0)
s = Solution()
head = s.addTwoNumbers(l1,l2)

#print head.val, head.next.val, head.next.next.val, head.next.next.next.val
output = []
while head is not None:
	output.append(str(head.val))
	head = head.next
print ''.join(output)

l1 = ListNode(5)
l2 = ListNode(5)
s = Solution()
head = s.addTwoNumbers(l1,l2)

output = []
while head is not None:
	output.append(str(head.val))
	head = head.next
print ''.join(output)

l1 = ListNode(1)
l2 = ListNode(9)
l2.next = ListNode(9)
s = Solution()
head = s.addTwoNumbers(l1,l2)

output = []
while head is not None:
	output.append(str(head.val))
	head = head.next
print ''.join(output)


