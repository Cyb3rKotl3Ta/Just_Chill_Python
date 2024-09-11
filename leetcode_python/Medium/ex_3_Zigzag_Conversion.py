def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    # Initialize a list of empty strings for each row
    rows = [''] * numRows
    current_row = 0
    direction = -1  # Start moving 'up' to start the zigzag pattern

    for char in s:
        rows[current_row] += char

        # Change direction if we are at the top or bottom row
        if current_row == 0 or current_row == numRows - 1:
            direction *= -1

        # Move to the next row in the current direction
        current_row += direction

    # Concatenate all rows to form the final string
    return ''.join(rows)

# Example usage
print(convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(convert("A", 1))               # Output: "A"
