class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first = 0
        
        second = 0
        largest = 0
        window = set()
        n = []
        while second < len(s):
            if s[second] in window:
                window.remove(s[first])
                first += 1
            else:
                window.add(s[second])
                second += 1
                largest = max(largest, second - first)
                    
        return largest