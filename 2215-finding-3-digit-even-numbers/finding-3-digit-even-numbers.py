class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result =set()

        for comb in permutations(digits,3):
            num =comb[0]*100 + comb[1]*10+comb[2]
            if num % 2== 0 and comb[0] != 0:
                result.add(num)
        return sorted(result)

        

