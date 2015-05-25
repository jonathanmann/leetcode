class Solution:	
	def plusOne(self,digits):
		if digits == [9]: return [1,0]
		if digits[-1] != 9:
			digits[-1] += 1
			return digits
		digits.reverse()
		digits[0] = 0
		for i,digit in enumerate(digits[1:]):
			print i, digit
			if digit + 1 < 10:
				digits[i+1] = digit + 1
				digits.reverse()
				return digits
			else:
				if (i + 2) == len(digits):
					digits[i + 1] = 0
					digits.append(1)
					digits.reverse()
					return digits
				else:
					digits[i+1] = 0	
				
s = Solution()
digits = [8,9,9]
print s.plusOne(digits)

						
