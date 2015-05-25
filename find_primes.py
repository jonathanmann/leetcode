import math
class Solution:
    # @param {integer} n
    # @return {integer}
	def countPrimes(self, n):
		if n == 1: return 0
		if n == 2: return 1
		primes = [2]
		for i in range(2,n):
			if self.is_prime(i,primes):
				primes.append(i)
		return len(primes)

	def is_prime(self,n,primes):
		s = math.sqrt(n)
		for prime in primes:
			if n % prime == 0:return False
			if prime >= s:	
				return True
		return True

s = Solution()
print s.countPrimes(1000000)
