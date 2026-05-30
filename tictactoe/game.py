"""
Game controller for Tic Tac Toe.
"""

import logging
from enum import Enum, auto
from typing import Optional

from .board import Board
from .exceptions import CellTakenError, InvalidMoveError
from .players import Player

logger = logging.getLogger(__name__)


class GameState(Enum):
    """Possible states of a Tic Tac Toe game."""

    IN_PROGRESS = auto()
    WIN = auto()
    DRAW = auto()


class Game:
    """Controls a full two-player Tic Tac Toe session.

    Args:
        player1: The player who uses mark 'X' and goes first.
        player2: The player who uses mark 'O'.
    """

    POSITION_HINT = (
        "Positions are numbered 0-8:\n"
        " 0 | 1 | 2 \n"
        "---|---|---\n"
        " 3 | 4 | 5 \n"
        "---|---|---\n"
        " 6 | 7 | 8 "
    )

    def __init__(self, player1: Player, player2: Player) -> None:
        """Initialise the game with two players."""
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self._current_player: Player = player1
        self.state: GameState = GameState.IN_PROGRESS

    def play(self) -> None:
        """Run the interactive game loop, including play-again handling."""
        print("\nWelcome to Tic Tac Toe!")
        print(self.POSITION_HINT)

        while True:
            self._run_round()
            if not self._ask_play_again():
                print("\nThanks for playing! Goodbye")
                break
            self._reset()

    def get_move(self, player: Player) -> int:
        """Prompt *player* for a valid board position and return it.

        Keeps re-prompting until a valid, unoccupied index in [0, 8] is entered.

        Returns:
            A validated board index in the range [0, 8].
        """
        while True:
            raw = input(f"{player.name} ({player.mark}) - enter position (0-8): ").strip()
            try:
                index = self._parse_index(raw)
            except InvalidMoveError as exc:
                print(f"  Invalid: {exc}  Please try again.")
                continue

            try:
                self.board.place(index, player.mark)
                # undo the peek
                self.board._cells[index] = " "
            except CellTakenError as exc:
                print(f"  {exc}  Please try again.")
                continue

            return index

    def switch_turn(self) -> None:
        """Toggle the current player."""
        self._current_player = (
            self.player2 if self._current_player is self.player1 else self.player1
        )

    def _run_round(self) -> None:
        """Play a single game until win or draw."""
        self.state = GameState.IN_PROGRESS

        while self.state == GameState.IN_PROGRESS:
            print()
            self.board.display()
            index = self.get_move(self._current_player)
            self.board.place(index, self._current_player.mark)
            logger.info(
                "%s placed '%s' at index %d.",
                self._current_player.name,
                self._current_player.mark,
                index,
            )

            winner_mark: Optional[str] = self.board.check_winner()
            if winner_mark:
                self.state = GameState.WIN
                print()
                self.board.display()
                winner = self._player_by_mark(winner_mark)
                print(f"\n{winner.name} ({winner.mark}) wins! Congratulations!")
                logger.info("Game over - %s won.", winner.name)
                return

            if self.board.is_full():
                self.state = GameState.DRAW
                print()
                self.board.display()
                print("\nIt's a draw! Well played by both players.")
                logger.info("Game over - draw.")
                return

            self.switch_turn()

    def _reset(self) -> None:
        """Reset board and turn for a fresh game."""
        self.board.reset()
        self._current_player = self.player1
        self.state = GameState.IN_PROGRESS
        logger.info("Board reset for a new game.")

    @staticmethod
    def _parse_index(raw: str) -> int:
        """Parse and validate a raw input string into a board index.

        Raises:
            InvalidMoveError: If the input is not a digit or out of range.
        """
        if not raw.isdigit():
            raise InvalidMoveError(f"'{raw}' is not a valid number.")
        index = int(raw)
        if index < 0 or index > 8:
            raise InvalidMoveError(
                f"{index} is out of range. Enter a number between 0 and 8."
            )
        return index

    def _player_by_mark(self, mark: str) -> Player:
        """Return the Player whose mark matches *mark*."""
        return self.player1 if self.player1.mark == mark else self.player2

    @staticmethod
    def _ask_play_again() -> bool:
        """Ask the players whether they want another round."""
        while True:
            answer = input("\nPlay again? (y/n): ").strip().lower()
            if answer in ("y", "yes"):
                return True
            if answer in ("n", "no"):
                return False
            print("  Please enter 'y' or 'n'.")
