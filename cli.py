"""Command-line entry point for the Tic Tac Toe game.

Usage::

    python cli.py
    python cli.py --player1 Alice --player2 Bob
"""

import argparse
import logging

from tictactoe import Game, Player


def _parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Play a two-player Tic Tac Toe game in the terminal."
    )
    parser.add_argument(
        "--player1",
        default="Player 1",
        help="Name of the first player (uses mark X). Default: 'Player 1'.",
    )
    parser.add_argument(
        "--player2",
        default="Player 2",
        help="Name of the second player (uses mark O). Default: 'Player 2'.",
    )
    parser.add_argument(
        "--log-level",
        default="WARNING",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Set the logging verbosity. Default: WARNING.",
    )
    return parser.parse_args()


def main() -> None:
    """Initialise the game and start the main loop."""
    args = _parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(levelname)s | %(name)s | %(message)s",
    )

    player1 = Player(name=args.player1, mark="X")
    player2 = Player(name=args.player2, mark="O")
    game = Game(player1, player2)
    game.play()


if __name__ == "__main__":
    main()
