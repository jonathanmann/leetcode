class Solution:
    def maxProfit(self,prices):
        if not prices:
            return 0

        n = len(prices)
        
        profit = 0
        min_price = prices[0]
        for i in range(1,n):
            profit = max(profit,prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return profit

        """
        px = []
        for i,e in enumerate(prices):
            px.append((e,i))
        p = sorted(px, key=lambda x: x[0])
	i = 0
        j = len(prices) - 1
        print p
        while i < j:
            if p[j][1] > p[i][1]:
                return p[j][0] - p[i][0]
            print p[j],p[i]
            i += 1
            j -= 1
			
        """
s = Solution()


prices = [400,50,60,70,80,30,50,100,200,180,300,200,100,50]
#prices = [20,55,30,20,25,50]
print s.maxProfit(prices)
