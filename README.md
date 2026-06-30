# Snake, Water, Gun — CLI Game (Python)

A command-line implementation of the classic three-way hand game (a Rock-Paper-Scissors variant), played against a computer opponent that picks randomly. The repo contains four iterations of the same program, written while working through conditional logic, dictionaries, and bug fixing.

## Rules

| Choice | Beats | Loses to |
|---|---|---|
| Water (`w`) | Gun | Snake |
| Gun (`g`) | Snake | Water |
| Snake (`s`) | Water | Gun |

Internally, choices are encoded as integers: `-1 = water`, `0 = gun`, `1 = snake`.

## How to Run

```bash
python main.py
```

You'll be prompted to enter your choice as a single letter — `s` for snake, `g` for gun, or `w` for water. The computer picks randomly, and the result is printed.

## Project Structure

```
main.py               # Original implementation (if-elif chain)
modification-01.py    # Refactor of main.py using compound boolean conditions
modification_02.py    # Rewrite using a "what-beats-what" dictionary mapping
modifictaion_03.py    # Rewrite using arithmetic difference logic + input validation
```

## Version Notes

**`main.py`** — Six explicit `if`/`elif` branches, one per winning/losing combination. Contains a logic bug: the branch for "computer plays snake, you play water" incorrectly prints `You win`, when by the stated rules snake beats water and the computer should win that round.

**`modification-01.py`** — Same case-by-case logic as `main.py`, collapsed into two compound `or` conditions instead of six separate branches. The bug from `main.py` is carried over unchanged, since the underlying case grouping wasn't re-derived, just reformatted.

**`modification_02.py`** — A different strategy entirely: builds a dictionary (`maindic`) mapping each choice to the choice it defeats (e.g. snake → water), then checks whether `maindic[your_choice] == computer_choice`. This derives the win condition directly from the rules rather than manually enumerating six cases, which is why the bug doesn't appear here.

**`modifictaion_03.py`** — Uses the numeric encoding directly: with values `-1, 0, 1`, the win/loss outcome reduces to checking whether `you - computer` equals `-1` or `2` (win) versus `1` or `-2` (loss). Also the only version with input validation — an invalid choice exits cleanly with a message instead of throwing a `KeyError`.

## Concepts Practiced

- Dictionaries for bidirectional lookups (choice → label, label → choice)
- Translating a real-world rule set into multiple different logical/arithmetic representations of the same problem
- Spotting and tracing a bug across refactors (it survived one rewrite, was fixed in two others)
- Basic input validation and graceful exit handling

## Possible Next Steps

- Consolidate into a single `main.py` using the dictionary-mapping approach from `modification_02.py` (clearest and most rule-faithful), plus the input validation from `modification_03.py`
- Add a loop for best-of-N rounds with a running scoreboard
- Add unit tests covering all nine `(you, computer)` combinations to catch regressions like the one above automatically

## Author

Shabd Gupta
