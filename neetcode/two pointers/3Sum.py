class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        sorted_nums = sorted(nums)
        res = []
        left = 0
        for left in range (0, n-1):
            mid = left + 1
            right = n -1
            if left > 0 and sorted_nums[left] == sorted_nums[left - 1]:
                continue
            while mid < right:
                curr_sum = sorted_nums[left] + sorted_nums[mid] + sorted_nums[right]
                combination = [sorted_nums[left], sorted_nums[mid], sorted_nums[right]]
                if curr_sum == 0:
                    res.append(combination)
                    while mid < right and sorted_nums[mid] == sorted_nums[mid+1]:
                        mid += 1
                    while mid < right and sorted_nums[right] == sorted_nums[right - 1]:
                        right -= 1
                    mid += 1
                    right -= 1
                else:
                    if curr_sum > 0:
                        right -= 1
                    elif curr_sum < 0:
                        mid += 1

        return res

