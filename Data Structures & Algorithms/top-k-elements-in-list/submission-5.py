class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        groups = {}
        s = set(nums)
        u = sorted(nums)
        count = 1
        for i in range(len(u)):
            if i + 1 < len(u) and u[i] == u[i+1]:                
                count +=1
                groups[u[i]]=  count
            else:
                groups[u[i]]=  count
                count = 1  
            
            #count = [0] * len(nums)
        groups2 = sorted(groups, key=groups.get, reverse=True)
        final = groups2[:k]

        return final