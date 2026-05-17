# 🎮 Survival Game (Console)

> Console survival game written in Python — no dependencies required.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![Language](https://img.shields.io/badge/Language-EN%20%7C%20UA-yellow)

---

## 📖 About

A text-based survival game where you explore dangerous territory, fight enemies, avoid traps, and collect treasure — all from your terminal. Features 5 distinct game modes, a real-time HP bar, and a persistent leaderboard saved to disk.

Built entirely with Python standard library — no pip installs needed.

---

## 🕹️ Game Modes

| Mode | Description |
|------|-------------|
| **Classic** | Survive a fixed number of turns |
| **Endless** | Play until HP reaches 0 |
| **Greedy** | Collect a target amount of coins before turns run out |
| **Hardcore** | Classic mode — but Rest is limited to 1 use per game |
| **Chaos** | Every turn triggers a random effect: Double Damage, Double Coins, Bonus Heal, or Nothing |

---

## ⚔️ Player Actions

- **Explore** — venture into unknown territory (enemy / trap / treasure)
- **Rest** — recover HP (limited in Hardcore mode)
- **Risk** — gamble for extra treasure (high reward, high danger)

---

## ✨ Features

- **Bilingual UI** — full English and Ukrainian language support
- **5 game modes** with unique win/lose conditions
- **Random event system** — enemies, traps, and treasures with weighted probability
- **Visual HP bar** — real-time health display in the console
- **Persistent leaderboard** — results saved to `scores.txt` across sessions
- **Input validation** — all user inputs are safely handled (no crashes on wrong input)
- **Configurable balance** — tweak game parameters directly in `main.py`

---

## 🚀 Getting Started

**Requirements:** Python 3.8+

```bash
# Clone the repository
git clone https://github.com/IvanShcherban-FS/SurvivalGame.git
cd SurvivalGame

# Run the game
python main.py
```

No external libraries needed — only Python's built-in `random` module is used.

---

## ⚙️ Configuration

At the top of `main.py` you can adjust game balance:

```python
start_hp      = 100   # Starting HP
max_turn      = 15    # Turns in Classic mode
enemy_dm      = 20    # Enemy damage
trap_dm       = 15    # Trap damage
heal_amount   = 25    # HP restored by Rest
coin          = 10    # Base coins per treasure
goal_coins    = 80    # Coin target in Greedy mode
greedy_turns  = 10    # Turn limit in Greedy mode
bar_len       = 20    # Length of the HP bar
```

---

## 🗂️ Project Structure

```
SurvivalGame/
├── main.py       # Game logic, modes, event system
├── scores.txt    # Auto-generated leaderboard (created on first run)
└── README.md
```

---

## 🛠️ Technical Highlights

- Multi-language support via dictionary-based string localization
- Game state management across 5 independent mode loops
- File I/O for persistent score tracking between sessions
- Defensive input handling throughout all menus and game screens
- Modular function structure separating UI, logic, and data layers

---

## 📄 License

MIT — free to use, modify, and distribute.
