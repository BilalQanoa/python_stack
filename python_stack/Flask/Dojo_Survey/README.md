# Champion Survey - Flask Application (Custom CSS)

## 📌 Project Overview
This is a web application built using the **Flask** framework. The project demonstrates the ability to create a server, handle multiple routes, and manage data flow using HTML forms. In this version, Bootstrap was replaced with **Custom CSS** stored in the `static` directory to demonstrate styling proficiency.

## 🚀 Features
* **Root Route (`/`)**: Serves a custom-styled HTML form.
* **Result Route (`/result`)**: Handles POST requests, processes form data, and renders a results page.
* **Custom Styling**: Uses external CSS files (`form.css`, `result.css`) linked via Flask's `static` folder.
* **Ninja Bonus**: Integrated **Radio Buttons** for selecting experience levels.
* **Sensei Bonus**: Integrated **Checkboxes** for selecting multiple favorite languages.
* **Debugging**: Logs `request.form` data to the server terminal for verification.

## 🛠️ Tech Stack
* **Backend**: Python (Flask)
* **Frontend**: HTML5, Jinja2 Templates
* **Styling**: Custom CSS (External stylesheets)

## 📁 Project Structure
```text
Dojo_Survey/
│
├── server.py           # Main Flask application
├── static/             # Directory for static assets
│   ├── form.css        # Styles for the survey form
│   └── result.css      # Styles for the results page
├── templates/          # Directory for HTML templates
│   ├── form.html       # Survey entry page
│   └── result.html     # Results display page
└── README.md           # Documentation