# User Dashboard System - Database Design (ERD)

## 📌 Project Overview
This repository contains the Entity-Relationship Diagram (ERD) for a comprehensive **User Dashboard System**, modeled after the provided wireframes. The design focuses on user management, role-based access control, and a hierarchical messaging system.

## 🏗️ Database Architecture
The schema is built around three core entities to ensure data integrity and full functionality as per the project requirements:

### 1. Users Table (`users`)
This is the central table for account management and profile data.
*   **Attributes**: Includes `id`, `first_name`, `last_name`, `email`, `password`, and `description`.
*   **Role Management**: Features a `user_level` field (Admin/Normal) to handle permissions for the Admin Dashboard vs. the User Dashboard.
*   **Profile**: Stores biographical data used in the "User Information" page.

### 2. Messages Table (`messages`)
Handles the primary communication layer where users can post on each other's walls.
*   **Logic**: Uses a dual-foreign key system:
    *   `author_id`: Links to the user who wrote the message.
    *   `recipient_id`: Links to the user on whose profile the message is displayed.
*   **Content**: Utilizes `LONGTEXT` to accommodate detailed posts.

### 3. Comments Table (`comments`)
Facilitates threaded discussions and replies to specific messages.
*   **Logic**: Each record is linked to a `user_id` (the commenter) and a `message_id` (the parent message).
*   **Purpose**: This allows the system to display nested replies under each main message in the "User Information" view.

## 🔗 Key Relationships
*   **One-to-Many (Users to Messages)**: A single user can write or receive multiple messages.
*   **One-to-Many (Users to Comments)**: A user can post multiple replies.
*   **One-to-Many (Messages to Comments)**: Each main message can host multiple sub-comments/replies.

## 🛠️ Tools Used
*   **MySQL Workbench**: For EER Modeling and relationship mapping.

---
*Developed as part of the Database Design Assignment.*