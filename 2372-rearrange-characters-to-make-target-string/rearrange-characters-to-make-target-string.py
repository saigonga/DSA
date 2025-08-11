class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_count=Counter(s)
        t_count=Counter(target)

        return min(s_count[ch] // t_count[ch] for ch in t_count)
        