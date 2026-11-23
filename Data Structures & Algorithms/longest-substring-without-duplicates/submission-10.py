class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}     # char → most recent index
        first = 0
        largest = 0

        for second in range(len(s)):
            c = s[second]
            if c in last_seen and last_seen[c] >= first:
                first = last_seen[c] + 1     # jump past the previous copy
            last_seen[c] = second
            largest = max(largest, second - first + 1)

        return largest