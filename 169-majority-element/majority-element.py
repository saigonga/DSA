class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority={}

        for x in nums:
            majority[x] = majority.get(x, 0) +1
            if majority[x] > len(nums) //2:
                return x