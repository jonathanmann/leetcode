class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        h = [] # populated with tuples (invalid_next,valid_next)
        for i,e in enumerate(nums):
            if i == 0:
                h.append((e,0))
            else:
                h.append(((e + h[i - 1][1]), max(h[i - 1][0],h[i - 1][1])))
        return max(h[-1])

nums = [50,40,20,70,35,95,45,60,70,80]
nums = []
print Solution().rob(nums)
