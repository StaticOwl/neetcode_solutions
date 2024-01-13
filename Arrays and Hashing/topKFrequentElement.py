class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = {}
        res = []
        i=0
        for num in nums:
            if num in freq_map:
                freq_map[num] = freq_map[num]+1
            else:
                freq_map[num] = 1

        resmap = sorted(freq_map.items(), key=lambda item : item[1], reverse=True)

        for key,value in resmap:
            if i<k:
                res.append(key)
                i+=1
            else:
                break

        return res
