class Solution:
	def intToRoman(self,num):
		rn = ''
		remaining = num
		while remaining > 0:
			subtrahend, rn_n = self.convert_rmn(remaining)
			rn += rn_n
			remaining -= subtrahend
		return rn
	
	def convert_rmn(self,remaining):
		opts = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
		itr = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
		
		for opt in opts:
			if remaining >= opt:
				return opt, itr[opt]
				
				
s = Solution()
print s.intToRoman(93)

