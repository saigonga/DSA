class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [nums[i+j] for i in range(n) for j in (0, n)]
        return res