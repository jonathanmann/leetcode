class Solution:
    def wordPattern(self, pattern, str):
        keys = list(pattern)
        values = str.split()
        hm = {}
        used = set()
        if len(keys) != len(values):return False
        for i,key in enumerate(keys):
            v = values[i]
            if key in hm:
                if hm[key] != v:
                    return False
            else:
                if v in used: return False
                hm[key] = v
                used.add(v)
        return True

print Solution().wordPattern("abxba","key b ra b key")
