class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l= Counter(ransomNote)
        r=Counter(magazine)

        for ch in ransomNote:
            if l[ch] > r[ch]:
                return False
        return True