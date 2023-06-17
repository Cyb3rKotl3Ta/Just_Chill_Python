class Sudoku(object):
    def __init__(self, data):
        self.board = data
        self.size = len(data)
        self.subgrid_size = int(self.size ** 0.5)

    def is_valid(self):
        if not self.is_valid_size():
            return False

        if not self.is_valid_values():
            return False

        if not self.is_valid_rows():
            return False

        if not self.is_valid_columns():
            return False

        if not self.is_valid_subgrids():
            return False

        return True

    def is_valid_size(self):
        for row in self.board:
            if len(row) != self.size:
                return False
        return len(self.board) == self.size

    def is_valid_values(self):
        for row in self.board:
            for num in row:
                if num < 1 or num > self.size:
                    return False
        return True

    def is_valid_rows(self):
        for row in self.board:
            if not self.is_valid_set(row):
                return False
        return True

    def is_valid_columns(self):
        for col in range(self.size):
            column = [self.board[row][col] for row in range(self.size)]
            if not self.is_valid_set(column):
                return False
        return True

    def is_valid_subgrids(self):
        for i in range(self.subgrid_size):
            for j in range(self.subgrid_size):
                subgrid = [
                    self.board[row][col]
                    for row in range(i * self.subgrid_size, (i + 1) * self.subgrid_size)
                    for col in range(j * self.subgrid_size, (j + 1) * self.subgrid_size)
                ]
                if not self.is_valid_set(subgrid):
                    return False
        return True

    @staticmethod
    def is_valid_set(nums):
        seen = set()
        for num in nums:
            if num != 0 and num in seen:
                return False
            seen.add(num)
        return True
 


goodSudoku1 = Sudoku([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

goodSudoku2 = Sudoku([
  [1,4, 2,3],
  [3,2, 4,1],

  [4,1, 3,2],
  [2,3, 1,4]
])


valid1 = goodSudoku1.is_valid()
valid2 = goodSudoku2.is_valid()
print(valid2)  # Output: True