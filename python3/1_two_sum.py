#!/usr/bin/env python
from typing import List, Tuple, Dict, TextIO

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_check = {}
        for i,e in enumerate(nums):
            if (target - e) in num_check:
                return[num_check[target - e],i]
            num_check[e] = i
