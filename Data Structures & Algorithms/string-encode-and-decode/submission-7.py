class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs)):
            result += str(len(strs[i]))
            result += '#'
            result += strs[i]
        return result
    def decode(self, s: str) -> List[str]:
        #print(s)
        strs = []
        i = 0
        while i < len(s):
            #print(s[i])
            j = s.find('#',i)
            print(j)
            length = int(s[i:j])
            #print(length)
            strs.append(s[j+1:j+length+1])
            i += j-i + length + 1
            print(i)
            #print(strs)
        return strs
            #length
            # for j in range(len(s)):
            #     j

            #         lenstr = s[i]
            # lenstr = s[i]






        # groups = {}
        # for i in nums:
        #     groups[i] = groups.get(i,0) + 1
        # groups2 = sorted(groups, key=groups.get, reverse=True)
        # final = groups2[:k]
        # return final