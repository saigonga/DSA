class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l,r= len(haystack),len(needle)

        for i in range(l-r +1):
            if haystack[i:i+r] == needle:
                return i
        return -1
        

