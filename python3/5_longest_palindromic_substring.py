#!/usr/bin/env python

class Solution:
    def longestPalindrome(self, s:str) -> str:
        l = len(s)
        longest = 0
        start = 0
        end = l
        if s == s[::-1]:
            return s
        p1 = self.longestPalindrome(s[start + 1:end])
        p2 = self.longestPalindrome(s[start:end - 1])
        if len(p1) > len(p2):
            return p1
        return p2

p = lambda s: print(Solution().longestPalindrome(s))
p("babad")
p("cbbd")
p("ac")
