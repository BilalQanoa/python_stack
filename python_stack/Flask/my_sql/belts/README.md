# 🥋 Martial Arts Belt Tracking System ERD

This database schema is designed to manage users and the multiple martial arts belts they have earned, as shown in the provided wireframe.

## 📊 Database Structure

### 1. User Table
Stores the identity of the practitioners.
*   **Fields**: `user_id` (PK), `name`.

### 2. Belt Table
A lookup table for all possible belt colors available in the system.
*   **Fields**: `belt_id` (PK), `color`.

### 3. User_Belts (Join Table)
Since a user can have multiple belts (e.g., Andrew Lee has yellow, red, and black), we use this table to break the **Many-to-Many** relationship.
*   **Foreign Keys**: `user_id` and `belt_id` (singular naming convention).

## 🔗 Relationships
*   **Many-to-Many**: Achieved via the `user_belt` table.
*   **Integrity**: Ensures that belt types aren't duplicated across users and allows for easy filtering (e.g., "Show all users with a yellow belt").

erDiagram
    user ||--o{ user_belt : "has"
    belt ||--o{ user_belt : "assigned_to"

    user {
        int user_id PK
        string name
    }

    belt {
        int belt_id PK
        string color
    }

    user_belt {
        int id PK
        int user_id FK
        int belt_id FK
    }