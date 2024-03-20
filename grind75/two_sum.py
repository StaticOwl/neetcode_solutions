#41ms
def twoSum(self, nums: List[int], target: int) -> List[int]:
        tally = {}
        for i in range (0, len(nums)):
            if nums[i] not in tally:
                tally[target-nums[i]] = i
            else:
                return [tally[nums[i]], i]
        return []