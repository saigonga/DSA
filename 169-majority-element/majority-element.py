class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=None
        count=0

        for x in nums:
            if count == 0:
                candidate = x
            if x == candidate:
                count+=1
            else:
                count-=1
        return candidate
    