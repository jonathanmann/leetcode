class Solution:	
	def reverse(self,x):
		sign = 1
		if x < 0: sign = -1
		x = abs(x)
		i = 0
		while 10 ** (i+1) <= x:
			i += 1
		rev = 0
		j = 0
		tmp = x
		while i >= 0:
			curr = (tmp//(10 ** i)) * (10 ** j)
			tmp = tmp - ((tmp//(10 ** i)) * (10 ** i))
			rev = rev + curr
			i -= 1
			j += 1
		if rev > 2147483648: return 0
		return rev * sign 
s = Solution()
print s.reverse(19)
