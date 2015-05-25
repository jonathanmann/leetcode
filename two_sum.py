class Solution:
	def twoSum(self,nums=(6, 7, 11, 15, 3, 6, 5, 3), target=6):
		d = {v: i for i, v in enumerate(nums)}
		return next(( (i+1, d.get(target-v)+1) 
				for i, v in enumerate(nums) 
					if d.get(target-v, i) != i), None)

nums = [2,7,11,15]
t = 9
s = Solution()
print s.twoSum()		
