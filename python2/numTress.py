class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        if n == 0: return 1
        num = 1
        for i in range(0, n):
            num = num * (4 * i + 2) / (i + 2)
        return num

s = Solution()
print s.numTrees(2)
