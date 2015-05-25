class Solution:	
	def climbStairs(self,n):
		d = {0:1,1:1}
		for i in range(2,n + 1):
			d[i] = d[i - 2] + d[i - 1]
		return d[n]

s = Solution()
print s.climbStairs(5)



