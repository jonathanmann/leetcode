#!/usr/bin/env python
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        total = len1 + len2
        if nums1[len1//2] > nums2[len2//2]:
            self.findMedianSortedArrays(

        return 0
    def getMedian(self,nums):
        if not nums:
            return 0
        ln = len(nums)
        if ln % 2 == 0:
            median =  

p = lambda n1,n2: print(Solution().findMedianSortedArrays(n1,n2))

p([1,3],[2])
p([1,2],[3,4])

