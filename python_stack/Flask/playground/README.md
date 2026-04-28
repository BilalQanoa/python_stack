# Flask Playground - Dynamic Boxes 🎨

This project is a fun exercise to master **Jinja2 Templates** in Flask. Instead of just returning text, the server now generates dynamic HTML elements (colorful boxes) based on the URL parameters.

---

### 💡 What does this app do?
I built three levels of routing to control the playground:

1. **Level 1 (`/play`):** The default view that renders **3 beautiful blue boxes**.
2. **Level 2 (`/play/<x>`):** Now it's dynamic! You tell the server how many boxes you want (e.g., `/play/10`), and it renders exactly that number using a `for loop` inside the template.
3. **Level 3 (`/play/<x>/<color>`):** Complete control. You choose the **number** and the **color** (e.g., `/play/5/green`), and the server updates the CSS on the fly.

---

### 🛠️ What I practiced:
* **Passing Data:** Sending variables from Python routes to HTML templates.
* **Jinja2 Loops:** Using `{% for ... %}` to repeat elements without writing repetitive HTML code.
* **Dynamic Styling:** Using variables inside the HTML `style` attribute to change colors dynamically.
* **Internal CSS:** Keeping the design clean and contained within the template.

---

### 🧠 The "Ninja" Approach
I managed to use **only one HTML template** for all three levels. By using default values in Python and smart logic in Jinja2, the code stays "DRY" (Don't Repeat Yourself).

---

### 🏃‍♂️ How to test it:
1. Run the server:
   ```bash
   python server.py