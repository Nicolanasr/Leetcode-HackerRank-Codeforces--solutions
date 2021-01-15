class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        try:
            min_str = min(strs, key=len)
            poss = min_str[0]
        except:
            return ""
        
        c = 1
        b = 0
        while b != 1 and c <= len(min_str):
            for word in strs:
                if not word.startswith(poss):
                    b=1
                    poss = min_str[:c-1]
                    break
            if b != 1:
                c += 1
                poss = (min_str[:c])
        return poss
