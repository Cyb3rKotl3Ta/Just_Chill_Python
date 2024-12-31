class Solution:
    def intToRoman(self, num: int) -> str:
        # List of Roman numeral symbols and their corresponding values
        value_to_symbol = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        # Initialize the result
        roman_numeral = ""

        # Iterate over the value-symbol pairs
        for value, symbol in value_to_symbol:
            # While the current value can be subtracted from num
            while num >= value:
                roman_numeral += symbol  # Append the symbol
                num -= value  # Subtract the value from num

        return roman_numeral
