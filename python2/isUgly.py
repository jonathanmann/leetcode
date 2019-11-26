


class Solution(object):
    def isUgly(self,num):
        """
        :type num: int
        :rtype: boo
        """
        ugly_primes = [2,3,5]
        if num == 1 or num in ugly_primes:
            return True
        for p in ugly_primes:
            if num % p == 0:
                return self.isUgly(num/p)
        return False



class Solution(object):
    def isUgly(self,num):
        """
        :type num: int
        :rtype: boo
        """
        ugly_primes = [2,3,5]

        if num == 1 or num in ugly_primes:
            return True
        p_num = 1
        while num <> p_num:
            m = 0
            for p in ugly_primes:
                if num % p == 0:
                    m = 1
                    p_num = num
                    num = num/p
                    if num in ugly_primes:
                        return True
            if m == 0:
                return False
        return False

print Solution().isUgly(33)

