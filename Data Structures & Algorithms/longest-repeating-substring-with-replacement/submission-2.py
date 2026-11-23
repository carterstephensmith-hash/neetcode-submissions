class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = dict()
        first = 0
        largest = 0

        for second in range(len(s)):
            count[s[second]] = 1 + count.get(s[second], 0)
            while second-first+1 - max(count.values()) > k:
                
                count[s[first]] = count.get(s[first], 0) -1
                first +=1
        
            largest = max(largest, second - first + 1)
                
        return largest