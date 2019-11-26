class Solution:
	# @param {string} s
	# @param {string} t
	# @return {boolean}
	def isIsomorphic(self, s, t):
		if s == t:
			return True
		if len(s) != len(t):
			return False
		t_d = self.get_dict(s,t)
		s_d = self.get_dict(t,s)
		print t_d,s_d
		if not t_d or not s_d:return False
		
		for c in t_d:
			if c != s_d[t_d[c]]:
				return False
		return True

	def get_dict(self,m,n):
		d = {}
		for i,c in enumerate(m):
			if n[i] not in d:
				d[n[i]] = c
			else:
				if d[n[i]] != c: return False
		return d

	#s_test = []
	#for c in t:
	#	s_test.append(d[c])
	#return s == ''.join(s_test)
sol = Solution()
print sol.isIsomorphic('ba','ab')
