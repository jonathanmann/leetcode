class Solution:
	def singleNumber(self, nums):
		d = {}
		for num in nums:
			if num not in d:
				d[num] = 1
			else:
				d[num] = d[num] + 1
		for e in d:
			if d[e] != 2:
				return e			


nums = [1,1,2,2,2,3,3,4,4]
s = Solution()
print s.singleNumber(nums)
