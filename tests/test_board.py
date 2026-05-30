"""
Unit tests for tictactoe.board.Board.
"""

import pytest

from tictactoe.board import Board
from tictactoe.exceptions import CellTakenError


def _place_all(board: Board, indices: list, mark: str) -> None:
    for i in indices:
        board.place(i, mark)


@pytest.mark.parametrize("combo", [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6],
])
def test_x_wins(combo: list) -> None:
    board = Board()
    _place_all(board, combo, "X")
    assert board.check_winner() == "X"


@pytest.mark.parametrize("combo", [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6],
])
def test_o_wins(combo: list) -> None:
    board = Board()
    _place_all(board, combo, "O")
    assert board.check_winner() == "O"


def test_no_winner_on_empty_board() -> None:
    board = Board()
    assert board.check_winner() is None


def test_draw() -> None:
    """
    X | O | X
    X | O | O
    O | X | X
    """
    board = Board()
    moves = [
        (0, "X"), (1, "O"), (2, "X"),
        (3, "X"), (4, "O"), (5, "O"),
        (6, "O"), (7, "X"), (8, "X"),
    ]
    for idx, mark in moves:
        board.place(idx, mark)
    assert board.check_winner() is None
    assert board.is_full()


def test_not_full_on_empty_board() -> None:
    board = Board()
    assert not board.is_full()


def test_cell_taken_raises() -> None:
    board = Board()
    board.place(4, "X")
    with pytest.raises(CellTakenError):
        board.place(4, "O")


def test_reset_clears_board() -> None:
    board = Board()
    board.place(0, "X")
    board.reset()
    assert board.check_winner() is None
    assert not board.is_full()
    board.place(0, "O")  # should not raise
