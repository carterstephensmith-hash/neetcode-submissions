class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        numbers = len(sort)
        solution = []

        for i in range(numbers):
            
            if i > 0 and sort[i] == sort[i - 1]:
                continue

            second = i + 1
            last = numbers - 1
            while second < last:
                total = sort[i] + sort[second] + sort[last]
                if total > 0:
                    last -= 1
                elif total < 0:
                    second += 1
                else:
                    solution.append([sort[i], sort[second], sort[last]])
                    second += 1
                    
                    while second < last and sort[second] == sort[second - 1]:
                        second += 1

        return solution