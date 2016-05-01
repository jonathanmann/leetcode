"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Solution(object):
    def isValid(self, s):
        """
        """
        d = {
                '(':{'t':0,'p':')','v':1},
                '{':{'t':1,'p':'}','v':1},
                '[':{'t':2,'p':']','v':1},
                ')':{'t':0,'p':'(','v':-1},
                '}':{'t':1,'p':'{','v':-1},
                ']':{'t':2,'p':'[','v':-1},
                }

        counts = [0,0,0]

        prev = ''
        for c in s:
            n = d[c]['t']
            counts[n] += d[c]['v']
            if counts[n] < 0:
                return False
            if prev:
                if d[c]['v'] == -1 and d[prev]['v'] == 1 and d[c]['p'] <> prev:
                    return False
            prev = c
        if sum(counts) <> 0:
            return False
        return True

s = '({[]()}){}{'
s ="[([]])"
z = Solution()
print z.isValid(s)
