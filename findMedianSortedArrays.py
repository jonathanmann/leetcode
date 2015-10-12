class Solution:
    def __init__(self,nums1,nums2):
        print self.findMedianSortedArrays(nums1,nums2)

    def findMedianSortedArrays(self,nums1,nums2):
        m1 = self.get_sorted_median(nums1)
        m2 = self.get_sorted_median(nums2)
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 > l2:
            nums1,nums2,l1,l2,m1,m2 = nums2,nums1,l2,l1,m2,m1

        if l1 == 0:
            if l2 == 0:
                return None
            else:
                return self.get_sorted_median(nums2)
        elif m1 == m2: 
            return m1
        elif l1 == 1:
            if l2 == 1:
                return (nums1[0] + nums2[0]) / 2.0
            elif l2 % 2 != 0:
                m3 = self.get_unsorted_median([nums2[l2 // 2 - 1],nums2[l2 // 2 + 1], m1])
                return (m2 + m3) / 2.0
            else:
                m3 = self.get_unsorted_median([nums2[l2 // 2 - 1],nums2[l2 // 2], m1])
                return m3
        elif l1 == 2:
            if l2 == 2:
                return (max(nums1[0],nums2[0]) + min(nums1[1],nums2[1]))/2.0
            elif l2 % 2 != 0:
                return self.get_unsorted_median([m2,max(nums1[0],nums2[l2 // 2 - 1]),min(nums1[1],nums2[l2 // 2 + 1])])
            else:
                return self.get_unsorted_median([nums2[l2 // 2],nums2[l2 // 2 - 1],max(nums1[0],nums2[l2 // 2 - 2]), min(nums1[1],nums2[l2 // 2 + 1])])
        else:
            l1_r = l1 % 2
            l2_r = l2 % 2
            if m1 > m2:
                return self.findMedianSortedArrays(nums1[:l1 // 2 + l1_r],nums2[l2 // 2:])
            else:
                return self.findMedianSortedArrays(nums1[l1 // 2:],nums2[:l2 // 2 + l2_r])

    def get_unsorted_median(self,a):
        a.sort()
        return self.get_sorted_median(a)

    def get_sorted_median(self,a):
        if a == []: 
            return []
        if len(a) % 2 != 0:
            return a[len(a) // 2]
        else:
            return (a[len(a) // 2 - 1] + a[len(a) // 2 ]) / 2.0

nums1 = [1,9,10,12]
nums2 = [5,8,11,15]

nums2 = [1,2,3]
nums1 = [4,5,6]

Solution(nums1,nums2)


