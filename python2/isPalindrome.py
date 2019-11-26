class Solution:	
	def isPalindrome(self,x):
		if x < 0: return False
		if x <= 9: return True
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
		return rev == x 
s = Solution()
print s.isPalindrome(919)
