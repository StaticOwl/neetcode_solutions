class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Important: Height can only be min of two heights for water to be stored.
        #TODO: Find min of two bars
        #TODO: Find Max of Volume/Area in this case of all
        left = 0
        right = len(height) - 1
        max_area = 0
        while (left < right):
            min_height = min(height[left], height[right])
            area = min_height * (right - left)
            if area > max_area:
                max_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area