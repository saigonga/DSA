class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        
        for r in range(1,len(nums)):
            if l == 1 or nums[r] != nums[l-2]:
                nums[l] = nums[r]
                l+=1
        return l    