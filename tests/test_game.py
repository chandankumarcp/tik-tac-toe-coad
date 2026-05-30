"""Unit tests for the Game class."""

import unittest
from unittest.mock import patch

from tictactoe.exceptions import InvalidMoveError
from tictactoe.game import Game
from tictactoe.players import Player


class TestGame(unittest.TestCase):
    """Tests for game turn handling and move validation."""

    def setUp(self) -> None:
        """Create a fresh game for each test."""
        self.player1 = Player(name="Alice", mark="X")
        self.player2 = Player(name="Bob", mark="O")
        self.game = Game(self.player1, self.player2)

    def test_switch_turn(self) -> None:
        """Switching turns should alternate between both players."""
        self.assertEqual(self.game.current_player, self.player1)
        self.game.switch_turn()
        self.assertEqual(self.game.current_player, self.player2)
        self.game.switch_turn()
        self.assertEqual(self.game.current_player, self.player1)

    @patch("builtins.input", return_value="bad")
    def test_get_move_raises_for_non_numeric_input(self, _: object) -> None:
        """Invalid non-numeric input should raise InvalidMoveError."""
        with self.assertRaises(InvalidMoveError):
            self.game.get_move(self.player1)

    @patch("builtins.input", return_value="9")
    def test_get_move_raises_for_out_of_range_index(self, _: object) -> None:
        """Out-of-range index input should raise InvalidMoveError."""
        with self.assertRaises(InvalidMoveError):
            self.game.get_move(self.player1)


if __name__ == "__main__":
    unittest.main()
