class Solution(object):
    def isPowerOfTwo(self,n):
        """
        :type n: int
        :rtype: boo
        """
        if n == 1 or n == 2:
            return True
        while n > 2:
            if n % 2 != 0:
                return False
            n = n / 2
            if n == 2:
                return True
        return False

print Solution().isPowerOfTwo(32)

