class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        left = 0
        right = len(numbers) - 1

        while(right-left >= 1):
            sum = numbers[left] + numbers[right]
            if sum < target:
                left +=1
            elif sum > target:
                right -=1
            else:
                return [x+1 for x in [left, right]]
