#!/usr/bin/env python
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        ll = []
        current = self
        while current is not None:
            ll.append(str(current.val))
            current = current.next
        return '->'.join(ll)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i1 = self.list_to_int(l1)
        i2 = self.list_to_int(l2)
        return self.int_to_list(i1 + i2)

    def list_to_int(self,ll: ListNode) -> int:
        n = 0
        place = 1
        while ll is not None:
            n += ll.val * place
            place *= 10
            ll = ll.next
        return n

    def int_to_list(self,n: int) -> ListNode:
        head = None
        while n:
            current = ListNode(n % 10)
            if head is None:
                head = current
                prev = head
            else:
                prev.next = current
                prev = current
            n = n // 10
        if head is None:
            return ListNode(0)
        return head


def populate_linked_list(nums: List) -> ListNode:
    head = None
    current = None
    nums.reverse()
    while nums:
        if head is None:
            head = ListNode(nums.pop())
            current = head
        else:
            current = ListNode(nums.pop())
            prev.next = current
        prev = current
        current = current.next
    return head

a1 = [2,4,3]
a2 = [5,6,4]

l1 = populate_linked_list(a1)
l2 = populate_linked_list(a2)

ln = Solution().addTwoNumbers(l1,l2)
print(ln)
