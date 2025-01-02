import itertools as it

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        nums = {
            '2':['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        combinations = it.product((nums[letter] for letter in sorted(nums)))
        return list(combinations)

sol = Solution()
print(sol.letterCombinations('23'))

