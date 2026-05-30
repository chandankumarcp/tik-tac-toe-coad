"""
Unit tests for tictactoe.game.Game.
"""

import pytest

from tictactoe.exceptions import InvalidMoveError
from tictactoe.game import Game, GameState
from tictactoe.players import Player


@pytest.fixture()
def game() -> Game:
    return Game(Player("Alice", "X"), Player("Bob", "O"))


def test_switch_turn_x_to_o(game: Game) -> None:
    assert game._current_player is game.player1
    game.switch_turn()
    assert game._current_player is game.player2


def test_switch_turn_o_to_x(game: Game) -> None:
    game.switch_turn()
    game.switch_turn()
    assert game._current_player is game.player1


@pytest.mark.parametrize("bad_input", ["a", "", "!", "1.5", " "])
def test_parse_index_non_numeric_raises(bad_input: str) -> None:
    with pytest.raises(InvalidMoveError):
        Game._parse_index(bad_input)


@pytest.mark.parametrize("bad_input", ["9", "10", "100"])
def test_parse_index_out_of_range_raises(bad_input: str) -> None:
    with pytest.raises(InvalidMoveError):
        Game._parse_index(bad_input)


@pytest.mark.parametrize("good_input,expected", [("0", 0), ("4", 4), ("8", 8)])
def test_parse_index_valid(good_input: str, expected: int) -> None:
    assert Game._parse_index(good_input) == expected


def test_initial_state(game: Game) -> None:
    assert game.state == GameState.IN_PROGRESS
    assert game._current_player is game.player1
