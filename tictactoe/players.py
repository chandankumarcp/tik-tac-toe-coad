"""Player models for Tic Tac Toe."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Player:
    """Represents a Tic Tac Toe player."""

    name: str
    mark: str

    def __post_init__(self) -> None:
        """Validate that the player mark is supported."""
        if self.mark not in {"X", "O"}:
            raise ValueError("Player mark must be 'X' or 'O'.")
