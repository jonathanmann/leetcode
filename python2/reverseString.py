class Solution:	
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        sz = len(s)
        hf = sz//2
        i = 0
        while i < hf:
            s[i],s[sz - 1 -i] = s[sz - 1 -i],s[i]
            print s
            i += 1
        return ''.join(s)
                    
                    
s = Solution()
print s.reverseString('abcde')
