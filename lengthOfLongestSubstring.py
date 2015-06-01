class Solution:
	def lengthOfLongestSubstring(self, s):
		d = {}
		#ss = [0] 
		start = -1
		mx_len = 0
		for i in range(len(s)):
			if s[i] not in d:
				d[s[i]] = i
			else:
				if d[s[i]] > start: start = d[s[i]]
				print 'place : ',i ,'latest : ', d[s[i]],'start : ', start
				d[s[i]] = i
			#ss.append(i - start)
			if i - start > mx_len: mx_len = i - start
		print d
		return mx_len
		#return ss


s = Solution()
st = "ppczpvxsqqarvvawuzwjopsdsfsee"
#st = "abcdabcrb"
#st = "ababc"
#st = "cd"
print s.lengthOfLongestSubstring(st)

"""
		if not s:return 0  
		d = {}  
		maxlen = i = 0  
		for j in range(len(s)):  
			if not d.has_key(s[j]):  
				d[s[j]] = j  
			else:  
				while s[i] != s[j]:  
					del d[s[i]]  
					i+=1  
				i+=1  
			maxlen = max(maxlen, j-i+1)
		return maxlen
""" 
"""
	def lengthOfLongestSubstring(self, s):
		letters = set()
		for letter in s:
			letters.add(letter)
		d = {}
		l_len = len(letters)
		for letter in letters:
			d[letter] = 0

		sub_strings = [0]
		for i in range(len(s)):
			dc = d.copy()
			sub_strings.append(self.get_sub_strings(s[i:],dc,l_len))
		return max(sub_strings)

	def get_sub_strings(self,s,d,l_len):
		s_s = 0
		for letter in s:
			if d[letter] == 1:
				return s_s
			if s_s == l_len:
				return s_s
			d[letter] = 1
			s_s += 1
		return s_s	
"""




