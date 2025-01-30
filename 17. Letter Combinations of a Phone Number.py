from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = { 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}        
        letter_groups = [ letters[int(i)] for i in digits ]
        result = [ ''.join(i) for i in product(*letter_groups) ]
        return result