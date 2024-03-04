# Question: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        data = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits):
            result = ['']
            for c in digits:
                result = [x+y for x in result for y in data[c]]
        else:
            result = []
        return result

print(Solution.letterCombinations(None, '234'))