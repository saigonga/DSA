class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # max_len = 0
        # start = 0
        # used = {}
        # for i, char in enumerate(s):
        #     if char in used and used[char] >= start:
        #         start = used[char] + 1
        #     max_len = max(max_len, i - start + 1)
        #     used[char] = i
        # return max_len


        l=0
        sett=set()
        longest =0
        n=len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l +=1
            w=(r-l) +1
            longest = max(longest,w)
            sett.add(s[r])
        return longest
