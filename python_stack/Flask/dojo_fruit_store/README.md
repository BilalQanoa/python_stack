# Dojo Fruit Store 🍎🍓

A clean and functional web application built with **Flask** that simulates an online fruit store for Dojo students. This project allows users to select fruit quantities, provide student information, and receive a detailed order receipt.

## 🚀 Features
* **Fruit Catalog:** A visual gallery showcasing available fruits.
* **Ordering System:** A user-friendly form to select fruit quantities and input customer details.
* **Real-time Processing:** Automatically calculates the total number of items ordered.
* **Dynamic Receipt:** A checkout page that displays the order details along with a precise timestamp.
* **Responsive Design:** Styled with **Bootstrap 4** for a professional look across all devices.

## 🛠️ Tech Stack
* **Back-end:** Python & Flask
* **Templating:** Jinja2
* **Front-end:** HTML5, CSS3, & Bootstrap 4

## 📂 Project Structure
```text
Dojo_Fruit_Store/
├── static/
│   ├── css/
│   │   └── bootstrap.css
│   └── img/
│       ├── apple.png
│       ├── blackberry.png
│       ├── raspberry.png
│       └── strawberry.png
├── templates/
│   ├── index.html       # Main store page
│   ├── fruits.html      # Image gallery page
│   └── checkout.html    # Order confirmation page
├── server.py            # Main Flask application
└── README.md