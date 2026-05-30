"""
Board class for the Tic Tac Toe game.
"""

from typing import Optional
from .exceptions import CellTakenError

WINNING_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]


class Board:
    """Represents a 3x3 Tic Tac Toe board.

    Internally stored as a flat list of 9 cells, each either ' ', 'X', or 'O'.
    """

    def __init__(self) -> None:
        """Initialise an empty board."""
        self._cells = [" "] * 9

    def place(self, index: int, mark: str) -> None:
        """Place *mark* at *index* (0-8).

        Args:
            index: Board position in the range [0, 8].
            mark:  The player's mark ('X' or 'O').

        Raises:
            CellTakenError: If the cell at *index* is already occupied.
        """
        if self._cells[index] != " ":
            raise CellTakenError(
                f"Cell {index} is already taken by '{self._cells[index]}'."
            )
        self._cells[index] = mark

    def check_winner(self) -> Optional[str]:
        """Return the winning mark ('X' or 'O'), or None if there is no winner yet."""
        for a, b, c in WINNING_COMBOS:
            if (
                self._cells[a] != " "
                and self._cells[a] == self._cells[b] == self._cells[c]
            ):
                return self._cells[a]
        return None

    def is_full(self) -> bool:
        """Return True when all nine cells are occupied."""
        return " " not in self._cells

    def reset(self) -> None:
        """Clear the board back to its initial empty state."""
        self._cells = [" "] * 9

    def display(self) -> None:
        """Print the current board state to stdout."""
        c = self._cells
        separator = "---|---|---"
        print(f" {c[0]} | {c[1]} | {c[2]} ")
        print(separator)
        print(f" {c[3]} | {c[4]} | {c[5]} ")
        print(separator)
        print(f" {c[6]} | {c[7]} | {c[8]} ")
