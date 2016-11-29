"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
"""
from itertools import combinations as cm
class Solution:	
    def threeSum(self, nums):
        positions = range(len(nums))
        nums.sort()
        while len(nums) > 2 and nums[0] + nums[1] + nums[-1] > 0:
            print nums.pop()
        while len(nums) > 2 and nums[-1] + nums[-2] + nums[0] < 0:
            print nums.pop(0)
        s = set()
        for e in cm(nums,3):
            if sum(e) == 0:
                s.add(e)
        r = list(s)
        return r

    #def get_triplets(self,nums):

"""

class Solution:	
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i = 0
        r = []
        while i < len(nums) - 2:
            l = i + 1
            h = len(nums) - 1
            while l < h:
                t = [nums[i],nums[l],nums[h]]
                s = sum(t)
                if s == 0:
                    r.append(t)
                    l += 1
                    h -= 1
                    while l < h and nums[l] == nums[l-1]:
                        l += 1
                    while l < h and nums[h] == nums[h+1]:
                        h -= 1
                elif s > 0:
                    h -= 1
                elif s < 0:
                    l += 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return r


nums = [1,2,3,4,5]

nums = [-2,10,-14,11,5,-4,2,0,-10,-10,5,7,-11,10,-2,-5,2,12,-5,14,-11,-15,-5,12,0,13,8,7,10,6,-9,-15,1,14,11,-9,-13,-10,6,-8,-5,-11,6,-9,14,11,-7,-6,8,3,-7,5,-5,3,2,10,-6,-12,3,11,1,1,12,10,-8,0,8,-5,6,-8,-6,8,-12,-14,7,9,12,-15,-12,-2,-4,-4,-12,6,7,-3,-6,-14,-8,4,4,9,-10,-7,-4,-3,1,11,-1,-8,-12,9,7,-9,10,-1,-14,-1,-8,11,12,-5,-7]

nums = [-1,0,1,2,3,4]
nums = [-10,-8,-6,-4,-2,0,2,3,4]
nums = [-4,-8,7,13,10,1,-14,-13,0,8,6,-13,-5,-4,-12,2,-11,7,-5,0,-9,-14,-8,-9,2,-7,-13,-3,13,9,-14,-6,8,1,14,-5,-13,8,-10,-5,1,11,-11,3,14,-8,-10,-12,6,-8,-5,13,-15,2,11,-5,10,6,-1,1,0,0,2,-7,8,-6,3,3,-13,8,5,-5,-3,9,5,-4,-14,11,-8,7,10,-6,-3,11,12,-14,-9,-1,7,5,-15,14,12,-5,-8,-2,4,2,-14,-2,-12,6,8,0,0,-2,3,-7,-14,2,7,12,12,12,0,9,13,-2,-15,-3,10,-14,-4,7,-12,3,-10]
nums = [-1,0,1,2,-1,-4]
nums = [12,13,-10,-15,4,5,-8,11,10,3,-11,4,-10,4,-7,9,1,8,-5,-1,-9,-4,3,-14,-11,14,0,-8,-6,-2,14,-9,-4,11,-8,-14,-7,-9,4,10,9,9,-1,7,-10,7,1,6,-8,12,12,-10,-7,0,-9,-3,-1,-1,-4,8,12,-13,6,-7,13,5,-14,13,12,6,8,-2,-8,-15,-10,-3,-1,7,10,7,-4,7,4,-4,14,3,0,-10,-13,11,5,6,13,-4,6,3,-13,8,1,6,-9,-14,-11,-10,8,-5,-6,-7,9,-11,7,12,3,-4,-7,-6,14,8,-1,8,-4,-11]
nums = [-1,0,1,2,-1,-4]
nums = [0,0,0,0]
s = Solution()
print s.threeSum(nums)
