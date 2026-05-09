# 📝 Simple Blog Database System

This project features the core database architecture for a simple blogging platform. It manages users, posts, and comments, focusing on clean relational mapping.

## 📊 Database Schema (ERD)

The database is designed with a relational structure that ensures data integrity through Primary Keys (PK) and Foreign Keys (FK).

### 1. Entities & Attributes
*   **User**: Stores account credentials, including a unique `user_id`, `email`, and `password`.
*   **Post**: Contains blog content with a `post_id`, `title`, `content`, and a `created_at` timestamp.
*   **Comment**: Manages user interactions with a `comment_id`, `content`, and `created_at` timestamp.

### 2. Relationships
*   **User ↔ Post**: A **One-to-Many** relationship; one user can write multiple posts, but each post belongs to a single author.
*   **User ↔ Comment**: A **One-to-Many** relationship; a user can make multiple comments across different posts.
*   **Post ↔ Comment**: A **One-to-Many** relationship; each post can contain numerous comments, while each comment is tied to one specific post.

---

## 🛠️ ERD Diagram (Mermaid Visualization)

You can render the schema directly in GitHub using the following Mermaid code:

```mermaid
erDiagram
    user ||--o{ post : "writes"
    user ||--o{ comment : "makes"
    post ||--o{ comment : "contains"

    user {
        int user_id PK
        string email
        string password
    }

    post {
        int post_id PK
        string title
        string content
        datetime created_at
        int user_id FK
    }

    comment {
        int comment_id PK
        string content
        datetime created_at
        int post_id FK
        int user_id FK
    }