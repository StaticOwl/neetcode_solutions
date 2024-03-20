#O(logn) I am trying to reduce the size of the array using mid finding approach takes 200ms
def search(self, nums: List[int], target: int) -> int:
    mid = int(len(nums)/2)
    idx = 0
    if nums[-1] < target:
        return -1
    while nums and target != nums[mid]:
        if mid == 0:
            return -1
        if target > nums[mid]:
            nums = nums[mid:]
            idx += mid
        elif target < nums[mid]:
            nums = nums[:mid]
        mid = int(len(nums)/2)
    return mid+idx if nums else -1