# 📚 Book Favorites Tracking System ERD

This database schema is designed to manage users and their collection of favorite books.

## 📊 Database Structure

### 1. Users Table
Stores basic information about the application users.
*   **Fields**: `id` (PK), `name`, `email`.

### 2. Books Table
Contains the library of books available in the system.
*   **Fields**: `id` (PK), `title`, `author`.
*   *Note: Author information is denormalized directly into the book record for simplicity.*

### 3. Favorites (Join Table)
The core table that tracks which user favorites which book.
*   **Fields**: `id` (PK), `user_id` (FK), `book_id` (FK).
*   **Logic**: Breaks the **Many-to-Many** relationship between Users and Books into two **One-to-Many** relationships.

## 🔗 How it Works
When a user clicks "favorite" on a book, a new entry is created in the `favorites` table containing the `user_id` of that person and the `book_id` of the selected book.