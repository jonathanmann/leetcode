class Solution:	
	def convert(self,s,numRows):
		if numRows == 1 or numRows >= len(s): return s
		final = [[] for row in xrange(numRows)]
		curr = 0
		for i in xrange(len(s)):
			if curr == numRows - 1: d = 0
			if curr == 0: d = 1
			final[curr].append(s[i])
			if d == 1:curr += 1
			if d == 0:curr -= 1
		return "".join(["".join(final[i]) for i in xrange(numRows)])

s = "PAYPALISHIRING"
sol = Solution()
print sol.convert(s,3)

