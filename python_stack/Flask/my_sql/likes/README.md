# 📱 Social Media Feed Database System

This project contains the database schema for a social media feed, designed to support features like user posting, commenting, and liking. The design is based on the wireframe provided in `image_f269b6.jpg`.

## 📊 Database Schema (ERD)

The Entity-Relationship Diagram (ERD) was developed to ensure efficient data retrieval for a dynamic feed. You can find the visual representation in `image_f253a8.png`.

### 1. Entities & Attributes
*   **User**: Represents the account holder (e.g., "Axsos Academy"). Stores `user_id`, `email`, and `password`.
*   **Post**: Stores the main feed content. Includes `post_id`, `title`, `content` (post text), and `created_at`.
*   **Comment**: Manages user interactions on specific posts, including `comment_id`, `content`, and timestamps.
*   **Like**: A join entity tracking which users have liked which posts via `like_id`.

### 2. Relational Logic
All foreign keys have been named in the **singular** format for clarity and standard convention:

*   **User ↔ Post**: One-to-Many relationship (A user writes multiple posts). Linked via `user_id`.
*   **Post ↔ Comment**: One-to-Many relationship (A post contains multiple comments). Linked via `post_id`.
*   **User ↔ Comment**: One-to-Many relationship (A user makes multiple comments). Linked via `user_id`.
*   **User/Post ↔ Like**: One-to-Many relationships to the Like table to track unique interactions. Linked via `user_id` and `post_id`.

---

## 🛠️ Mermaid Visualization

For developers using Mermaid-compatible viewers, here is the schema code:

```mermaid
erDiagram
    user ||--o{ post : "writes"
    user ||--o{ comment : "makes"
    user ||--o{ like : "likes"
    post ||--o{ comment : "contains"
    post ||--o{ like : "receives"

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

    like {
        int like_id PK
        int post_id FK
        int user_id FK
    }