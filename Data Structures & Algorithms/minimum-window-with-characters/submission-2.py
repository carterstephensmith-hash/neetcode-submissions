class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        window = {}
        has = 0
        second = 0
        first = 0
        answer = ""
        for i in range(len(t)):
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        need = len(count_t)
        for second in range(len(s)):
            window[s[second]] = window.get(s[second], 0) + 1
            if s[second]  in count_t and window[s[second]] == count_t[s[second]]:   
                has +=1
            while has == need:
                if second - first < len(answer) or len(answer) == 0: 
                    answer = s[first:second +1]
                
                window[s[first]] -= 1
                if s[first] in count_t and window[s[first]]<count_t[s[first]]:
                    has -=1


                first +=1
        return answer



