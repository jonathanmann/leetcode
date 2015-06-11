class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        import re
        try:
            i = 0
            while str[i] == ' ':
                str = str[i+1:]
            p = re.compile('^(\+|\-)(\+|\-)')
            if p.findall(str): return 0
            str = str.replace('+','')
            s2 = []
            for i,e in enumerate(str):
                if e in ['+','-','1','2','3','4','5','6','7','8','9','0']:
                    s2.append(e)
                else:
                    break
            str = "".join(s2)
            r = int(str)
            if r >= 2147483647: return 2147483647
            if r <= -2147483648: return -2147483648
            return r
        except:
            return 0
