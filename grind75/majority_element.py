#takes O(n) space and linear time
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target=(len(nums)) // 2
        count = Counter(nums)
        for num, freq in count.items():
            if freq > target:
                return num

#No Extra Space
'''
idea:
considering bracket closure logic. taking the first element as start, I will keep on increasing the count if I get the same value in the nums
and decrease it if I don't get same. Now at any instance if count is 0, that means the current element has more count than the other one. this 
case would warrant that I update the temp element with current element and proceed with the same again.
Think of this [2,2,1,1,1,2,2]: for first 2 elements the count is 2, the next 2 elements the count will go back to 0, now for the 5th element,
since the value is different (2!=1) the temp will be updated to 1 and count 1. Now going forward, again for 6th element, the count is back to 0,
and for last element, temp will update back to 1.

This algorithm has nothing to do with target. And basically searches for the element with maximum occurrence, which can only be one element.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        temp = 0
        target = len(nums) // 2
        for num in nums:
            if count == 0:
                temp = num
            
            count += 1 if temp == num else -1

        return temp