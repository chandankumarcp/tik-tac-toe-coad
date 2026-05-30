"""
Custom exceptions for the Tic Tac Toe game.
"""


class TicTacToeError(Exception):
    """Base exception for all Tic Tac Toe errors."""


class InvalidMoveError(TicTacToeError):
    """Raised when the input is non-numeric or out of range (0-8)."""


class CellTakenError(TicTacToeError):
    """Raised when a player tries to place a mark on an already-occupied cell."""
