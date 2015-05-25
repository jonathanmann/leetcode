class Solution:
	def titleToNumber(self,s):
		
		s = s.upper()[::-1]
		column = 0
		for i,c in enumerate(s):
			column += (ord(c) - 64) * 26 ** i
		return column 
z = Solution()
print z.titleToNumber('aB')
