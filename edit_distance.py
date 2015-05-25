class Solution:
	# @param {string} word1
	# @param {string} word2
	# @return {integer}
	def minDistance(self, word1, word2):
		if word1 == word2: return 0
		return self.f(word1,word2,{})
	def f(self, word1, word2, d):
		if len(word2)>len(word1):
			return self.f(word2, word1, d)
		if d.__contains__(tuple([word1,word2])):
			return d[tuple([word1,word2])]
		if word2=='' or word1==word2:
			return len(word1)
		if word1[0]==word2[0]:
			d[tuple([word1,word2])]=self.minDistance(word1[1:], word2[1:])
		else:
			a=1+self.minDistance(word1[1:], word2)
			b=1+self.minDistance(word1, word2[1:])
			c=1+self.minDistance(word1[1:], word2[1:])
			d[tuple([word1,word2])] = min(a,b,c)
		return d[tuple([word1,word2])]

s = Solution()
word1 = 'bird'
word2 = 'airid'
print s.minDistance(word1,word2)
