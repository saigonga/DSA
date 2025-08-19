class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l1=Counter(s)          
        l2=Counter(t)

        return l1 == l2       