class Solution:
	def romanToInt(self,s):
		rns = {'':0,'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
		p = ''
		total = 0
		for c in s:
			if rns[p] < rns[c]:
				total = total - 2 * rns[p]
			p = c
			total = total + rns[c]
		return total

s = Solution()
s.romanToInt('III')
s.romanToInt('IV')
s.romanToInt('IX')
print s.romanToInt('CD')

