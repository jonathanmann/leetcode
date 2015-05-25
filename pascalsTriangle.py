class Solution:	
	def generate(self,numRows):
		if numRows <= 0:
			return []
		elif numRows == 1:
			return [[1]]
		elif numRows == 2:
			return [[1],[1,1]]
		else:
			odd = numRows % 2
			prev = self.generate(numRows - 1)
			lastRow = prev[-1]
			rowHalf = lastRow[:(numRows // 2 + 1)]
			print rowHalf, numRows //2 + 1
			finalHalf = []
			for i,e in enumerate(rowHalf):
				if i == 0: finalHalf.append(1)
				else:
					finalHalf.append(rowHalf[i] + rowHalf[i-1])
			if odd:
				fullRow = finalHalf + finalHalf[:-1][::-1]
			else:
				fullRow = finalHalf[:-1] + finalHalf[:-1][::-1]
			prev.append(fullRow)
			return prev

s = Solution()
print s.generate(7)
				
				
				
