class Solution:	
    def isMatch(self,s,p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        p = self.simplify(p)
        if self.fails_reqs(s,p):
            return False
        else:
            return self.isMatchR(s,p)

    def isMatchR(self,s,p):
        if len(p) == 0:
            return len(s) == 0

        if len(p) == 1:
            # base case
            if len(s) < 1:
                return False
            elif p[0] != s[0] and p[0] != '.':
                return False
            else:
                return self.isMatchR(s[1:],p[1:])

        if p[1] != '*':
            # second char not '*'
            if len(s) < 1:
                return False
            elif p[0] != s[0] and p[0] != '.':
                return False
            else:
                return self.isMatchR(s[1:],p[1:])

        else:
            # second char is '*'
            if self.isMatchR(s,p[2:]):
                return True
            i = 0
            while i < len(s) and (s[i] == p[0] or p[0] == '.'):
                if self.isMatchR(s[i+1:],p[2:]):
                    return True
                i += 1
            return False

    def fails_reqs(self,s,p):
        required = {}
        included = {}
        i = len(p) - 1
        prev = ''
        while i > 0:
            if prev <> '*' and p[i] <> '.' and p[i] <> '*':
                if p[i] not in required:
                    required[p[i]] = 1
                else:
                    required[p[i]] += 1
            prev = p[i]
            i -= 1
        for e in s:
            if e not in included:
                included[e] = 1
            else:
                included[e] += 1

        for e in required:
            if e not in included:
                return True
            elif required[e] > included[e]:
                return True
        return False

    def simplify(self,p):
        i = 3
        block = set()
        while i < len(p) - 1:
            if p[i] == '*':
                if (p[i],p[i-1]) == (p[i-2],p[i-3]):
                    block.update([i-1,i])
            i += 1

        sim = []
        for i,e in enumerate(p):
            if i not in block:
                sim.append(e)
        return ''.join(sim)

"""
s = Solution()
print s.isMatch("aa","a") # false
print s.isMatch("aa","a*") # true
print s.isMatch("aa",".*") # true
print s.isMatch("ab",".*") # true
print s.isMatch("aab","c*a*b") # true
print s.isMatch("aab","c*a*b") # true
print s.isMatch("ab",".*c") # false
print s.isMatch("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c") # false
print s.isMatch("aaaaaaaaaaaaab","a*a*a*aaa*a*a*a*a*a*a*c") # false
print s.isMatch("jzzzzn","j.*n")
print s.isMatch("aa","aa") # true
"""
