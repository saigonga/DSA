class Solution:
    def reverseString(self, s: List[str]) -> None:
        n=len(s)
        T=[]
        for i in range(n-1,-1,-1):
            T.append(s[i])
        for i in range(n):
            s[i]=T[i]
        
    
     
        
        