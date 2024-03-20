#TODO: Visit https://leetcode.com/problems/trapping-rain-water/ for problem description
#TODO: Check this solution once again as it is not clear to me and I have taken help to solve this problem
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left, right = 0, len(height)-1
        leftMax, rightMax = height[left], height[right]
        area = 0
        while left < right:
            if leftMax <= rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                area += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                area += rightMax - height[right]

        return area
