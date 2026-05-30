"""Board model and operations for Tic Tac Toe."""

from typing import Optional

from tictactoe.exceptions import CellTakenError


class Board:
    """Represents a 3x3 Tic Tac Toe board."""

    def __init__(self) -> None:
        """Initialize an empty board."""
        self.grid: list[list[str]] = [[" " for _ in range(3)] for _ in range(3)]

    def place(self, row: int, col: int, mark: str) -> None:
        """Place a player's mark at the given row and column.

        Raises:
            CellTakenError: If the target cell is already occupied.
        """
        if self.grid[row][col] != " ":
            raise CellTakenError(f"Cell ({row}, {col}) is already taken.")
        self.grid[row][col] = mark

    def check_winner(self) -> Optional[str]:
        """Return the winning mark ('X' or 'O') if present, otherwise None."""
        lines = []
        lines.extend(self.grid)
        lines.extend([[self.grid[r][c] for r in range(3)] for c in range(3)])
        lines.append([self.grid[i][i] for i in range(3)])
        lines.append([self.grid[i][2 - i] for i in range(3)])

        for line in lines:
            if line[0] != " " and line[0] == line[1] == line[2]:
                return line[0]
        return None

    def is_full(self) -> bool:
        """Return True when no empty cells remain."""
        return all(cell != " " for row in self.grid for cell in row)

    def display(self) -> None:
        """Pretty-print the board."""
        for row_index, row in enumerate(self.grid):
            print(" | ".join(row))
            if row_index < 2:
                print("--+---+--")

    def reset(self) -> None:
        """Clear the board to an empty state."""
        self.grid = [[" " for _ in range(3)] for _ in range(3)]
