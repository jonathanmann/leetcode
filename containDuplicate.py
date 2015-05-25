class Solution:
	def containsDuplicate(self,nums):
		d = set()
		for e in nums:
			if e in d:
				return True
			else:
				d.add(e)
		return False
