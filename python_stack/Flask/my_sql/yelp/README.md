## 🍴 Restaurant Review System Schema

This database schema is designed to support a restaurant listing and review application based on the provided wireframe.

### Key Features:
*   **Dynamic Reviews**: Supports many-to-one relationships where a single restaurant can have hundreds of reviews (e.g., "914 reviews").
*   **User Attribution**: Each review snippet is linked to a specific user profile to display their avatar and feedback.
*   **Relational Integrity**: Uses singular foreign keys (`restaurant_id`, `user_id`) to maintain clean data mapping between users and the venues they visit.

### Relationship Logic:
1. **Restaurants to Reviews**: One-to-Many. A restaurant can have many reviews, but each review belongs to one restaurant.
2. **Users to Reviews**: One-to-Many. A user can write many reviews, but each specific review is written by one user.

erDiagram
    restaurants ||--o{ reviews : "has"
    users ||--o{ reviews : "writes"

    restaurants {
        int restaurant_id PK
        string name
        string image_url
    }

    users {
        int user_id PK
        string name
        string profile_image_url
    }

    reviews {
        int review_id PK
        int rating
        string content
        int restaurant_id FK
        int user_id FK
    }