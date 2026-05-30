# Tic Tac Toe 🎮

A production-ready Tic Tac Toe package implemented in Python 3.9+ using only the standard library.

## Run the game

```bash
python cli.py
```

With custom player names:

```bash
python cli.py --player1 Alice --player2 Bob
```

## Run tests

```bash
python -m pytest tests/
```

## Project structure

```text
tik-tac-toe-coad/
├── cli.py
├── requirements.txt
├── tictactoe.py
├── tic_tac_toe.ipynb
├── tictactoe/
│   ├── __init__.py
│   ├── board.py
│   ├── exceptions.py
│   ├── game.py
│   └── players.py
└── tests/
    ├── __init__.py
    ├── test_board.py
    └── test_game.py
```

Legacy files `tictactoe.py` and `tic_tac_toe.ipynb` remain in place for reference.
