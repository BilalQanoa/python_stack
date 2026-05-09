# Assignment: Database Normalization

## 📌 Overview
This project involves refactoring an initial Entity-Relationship Diagram (ERD) that violated several database normalization rules. The goal was to redesign the schema to track student information and interests while adhering to the **First (1NF)**, **Second (2NF)**, and **Third (3NF)** Normal Forms.

## 🛠️ Problems Identified in the Original Model
The original schema (as seen in `image_ab8b20.png`) had several issues:
*   **Multi-valued Attributes**: The `interests` field contained multiple values in a single cell, violating **1NF**.
*   **Repeating Groups**: Fields like `address1` and `address2` represented repeating groups, also violating **1NF**.
*   **Many-to-Many Relationship**: A student can have multiple interests, and an interest can belong to multiple students. This relationship was not properly handled.

## ✅ The Normalized Solution
To achieve a fully normalized state, the schema was broken down into the following structure (refer to `watermarked_img_2894787781654610453.png`):

### 1. First Normal Form (1NF)
*   **Atomicity**: Removed the multi-valued `interests` field and the repeating `address` fields.
*   Each attribute now contains only atomic (indivisible) values.

### 2. Second Normal Form (2NF)
*   Ensured that all non-key attributes are fully functionally dependent on the primary key.
*   Separated **Dojos** and **Students** into distinct tables, as Dojo information (like location) is not dependent on a specific Student ID.

### 3. Third Normal Form (3NF)
*   Removed transitive dependencies. 
*   Created a separate `interests` table so that interest names are stored only once, preventing data redundancy.

### 4. Many-to-Many Relationship (The Junction Table)
As suggested in the assignment hint, a **new type of relationship** was created:
*   **`student_interests`**: This is a junction (join) table that connects `students` and `interests`. It contains foreign keys for both, allowing a flexible many-to-many mapping.

## 🗂️ Final Table Structure
*   **dojos**: Stores dojo names and locations.
*   **students**: Stores individual student names and links to their respective dojo.
*   **interests**: A lookup table for all possible interest categories.
*   **student_interests**: The bridge table linking students to their specific interests.

---
*Completed as part of the Database Normalization module.*