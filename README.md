# Pokesim

A small command-line Pokemon simulator that fetches Pokemon and move data from the PokeAPI.

This branch (fixes-improvements) contains bugfixes and improvements:
- Fixed missing imports and undefined names.
- Exposed Pokemon stats (HP/attack/defense) and used them in damage calculation.
- Added a cache directory (cache/) for API responses to avoid polluting repo root.
- Improved Trainer and Pokemon classes (robust HP/stat lookup, proper __str__, bag attribute).
- Safer caching of API responses (uses 'wb' for pickle writes).
- Improved game loop: input validation, clearer error messages, safer move handling, a usable potion item.

```markdown
Requirements
- Python 3.8+
- Install dependencies:
  pip install -r requirements.txt
```

How to run
```markdown
python game.py
```
- The prompts are in German; start by entering your name and a starter Pokemon name (e.g. "pikachu").

Notes & Next steps
- Damage calculation is still simplified. Consider refining with accuracy/effectiveness and other mechanics.
- Cache files are saved in the cache/ directory.
- Add unit tests and a CI workflow for easier development.
