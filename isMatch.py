class Solution:	
	def isMatch(self,s,p):
            if s == p:
                return True
            s = '*'
            d = '.'
            l = len(p)
            i = 0
            while i < l:
                if p[i + 1] == '*':
                    
                    
s = Solution()
print s.isMatch(919)
