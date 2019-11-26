class Solution:	
	def removeElement(self,nums,val):
		print nums
		l = len(nums)
		r = l
		for i in xrange(l):
			if nums[i] == val:
				k = 1
				while nums[i + k] == val:
					k += 1
				l -= k
				for j in range(i,l):
					nums[j] = nums[j+k]
				if i + k + 1 == len(nums): return l,nums
		return l,nums


t = [1,2,3,3,4,3,5]
t = [3,3,3,1]
t = [1,3,3,4]
t = [3]
s = Solution()
print s.removeElement(t,3)
