# Flag Duel

A two-player mine-hunt game in the style of MSN Minesweeper Flags.

- 16×16 field, 51 hidden mines. Players take turns uncovering squares.
- **Uncover a mine → you claim it and go again.** Uncover a number or blank → the turn passes.
- First to **26 mines** wins.
- Each player has **one bomb** (opens a 5×5 area) that can only be used while behind.
- Play vs CPU (Easy / Normal / Hard) or 2 players on one screen.

## Play
- **Browser:** https://thegooseygoose.github.io/flag-duel/ (or open `index.html`).
- **Windows:** download `Flag Duel.exe` from [Releases](https://github.com/thegooseygoose/flag-duel/releases/latest).

## Build the exe
```
pip install pywebview pyinstaller
pyinstaller "Flag Duel.spec"
```
Output: `dist/Flag Duel.exe`.
