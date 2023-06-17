def is_valid_battleship_field(field):
    ship_sizes = [1, 2, 3, 4]
    expected_counts = [4, 3, 2, 1]
    ship_counts = [0, 0, 0, 0]
    rows, cols = len(field), len(field[0])

    def is_valid_position(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        return True

    def is_adjacent_occupied(row, col):
        for dx in [-1, 1]:
            if (
                is_valid_position(row + dx, col) and field[row + dx][col] == 1 or
                is_valid_position(row, col + dx) and field[row][col + dx] == 1
            ):
                return True
        return False

    def dfs(row, col, size):
        if not is_valid_position(row, col) or field[row][col] != 1:
            return False
        field[row][col] = -1  # Mark cell as visited
        size -= 1
        if size == 0:
            return True
        return (
            dfs(row - 1, col, size) or
            dfs(row + 1, col, size) or
            dfs(row, col - 1, size) or
            dfs(row, col + 1, size)
        )

    for row in range(rows):
        for col in range(cols):
            if field[row][col] == 1:
                if is_adjacent_occupied(row, col):
                    return False  # Ships are touching diagonally

                for size in ship_sizes:
                    if dfs(row, col, size):
                        ship_counts[size - 1] += 1
                        break
                else:
                    return False  # Ship size is invalid

    return ship_counts == expected_counts


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

is_valid = is_valid_battleship_field(battleField)
print(is_valid)

