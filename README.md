# Tic Tac Toe

A clean, production-ready command-line Tic Tac Toe game written in pure Python (stdlib only).

## Features

- Full input validation (non-numeric, out-of-range, already-taken cell)
- Draw detection
- Play-again loop
- Structured as an importable Python package
- Custom exceptions (`InvalidMoveError`, `CellTakenError`)
- Type hints and docstrings throughout
- Unit tests for all critical paths
- `argparse` CLI with optional player names and log-level control

## Requirements

- Python 3.9+
- `pytest` (for running tests only)

## How to Run

### Default player names
```bash
python cli.py
```

### Custom player names
```bash
python cli.py --player1 Alice --player2 Bob
```

### With verbose logging
```bash
python cli.py --log-level INFO
```

## How to Run Tests

```bash
pip install pytest
python -m pytest tests/ -v
```

## Project Structure

```
tik-tac-toe-coad/
├── tictactoe/
│   ├── __init__.py       # Package exports: Game, Player, GameState
│   ├── board.py          # Board class - grid, win/draw detection
│   ├── game.py           # Game class - main loop, input handling
│   ├── players.py        # Player dataclass
│   └── exceptions.py     # TicTacToeError, InvalidMoveError, CellTakenError
├── tests/
│   ├── __init__.py
│   ├── test_board.py     # Board unit tests
│   └── test_game.py      # Game unit tests
├── cli.py                # CLI entry point
├── requirements.txt
├── README.md
├── tictactoe.py          # Original script (kept for reference)
└── tic_tac_toe.ipynb     # Original notebook (kept for reference)
```

## Board Layout

```
 0 | 1 | 2
---|---|---
 3 | 4 | 5
---|---|---
 6 | 7 | 8
```

Enter the number of the cell you want to occupy when prompted.

## Example Session

```
Welcome to Tic Tac Toe!
Positions are numbered 0-8:
 0 | 1 | 2
---|---|---
 3 | 4 | 5
---|---|---
 6 | 7 | 8

   |   |  
---|---|---
   |   |  
---|---|---
   |   |  
Alice (X) - enter position (0-8): 4

   |   |  
---|---|---
   | X |  
---|---|---
   |   |  
Bob (O) - enter position (0-8): 0
...
```
