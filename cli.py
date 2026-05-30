"""Command-line entry point for the Tic Tac Toe game."""

import argparse

from tictactoe import Game, Player


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for player names."""
    parser = argparse.ArgumentParser(description="Play Tic Tac Toe")
    parser.add_argument("--player1", default="Player 1", help="Name for player X")
    parser.add_argument("--player2", default="Player 2", help="Name for player O")
    return parser.parse_args()


def main() -> None:
    """Create and start a Tic Tac Toe game from CLI options."""
    args = parse_args()
    game = Game(Player(name=args.player1, mark="X"), Player(name=args.player2, mark="O"))
    game.play()


if __name__ == "__main__":
    main()
