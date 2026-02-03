class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n=len(nums)
        if n < 3:
            return False

        i=0
        while i+1< n and nums[i] < nums[i+1]:
            i+=1
        if i == 0 or i == n - 1: return False
        p=i
        while p+1 < n and  nums[p] > nums[p+1]:
            p+=1
        if p == i or p == n-1: return False
        q=p
        while q+1 < n and nums[q] < nums[q+1]:
            q+=1
        return q == n - 1
                
        
            
