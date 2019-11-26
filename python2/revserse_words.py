class Solution:
	def reverseWords(self,s):
		s = s.split()
		s.reverse()
		return ' '.join(s)


s = "the sky is blue"
sol = Solution()
print sol.reverseWords(s)
