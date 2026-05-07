# 🥷 Ninja Gold Game

An interactive web-based guessing game built with the **Flask** framework. Play as a ninja visiting different locations to accumulate gold, track your adventure history, and try your luck at the casino!

## 🎮 Game Features
- **Four Unique Locations:**
  - **Farm:** Earns 10-20 gold.
  - **Cave:** Earns 5-10 gold.
  - **House:** Earns 2-5 gold.
  - **Casino:** Earn or lose up to 50 gold!
- **Real-time Activity Log:** A color-coded history of all your moves, showing gains in green and losses in red.
- **Descending Order:** The most recent activities always appear at the top of the log.
- **State Management:** Uses **Flask Sessions** to persist your total gold and activity history during your visit.
- **Game Reset:** A dedicated button to clear your session and start your ninja journey from scratch.

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML5, Jinja2, Bootstrap 4
- **Styling:** Custom CSS (External stylesheet)
- **State:** Flask Session

## 📂 Project Structure
```text
ninja_gold/
├── static/
│   └── css/
│       └── style.css      # Custom styles for the retro look
├── templates/
│   └── index.html         # Main game dashboard
├── server.py              # Flask server and core game logic
└── README.md              # Project documentation