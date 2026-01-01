import tkinter as tk
from grid import SudokuGrid
from solver import SudokuSolver

CELL_SIZE = 50
GRID_SIZE = CELL_SIZE * 9
BG_COLOR = "#f2f2f2"
LINE_COLOR = "#555555"
ACCENT = "#4a90e2"

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.configure(bg=BG_COLOR)

        self.canvas = tk.Canvas(
            root,
            width=GRID_SIZE,
            height=GRID_SIZE,
            bg=BG_COLOR,
            highlightthickness=0
        )
        self.canvas.pack(padx=20, pady=20)

        self.entries = [[None]*9 for _ in range(9)]

        self.draw_grid()
        self.create_entries()
        self.create_buttons()

    # 🎨 Dessin des lignes
    def draw_grid(self):
        for i in range(10):
            width = 3 if i % 3 == 0 else 1
            dash = () if i % 3 == 0 else (2, 4)

            # Vertical
            self.canvas.create_line(
                i * CELL_SIZE, 0,
                i * CELL_SIZE, GRID_SIZE,
                width=width,
                dash=dash,
                fill=LINE_COLOR
            )

            # Horizontal
            self.canvas.create_line(
                0, i * CELL_SIZE,
                GRID_SIZE, i * CELL_SIZE,
                width=width,
                dash=dash,
                fill=LINE_COLOR
            )

    # ✍️ Entries invisibles
    def create_entries(self):
        for i in range(9):
            for j in range(9):
                e = tk.Entry(
                    self.canvas,
                    font=("Segoe UI", 20),
                    justify="center",
                    bg=BG_COLOR,
                    fg="#333333",
                    relief="flat",
                    bd=0
                )

                self.canvas.create_window(
                    j * CELL_SIZE + CELL_SIZE // 2,
                    i * CELL_SIZE + CELL_SIZE // 2,
                    window=e,
                    width=CELL_SIZE - 10,
                    height=CELL_SIZE - 10
                )

                self.entries[i][j] = e

    def create_buttons(self):
        frame = tk.Frame(self.root, bg=BG_COLOR)
        frame.pack(pady=10)

        tk.Button(
            frame,
            text="Solve",
            font=("Segoe UI", 12),
            bg=ACCENT,
            fg="white",
            relief="flat",
            width=10,
            command=self.solve
        ).pack(side="left", padx=5)

        tk.Button(
            frame,
            text="Clear",
            font=("Segoe UI", 12),
            relief="flat",
            width=10,
            command=self.clear
        ).pack(side="left", padx=5)

    def read_grid(self):
        return [
            [int(e.get()) if e.get().isdigit() else 0 for e in row]
            for row in self.entries
        ]

    def write_grid(self, grid):
        for i in range(9):
            for j in range(9):
                e = self.entries[i][j]
                e.delete(0, tk.END)
                if grid[i][j] != 0:
                    e.insert(0, str(grid[i][j]))
                    e.config(fg=ACCENT)

    def clear(self):
        for row in self.entries:
            for e in row:
                e.delete(0, tk.END)
                e.config(fg="#333333")

    def solve(self):
        grid = SudokuGrid(self.read_grid())
        solver = SudokuSolver(grid)

        if solver.solve():
            self.write_grid(grid.grid)
