"""Custom exception hierarchy for the Tic Tac Toe package."""


class TicTacToeError(Exception):
    """Base exception for all Tic Tac Toe errors."""


class InvalidMoveError(TicTacToeError):
    """Raised when a move input is invalid or out of range."""


class CellTakenError(TicTacToeError):
    """Raised when trying to place a mark in an occupied cell."""
