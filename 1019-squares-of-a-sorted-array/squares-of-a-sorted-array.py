class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # left=0
        # right=len(nums)-1
        result=[]

        for i, n in enumerate(nums):
            num = n ** 2
            result.append(num)
        result.sort()
        return result