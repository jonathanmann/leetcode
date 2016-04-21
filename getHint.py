class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s = {}
        for e in secret:
            if e in s:
                s[e] += 1
            else:
                s[e] = 1
        b = 0
        c = 0
        for i,e in enumerate(guess):
                if e == secret[i]:
                    b += 1
                    if s[e] == 1:
                        del s[e]
                    else:
                        s[e] -= 1
        for e in guess:
                if e in s:        
                    c += 1
                    if s[e] == 1:
                        del s[e]
                    else:
                        s[e] -= 1

        return str(b)+ "A" + str(c) + "B"

s = Solution()
print s.getHint("1807","7810")
print s.getHint("1123","0111")
print s.getHint("1122","1222")
