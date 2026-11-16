class Solution:
    def maxArea(self, heights: List[int]) -> int:

        nums = len(heights)
        first = 0
        last = nums - 1
        solution = 0
        
        while first < last:
            total = min(heights[first],heights[last]) * (last-first)
            if  total > solution:
                solution = total
                if heights[first] > heights[last]:
                    last -=1
                elif heights[first] < heights[last]:
                    first +=1
            elif heights[first] > heights[last]:
                last -=1
            else:
                first +=1
        return solution