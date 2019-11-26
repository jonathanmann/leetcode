class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ll = len(nums)
        end = ll - 1
        i = 0
        while i < end:
            if nums[i] == nums[i + 1]:
                nums[i + 1],nums[end] = nums[end],nums[i + 1]
                end -= 1
                j = i + 1 
                while j < end:
                    nums[j],nums[j + 1] = nums[j + 1], nums[j]
                    j += 1
            i += 1
        return end + 1
                
nums = [1,2,3,3,4,5,5,6,6,7,7,9]
nums = [1,1,2]
nums = []
print Solution().removeDuplicates(nums)
print nums
