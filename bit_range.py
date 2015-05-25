class Solution:
	def rangeBitwiseAnd(self,m,n):
		if m == 0: return m
		if m == n: return m
		while n > m:
			n = n & (n-1)
		return m & n
s = Solution()
print s.rangeBitwiseAnd(20000,2147483647)

"""
x = m
for i in range(m,n):
	x = i & (i+1) & x
return x
"""
