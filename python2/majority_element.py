class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def majorityElement(self, nums):
		maj = len(nums)/2
		d = {}
		for e in nums:
			if e not in d:
				d[e] = 1
			else:
				d[e] = d[e] + 1

			if d[e] >= maj + 1:
				return e

s = Solution()
a = [6,5,5]
print s.majorityElement(a)
print a
