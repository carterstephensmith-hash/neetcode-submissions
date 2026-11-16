class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = set()
        nums = set(nums)
        for i in nums:
            if i-1 in nums:
                continue
            else:
                start.add(i)
        count = 0
        
        for i in start:
            count2 = 1
            current = i
            while current + 1 in nums:
                count2 +=1
                current +=1
            if count2 > count:
                count = count2
        return count