class Solution:	
	def longestCommonPrefix(self, strs):
		if not strs: return ""
		l = None
		for s in strs:
			if l is None:
				l = s
			else:
				tmp = []
				i = 0
				while i < len(s) and i < len(l) and s[i] == l[i]:	
					tmp.append(s[i])
					i += 1
				l = ''.join(tmp)
		return l


strs = ['zaaz','zaazr']
s = Solution()
print s.longestCommonPrefix(strs)	
