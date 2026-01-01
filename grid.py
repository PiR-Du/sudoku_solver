class SudokuGrid:
    def __init__(self, grid):
        self.grid = grid

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def is_valid(self, row, col, num):
        if num in self.grid[row]:
            return False

        for i in range(9):
            if self.grid[i][col] == num:
                return False

        box_x = (col // 3) * 3
        box_y = (row // 3) * 3
        for i in range(box_y, box_y + 3):
            for j in range(box_x, box_x + 3):
                if self.grid[i][j] == num:
                    return False

        return True
