# 📝 Blog Platform Database System (Blogspot Clone)

This schema supports a multi-user, multi-blog platform with collaborative administration and site analytics.

## 🔑 Key Features
*   **Collaborative Admin**: Uses a `blog_admins` join table to allow multiple users to manage a single blog.
*   **Content Management**: Supports posts, nested comments, and file attachments.
*   **User Analytics**: Tracks logged-in users' behavior, including IP addresses and session duration.

## 🔗 Relational Logic
1.  **Many-to-Many (Users & Blogs)**: Managed via `blog_admins` to handle co-administration.
2.  **One-to-Many (Blog & Posts)**: Each blog owns multiple posts.
3.  **One-to-Many (Post & Files/Comments)**: Posts are the central hub for interaction and media.
4.  **One-to-Many (User & PageLogs)**: Captures tracking data for each registered user session.

## 🛠️ Implementation Note
In MySQL Workbench, ensure all foreign keys use the **singular** naming convention (e.g., `user_id` NOT `users_id`) to maintain standard naming practices.