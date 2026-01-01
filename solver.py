class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
        self.steps = 0

    def solve(self):
        empty = self.grid.find_empty()
        if not empty:
            return True

        row, col = empty
        for num in range(1, 10):
            if self.grid.is_valid(row, col, num):
                self.grid.grid[row][col] = num
                self.steps += 1

                if self.solve():
                    return True

                self.grid.grid[row][col] = 0

        return False
