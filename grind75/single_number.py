class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for item in count:
            if count[item] == 1:
                return item
        return -1

# The other approach will be to sort and then count linearly and update with element change, but it involves sorting withi using Timsort will
# have worst case of O(nlogn)