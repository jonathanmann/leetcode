class Solution:
	def permute(self, nums):
		import itertools
		ps = []
		for p in itertools.permutations(nums):
				ps.append(p)						
		return ps

nums = [1,2,3,4]
s = Solution()
print s.permute(nums)
