class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        nums = len(numbers)
        first = 0
        last = nums - 1

        for i in range(nums):

            if numbers[first] + numbers[last] == target:
                return [first+1,last+1]

            elif numbers[first] + numbers[last] > target:
                last -=1

            elif numbers[first] + numbers[last] < target:
                first +=1