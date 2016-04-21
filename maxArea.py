"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left = 0
        right = len(height) - 1
        
        while right > left:
            tmp = min(height[right],height[left]) * (right - left)
            area = max(area,tmp)
            
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1



        """
        for i,e in enumerate(height):
            for j,m in enumerate(height):
                tmp = self.get_area(i,e,j,m)
                if tmp > mx:
                    mx = tmp
        """
        return area

    def get_area(self,x1,y1,x2,y2):
        h = min(y1,y2)
        w = x2 - x1
        return h * w


height = [46,53,93,82,78,20,49,76,43,67,52,41,65,38,97,98,56,32,85,11,49,90,68,95,38,53,96,94,57,36,93,55,89,87,89,67,59,90,96,2,58,0,95,75,38,44,73,94,76,10,57,25,1,25,21,91,30,69,85,39,57,31,95,46,70,84,66,29,75,14,83,85,14,79,60,52,23,85,98,0,96,55,77,49,32,50,92,62,20,78,53,29,9,48,76,79,85,94,60,60,60,43,97,74,74,9,78,98,94,76,50,42,83,79,43,67,30,36,81,2,66,34,31,27,35,59,58,20,53,18,32,13,13,29,39,88,90,17,38,84,45,40,79,80,19,22,99,49,10,80,51,76,67,83,3,2,42,61,74,48,31,6,13,45,87,53,85,77,22,75,13,20,67,92,0,86,67,0,88,77,32,91,6,99,26,61,53,69,75,27,69,6,33,82,3,72,87,40,49,10,15,63,30,82,7,82,21,74,34,9,4,67,0,10,18,27,23,72,48,98,51,69,57,37,3,60,9,91,1,59,53,68,22,35,3,29,69,76,56,4,37,12,23,89,74,41,68,97,65,68,96,17,37,53,54,41,65,63,84,18,22,89,87,96,76,42,78,45,70,34,1,7,46,24,96,20,66,65,69,31,33,65,0,23,70,54,64,36,18,0,54,92,41,93,89,17,87,19,14,57,53,16,64,51,40,61,23,58,78,92,90,63,10,90,86,80,97,2,68,15,2,75,59,95,68,0,64,56,19,79,65,24,47,30,27,87,43,50,46,73,95,88,36,5,30,23,37,27,25,58,94,80,33,6,75,1,6,40,9,26,19,27,50,66,9,30,5,52,80,3,77,27,43,13,84,74,36,22,53,14,80,48,94,65,6,69,18,12,61,80,90,32,7,93,50,16,23,56,20,3,11,97,31,55,10,15,29,99,89,34,13,21,34,59,86,40,28,5,53,42,37,43,74,44,36,25,60,59,33,80,15,44,77,98,51,39,65,32,38,55,67,3,28,1,62,67,42,43,24,47,85,61,90,59,5,79,36,65,90,21,97,5,66,74,55,17,13,21,50,4,28,69,7,56,70,70,23,64,65,99,11,50,60,2,61,65,33,50,82,23,71,79,81,89,5,36,59,71,57,61,75,37,30,34,94,0,56,69,65,21,69,76,71,29,30,85,47,15,35,29,39,6,61,72,48,66,8,7,89,18,68,64,55,98,99,1,50,7,23,15,29,92,44,52,73,26,89,72,42,24,2,33,83,15,5,31,33,65,38,23,83,58,87,91,56,38,44,58,98,67,74,27,11,70,31,85,48,21,57,90,97,11,75,80,78,80,63,12,46,53,35,81,11,74,72,19,65,69,78,63,36,4,42,48,26,73,85,74,46,94,17,44,58,92,24,36,73,40,48,71,93,35,52,57,62,77,28,27,46,6,42,34,62,36,34,88,61,71,63,8,66,32,52,24,24,28,60,49,20,61,20,66,48,73,23,10,2,51,89,0,10,31,34,72,19,69,61,81,40,76,89,58,8,93,82,84,73,95,34,94,8,6,12,56,31,35,19,33,38,8,33,48,40,68,73,11,89,86,92,81,62,33,92,22,78,26,6,52,21,92,98,81,99,10,90,30,97,9,16,87,17,49,36,9,69,61,21,10,47,65,44,61,99,36,83,77,62,41,81,36,86,79,17,37,41,59,67,90,68,83,78,38,85,66,47,6,27,20,17,26,86,61,87,85,97,22,14,59,15,96,47,1,27,65,38,69,24,58,59,45,93,37,83,30,55,30,37,82,3,54,8,89,67,47,74,16,69,40,27,85,36,75,38,64,92,29,85,68,87,96,13,32,86,96,63,41,79,52,24,82,58,84,71,25,32,97,41,1,89,68,38,26,95,77,90,87,6,27,56,45,23,69,77,9,18,92,51,97,96,27,31,54,11,54,79,95,3,72,49,92,93,87,70,88,16,12,28,74,39,84,19,63,5,49,72,75,93,75,24,90,2,55,44,66,61,76,13,64,48,62,9,93,2,79,82,70,92,10,45,83,46,64,46,3,65,71,79,59,98,3,49,53,59,45,19,72,21,84,89,22,99,98,15,1,29,49,23,73,11,68,57,57,85,55,61,50,78,92,9,77,95,10,30,6,56,1,79,77,85,68,99,84,18,67,37,47,16,61,21,28,81,30,85,66,85,98,17,64,42,26,93,38,89,23,96,45,24,75,74,61,95,74,46,13,93,35,13,9,96,86,37,78,16,75,96,53,25,13,69,68]

print Solution().maxArea(height)
