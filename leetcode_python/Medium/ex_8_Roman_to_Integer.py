class Solution:
    def romanToInt(self, s: str) -> int:
        # Roman numeral to integer mapping
        roman_to_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Initialize the result
        total = 0

        # Iterate through the Roman numeral string
        for i in range(len(s)):
            # Get the value of the current symbol
            value = roman_to_value[s[i]]

            # If this is not the last symbol and the next symbol is larger, subtract current value
            if i < len(s) - 1 and value < roman_to_value[s[i + 1]]:
                total -= value
            else:
                total += value

        return total
