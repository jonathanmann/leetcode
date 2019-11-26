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
        while i < h_len:
            if haystack[i:i + n_len] == needle:
                return i
            i += 1
        return -1
