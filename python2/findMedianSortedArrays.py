class Solution:
    def getKth(self, nums1, nums2, k):
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 > l2:
            return self.getKth(nums2, nums1, k)
        if l1 == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])

        p1 = min(k // 2, l1)
        p2 = k - p1
        
        if nums1[p1 - 1] <= nums2[p2 - 1]:
            return self.getKth(nums1[p1:], nums2, p2)
        else:
            return self.getKth(nums1, nums2[p2:], p1)
    
    def findMedianSortedArrays(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1 + l2) % 2 == 1: 
            return self.getKth(nums1, nums2, (l1 + l2) // 2 + 1)
        else:
            return (self.getKth(nums1, nums2, (l1 + l2) // 2) + self.getKth(nums1, nums2, (l1 + l2) // 2 + 1)) * 0.5 
