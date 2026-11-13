class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        solution = [0] * len(nums)
        index = 0
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        solve = 1
        solve2= 1
        for i in range(len(nums)):
            prefix[i] = solve
            solve *= nums[i]
            
            
        for i in range(len(nums)-1,-1,-1):

            suffix[i]=solve2
            solve2 *= nums[i]
        for i in range(len(nums)):
            solution[i]=prefix[i]*suffix[i]
        # print(suffix)   
        # print(prefix) 
        return solution