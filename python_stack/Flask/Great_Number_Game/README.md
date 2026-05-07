# Great Number Game 🎮🔢

An interactive web-based guessing game built with **Python** and the **Flask** framework. The server "thinks" of a random number between 1 and 100, and the player has 5 attempts to guess it correctly.

## 🚀 Features
* **Random Number Generation:** Uses Python's `random` module to generate a new target number for each game.
* **Session Management:** Tracks game state, user attempts, and guessing history using Flask Sessions.
* **Persistence:** A **JSON-based Leaderboard** that saves winners' names and their attempt counts permanently.
* **Dynamic UI:** Responsive design using **Bootstrap 5**, featuring color-coded feedback (Red for wrong, Green for win, Black for loss).
* **Logic Handling:** Smart win/loss conditions that prioritize a correct guess even on the final attempt.

## 🛠️ Tech Stack
* **Back-end:** Python, Flask
* **Storage:** JSON (for Leaderboard), Flask Session (for Game State)
* **Front-end:** HTML5, CSS3, Bootstrap 5, Jinja2 Templates

## 📂 Project Structure
```text
great_number_game/
├── templates/
│   ├── index.html       # Main game interface
│   └── leaderboard.html # High scores display
├── leaderboard.json     # Persistent storage for winners
├── server.py            # Main Flask application logic
└── README.md