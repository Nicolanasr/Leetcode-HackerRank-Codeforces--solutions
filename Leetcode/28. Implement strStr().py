class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)

        if needle == "":
            return 0

        for i in range(len(haystack)):
            if needle in haystack[i:i+l]:
                return i
                break
        return -1
