class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        v = {'a','e','i','o','u','A','E','I','O','U'}
        t = []
        p = []
        for i,c in enumerate(s):
            if c in v:
                t.append(c)
                p.append(i)
        t.reverse()
        d = dict(zip(p,t))
        for e in d:
            s[e] = d[e]
        return ''.join(s)

print Solution().reverseVowels('aileetcode')
