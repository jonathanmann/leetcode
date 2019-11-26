class Solution:
    def findDuplicate(self,nums):
        ln = len(nums)
        tmp = -1
        for i in range(ln):
            tmp = nums[i]
            for j in range(ln):
                if tmp == nums[j]:
                    return tmp
            
