class Solution:
	def rotate(self,nums,k):
		n = len(nums)
		k = k % n
		while k > 0:
			self.move_one(nums,n)
			k -= 1

	def move_one(self,nums,n):
		last = nums[-1]
		for i in range(n-1,0,-1):
			nums[i] = nums[i-1]
		nums[0] = last

s = Solution()
a = [1,2,3,4,5,6,7]
s.rotate(a,10)
print a
