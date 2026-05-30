"""
Player dataclass for the Tic Tac Toe game.
"""

from dataclasses import dataclass


@dataclass
class Player:
    """Represents a Tic Tac Toe player.

    Attributes:
        name: Display name of the player.
        mark: The mark used on the board, either 'X' or 'O'.
    """

    name: str
    mark: str

    def __post_init__(self) -> None:
        """Validate that mark is either 'X' or 'O'."""
        if self.mark not in ("X", "O"):
            raise ValueError(f"Player mark must be 'X' or 'O', got '{self.mark}'.")
