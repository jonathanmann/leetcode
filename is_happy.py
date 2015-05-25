class Solution:
	def __init__(self):
		self.past_vals = set()
	def isHappy(self,n):
		digits = str(n)
		sq = 0
		for d in digits:
			sq = sq + int(d)**2
		if sq == 1:
			return True
		if sq in self.past_vals:
			return False
		self.past_vals.add(sq)
		return self.isHappy(sq)

s = Solution()
print s.isHappy(1000)
