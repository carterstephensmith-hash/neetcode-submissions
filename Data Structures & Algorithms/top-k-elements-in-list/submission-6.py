class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        
        coount = 0
        for i in nums:
            groups[i] = groups.get(i,0) + 1
        groups2 = sorted(groups, key=groups.get, reverse=True)
        final = groups2[:k]
        return final


