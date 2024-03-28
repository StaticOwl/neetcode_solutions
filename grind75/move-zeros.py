class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """ easy way would be to just simply run a double loop"""
        # count = 0
        # n = len(nums)
        # i = 0
        # while i < n:
        #     if nums[i] == 0:
        #         nums.remove(nums[i])
        #         nums.append(0)
        #         n -= 1
        #     else:
        #         i += 1
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                temp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = temp
                slow += 1