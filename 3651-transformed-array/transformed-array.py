class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        for i in range(n):
            jump = nums[i]
            next_i = (i+jump)% n
            res.append(nums[next_i])
        return res