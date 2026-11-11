class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        strings = {}


        for i in  range(len(strs)):
            count = [0] * 26
            single = strs[i]
            

            for j in range(len(strs[i])):
                letter = ord(single[j])- ord('a')
                count[letter] += 1
            key = tuple(count)
            strings[key] = strings.get((key), []) + [strs[i]]

        return list(strings.values())
            