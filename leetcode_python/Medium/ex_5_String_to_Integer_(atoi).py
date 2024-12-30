import re

class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Use regex to handle whitespace, sign, and digits
        match = re.match(r'^[ \t]*([+-]?\d+)', s)

        if not match:
            return 0

        # Extract the number from the matched group
        num_str = match.group(1)

        # Convert to integer
        result = int(num_str)

        # Step 2: Clamp the result within 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result


solution = Solution()
print(solution.myAtoi("   -42"))  # Output: -42