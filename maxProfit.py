class Solution:
	def maxProfit(self,prices):
		profit = 0
		if not prices:
			return 0
		prev = prices[0]
		for p in prices[1:]:
			p_prof = prev - p
			print p_prof
			
			
s = Solution()


prices = [50,60,70,80,30,50,100,200,180,300,200,100,50]
s.maxProfit(prices)
