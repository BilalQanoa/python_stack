# Flask Checkerboard - Logic & Layout 🏁

This project is a deep dive into **Nested Loops** and **Conditional Rendering** within Flask templates. The goal was to build a dynamic checkerboard that scales based on URL parameters while maintaining a clean project structure with static files.

---

### 💡 Features & Levels
I implemented a flexible routing system that handles everything from a standard board to a fully customized one:

1.  **Default Board (`/`):** Renders the classic **8x8** checkerboard.
2.  **Variable Rows (`/<x>`):** Allows the user to set the number of rows while keeping 8 columns.
3.  **Full Dimensions (`/<x>/<y>`):** Complete control over the grid size (e.g., `/10/10` for a 100-box grid).


---

### 🛠️ Technical Skills Applied
* **Nested For Loops:** Using loops within loops in Jinja2 to generate rows and columns dynamically.
* **Checkerboard Logic:** Applied the `(i + j) % 2 == 0` mathematical logic to toggle background colors across the grid.
* **Static File Linking:** Organized the project by separating CSS into a `static` folder and linking it using `url_for`.
* **Route Parameters:** Handling multiple variable rules and converting string inputs to integers for range functions.

---

### 📁 Project Structure
```text
/checkerboard_project
    ├── server.py
    ├── static/
    │    └── css/
    │         └── style.css
    └── templates/
         └── index.html