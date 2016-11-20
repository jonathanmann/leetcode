class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "" and haystack is not None:
            return 0
        h_len = len(haystack)
        n_len = len(needle)
        if n_len > h_len:
            return - 1
        i = 0 
        while i + n_len <= h_len:
            j = 0
            while j <= n_len/2:
                if haystack[i + j] != needle[j] or haystack[i + n_len - 1 - j] != needle[-1-j]:
                    break
                if j >= n_len/2:
                    return i
                j += 1
            i += 1
        return -1

print Solution().strStr("mississippi","issip")


                
            
