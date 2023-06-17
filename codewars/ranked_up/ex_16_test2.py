def count_sequences(matrix):
    count_4 = count_3 = count_2 = count_1 = 0
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    # Horizontal sequences
    for row in range(num_rows):
        for col in range(num_columns - 3):
            if (
                matrix[row][col] == matrix[row][col + 1] == matrix[row][col + 2] == matrix[row][col + 3]
                and matrix[row][col] != 0
            ):
                if matrix[row][col] == 1:
                    count_4 += 1
                else:
                    count_4 -= 1

    # Vertical sequences
    for col in range(num_columns):
        for row in range(num_rows - 3):
            if (
                matrix[row][col] == matrix[row + 1][col] == matrix[row + 2][col] == matrix[row + 3][col]
                and matrix[row][col] != 0
            ):
                if matrix[row][col] == 1:
                    count_4 += 1
                else:
                    count_4 -= 1

    return count_4, count_3, count_2, count_1


battleField = [     
            [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print(count_sequences(battleField))