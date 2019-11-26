class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        A = {}
        B = {}
        for c in s:
            A = self.incrementElement(A,c)
        for c in t:
            B = self.incrementElement(B,c)
        return A == B

    def incrementElement(self,d,c):
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1 
        return d

print Solution().isAnagram('azp','zzap')
