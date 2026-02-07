class Solution:
    def checkString(self, s: str) -> bool:
        l=0
        r=len(s)-1

        for x in s:
            if s[l] == 'a':
                l+=1
            elif s[r] == 'b':
                r-=1
        if l > r :
            return True
        return False
                
