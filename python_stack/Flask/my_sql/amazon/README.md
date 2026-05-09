# 📦 Product Catalog System ERD

This database schema is designed based on a product browsing interface that allows users to filter products by **Brand**, **Category**, and **Character**.

## 📊 Database Entities

### 1. Products Table
The core table containing items for sale.
*   **Foreign Keys**: Linked to `category_id`, `brand_id`, and `character_id` to support the filtering tabs shown in the UI.

### 2. Categories Table
Supports a hierarchical structure (e.g., "Action Figures" as a parent with sub-categories like "Robots" or "Military Figures").

### 3. Brands & Characters Tables
Lookup tables that allow users to browse products associated with specific manufacturers or fictional icons.

## 🔗 Relational Logic
*   **One-to-Many (1:N)**: Each product is assigned to exactly one Category, one Brand, and one Character to ensure clean navigation.
*   **Foreign Key Naming**: All foreign keys follow the singular naming convention (`category_id`, `brand_id`, etc.) for consistency.