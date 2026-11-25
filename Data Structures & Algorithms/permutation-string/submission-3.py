class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first = 0
        anagram1 = {}
        anagram2 = {}
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            anagram1[s1[i]] = anagram1.get(s1[i], 0) + 1
        for second in range(len(s2)):
            anagram2[s2[second]] = anagram2.get(s2[second], 0) + 1
            while second - first + 1 > len(s1):
                
                anagram2[s2[first]] -= 1
                if anagram2[s2[first]] == 0:
                    del anagram2[s2[first]]
                first += 1

            if anagram1 == anagram2:
                return True
        return False
