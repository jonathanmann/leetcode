class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        else:
            return (num - 9  * ((num - 1) // 9))

print Solution().addDigits(33)
