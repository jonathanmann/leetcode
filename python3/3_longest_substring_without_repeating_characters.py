#!/usr/bin/env python

class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        length = 0
        used = set()
        start = 0
        end = 0
        slen = len(s)
        while end < slen:
            if s[end] not in used:
                length = max(end - start + 1,length)
                used.add(s[end])
                end += 1
            else:
                used = set()
                start += 1
                end = start
        return length

s = lambda x: print(Solution().lengthOfLongestSubstring(x))
