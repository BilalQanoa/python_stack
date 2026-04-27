# Doubly Linked List Implementation in Python

A professional implementation of a **Doubly Linked List (DList)** data structure using Python and Object-Oriented Programming (OOP) principles.

## 📌 Overview
Unlike a Singly Linked List, a **Doubly Linked List** consists of nodes that have references to both the **next** and the **previous** node. This allows for bidirectional traversal and more efficient deletions in certain scenarios.



## 🚀 Features implemented
The current Python script includes the following core functionalities:

* **Node Class**: A custom object to store data (`value`) and pointers (`next`, `prev`).
* **Dynamic Insertion**: Add nodes to the end of the list with automatic pointer management.
* **Smart Deletion**: Remove nodes by value while maintaining the integrity of the chain.
* **Contextual Insertion**: A specialized method to insert a new node specifically between two existing values.

## 🛠️ Code Structure

### 1. The Node Class
Each element in the list is an instance of the `Node` class:
- `value`: The data stored in the node.
- `next`: Pointer to the succeeding node (defaults to `None`).
- `prev`: Pointer to the preceding node (defaults to `None`).

### 2. The DoublyLinkedList Class
This class manages the nodes and provides the following methods:
- `add_to_end(value)`: Traverses to the end of the list and appends a new node.
- `delete_node(value)`: Searches for a value and re-links the surrounding nodes to remove it.
- `insert_between(value, prev_value, next_value)`: Inserts a new value only if the specified sequence is found.

## 📊 Complexity Analysis
| Operation       | Time Complexity |
| :-------------- | :-------------- |
| Append to End   | $O(n)$          |
| Search / Delete | $O(n)$          |
| Insert Between  | $O(n)$          |

> **Note:** The current `add_to_end` operation is $O(n)$. This can be optimized to $O(1)$ by adding a `tail` pointer to the `DoublyLinkedList` class.

## 💻 How to Use
```python
# Initialize the list
my_list = DoublyLinkedList()

# Add values
my_list.add_to_end(10)
my_list.add_to_end(20)
my_list.add_to_end(30)

# Insert 25 between 20 and 30
my_list.insert_between(25, 20, 30)

# Delete a node
my_list.delete_node(10)