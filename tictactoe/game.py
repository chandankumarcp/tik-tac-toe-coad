"""Game loop and move validation for Tic Tac Toe."""

import logging
from enum import Enum
from typing import Tuple

from tictactoe.board import Board
from tictactoe.exceptions import CellTakenError, InvalidMoveError
from tictactoe.players import Player

logging.basicConfig(level=logging.INFO, format="%(message)s")


class GameState(Enum):
    """Represents the state of a Tic Tac Toe game."""

    IN_PROGRESS = "in_progress"
    WIN = "win"
    DRAW = "draw"


class Game:
    """Encapsulates Tic Tac Toe gameplay between two players."""

    def __init__(self, player1: Player, player2: Player) -> None:
        """Initialize the game state and set the first player."""
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.board = Board()

    def get_move(self, player: Player) -> Tuple[int, int]:
        """Read and validate a move from input.

        Supports either:
        - row,col format where row and col are in [0, 2]
        - single index format in [0, 8]

        Raises:
            InvalidMoveError: If input is malformed or out of range.
        """
        raw_move = input(f"{player.name} ({player.mark}), enter move (row,col or 0-8): ").strip()

        if "," in raw_move:
            parts = [part.strip() for part in raw_move.split(",")]
            if len(parts) != 2:
                raise InvalidMoveError("Move must contain exactly one comma.")
            try:
                row, col = int(parts[0]), int(parts[1])
            except ValueError as exc:
                raise InvalidMoveError("Row and column must be integers.") from exc
            if row not in range(3) or col not in range(3):
                raise InvalidMoveError("Row and column must be between 0 and 2.")
            return row, col

        try:
            index = int(raw_move)
        except ValueError as exc:
            raise InvalidMoveError("Move must be an integer or row,col.") from exc

        if index not in range(9):
            raise InvalidMoveError("Index must be between 0 and 8.")
        return divmod(index, 3)

    def switch_turn(self) -> None:
        """Switch to the other player's turn."""
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def play(self) -> None:
        """Run the main game loop until users choose to stop playing."""
        logging.info("Welcome to Tic Tac Toe")
        while True:
            state = GameState.IN_PROGRESS
            self.current_player = self.player1

            while state == GameState.IN_PROGRESS:
                self.board.display()
                try:
                    row, col = self.get_move(self.current_player)
                    self.board.place(row, col, self.current_player.mark)
                except (InvalidMoveError, CellTakenError) as error:
                    logging.info("Invalid move: %s", error)
                    continue

                winner = self.board.check_winner()
                if winner is not None:
                    state = GameState.WIN
                    self.board.display()
                    logging.info("%s wins!", self.current_player.name)
                    break

                if self.board.is_full():
                    state = GameState.DRAW
                    self.board.display()
                    logging.info("It's a draw!")
                    break

                self.switch_turn()

            play_again = input("Play again? (y/n): ").strip().lower()
            if play_again != "y":
                logging.info("Thanks for playing!")
                return

            self.board.reset()
            logging.info("Starting a new game...")
