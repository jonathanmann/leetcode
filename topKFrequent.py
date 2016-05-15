class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        seq = sorted([(d[y],y) for y in d],key=lambda x: x[0], reverse=True)
        frq = []
        i = 0
        while i < k:
            frq.append(seq[i][1])
            i += 1
        return frq


nums = [1,2,1,2,3,4,4,4]
k = 2
print Solution().topKFrequent(nums,k)
