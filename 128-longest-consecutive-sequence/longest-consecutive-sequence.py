class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=sorted(set(nums))
        max_count=1
        count=1
        if not n: return 0
        for i in range(1, len(n)):
            if n[i] == n[i-1]+1:
                count+=1
            else:
                count= 1
            max_count =max(max_count,count)
        return max_count 