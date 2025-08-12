class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        l=0
        count=0

        while l < len(jewels):
            r=0
            while r < len(stones):
                if jewels[l] == stones[r]:
                    count +=1
                r+=1
            l+=1
        return count