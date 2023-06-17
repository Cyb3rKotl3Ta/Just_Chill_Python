def validate_battlefield(field):
    buttleships_count = [0, 0, 0, 0]
    true_buttleships_count = [4, 3, 2, 1]
    counts_row = 0
    num_rows = len(field)
    num_columns = len(field[0])
    counts = [0] * num_columns
    for col in range(num_columns):
        counts_col = 0
        counts_row = 0
        for row in range(num_rows):
            current_element = battleField[row][col]


            if field[row][col] == 1:
                counts_col += 1
                if counts_col > 4:
                    print(counts_col)
                    return False
            elif field[row][col] == 0:
                if counts_col == 1:
                    if row + 1 < num_rows and battleField[row + 1][col] == 1:
                        buttleships_count[counts_col-1] += 1
                    if row - 1 >= 0 and battleField[row - 1][col] == 1:
                        buttleships_count[counts_col-1] += 1
                counts_col = 0

            if field[col][row] == 1:
                counts_row += 1
                if counts_row > 4:
                    print(counts_row)
                    return False
            elif field[col][row] == 0:
                buttleships_count[counts_row-1] += 1
                counts_row = 0
        counts[col] = counts_col

    for buttleship in range(len(buttleships_count)):
        if buttleships_count[buttleship] != true_buttleships_count[buttleship]:
            return False



    # def count_buttleship():

    return True


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

print(validate_battlefield(battleField))
