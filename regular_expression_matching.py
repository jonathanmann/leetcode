class Solution:
	def isMatch(self, s, p):
		if s == p: return True
		s = s.split()
		p = p.split()
		if p[0] != '*' and p[0] != '.' and p[0] != s[0]: return False	

s = Solution()
s.isMatch("aa","a")
