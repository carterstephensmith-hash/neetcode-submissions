class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0
        s = 0
        e = len(range(n)) - 1
        c_max = 0
        f_max = 0
        
        
        while s < e:
            
            if height[s] > c_max:
                c_max = height[s]
            if height[e] > f_max:
                f_max = height[e]
            
            if height[s] > height[e]:
                
                total += f_max - height[e]
                e -=1
            else:
                
                total += c_max - height[s]
                s+=1


        return total