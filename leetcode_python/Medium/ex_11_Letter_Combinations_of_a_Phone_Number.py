import itertools as it

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Mapping of digits to corresponding letters
        nums = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        # Return empty list if input is empty
        if not digits:
            return []

        # Generate combinations based on the input digits
        combinations = it.product(*(nums[digit] for digit in digits))

        # Convert tuples to strings and return as a list
        return [''.join(combination) for combination in combinations]

# Example usage:
sol = Solution()
print(sol.letterCombinations("23"))  # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print(sol.letterCombinations(""))    # Output: []
print(sol.letterCombinations("2"))   # Output: ['a', 'b', 'c']
