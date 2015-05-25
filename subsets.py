class Solution:
	def subsets(self,nums):
		import itertools
		p_set = [[]]
		for i in range(len(nums)):
				for e in itertools.combinations(nums,i + 1):
					p_set.append(sorted(e))
		return p_set

s = Solution()
ss = [1,2,3]
print s.subsets(ss)
