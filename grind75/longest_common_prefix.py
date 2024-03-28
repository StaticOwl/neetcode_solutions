# Uses Sorting which is the maximum contributor in the time complexity, the other solution offers O(n^2), this will be O(nlogn) TIMSORT
#TODO: Understand TIMSORT
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        res = []
        for i in range (0, min(len(first), len(last))):
            if first[i] == last[i]:
                res.append(first[i])
            else:
                break
        return ''.join(res)