"""Unit tests for the Board class."""

import unittest

from tictactoe.board import Board
from tictactoe.exceptions import CellTakenError


class TestBoard(unittest.TestCase):
    """Tests for board placement, winner checks, and draw behavior."""

    def test_check_winner_all_combinations_for_x_and_o(self) -> None:
        """Winner detection should work for all 8 winning lines and both marks."""
        win_lines = [
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
            ((0, 0), (1, 1), (2, 2)),
            ((0, 2), (1, 1), (2, 0)),
        ]

        for mark in ("X", "O"):
            for line in win_lines:
                board = Board()
                for row, col in line:
                    board.place(row, col, mark)
                self.assertEqual(board.check_winner(), mark)

    def test_draw_detection(self) -> None:
        """A full board with no winner should be identified as draw state."""
        board = Board()
        moves = [
            (0, 0, "X"), (0, 1, "O"), (0, 2, "X"),
            (1, 0, "X"), (1, 1, "O"), (1, 2, "O"),
            (2, 0, "O"), (2, 1, "X"), (2, 2, "X"),
        ]
        for row, col, mark in moves:
            board.place(row, col, mark)

        self.assertTrue(board.is_full())
        self.assertIsNone(board.check_winner())

    def test_place_raises_when_cell_taken(self) -> None:
        """Placing on an occupied cell should raise CellTakenError."""
        board = Board()
        board.place(0, 0, "X")

        with self.assertRaises(CellTakenError):
            board.place(0, 0, "O")


if __name__ == "__main__":
    unittest.main()
