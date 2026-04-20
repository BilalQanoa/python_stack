# Singly Linked List Project

This project is a simple Python implementation of a **Singly Linked List**. It demonstrates how to manage a collection of data using nodes and pointers instead of traditional arrays.

## 📝 What I Implemented

### 1. The Core Structure
* **Node Class**: I created a basic unit (Node) that stores a value.
* **SinglyLinkedList Class**: This is the main class that manages the list, starting with a `head` pointer.

### 2. Adding Data
* **`add_to_front(value)`**: Efficiently adds a new element at the very beginning of the list.
* **`add_to_back(value)`**: Traverses the list to append an element at the end.
* **`insert_at_position(value, position)`**: Adds an element at a specific index by moving through the nodes.

### 3. Removing Data
* **`remove_from_front()`**: Removes the first node.
* **`remove_from_back()`**: Removes the last node by finding the second-to-last element.
* **`remove_value(value)`**: Searches for a specific value and deletes its node from the list.

### 4. Viewing Data
* **`print_values()`**: A simple loop that visits every node and prints its content to the console.

## 🛠 How it Works
The code is built to handle **Edge Cases**, such as:
- Checking if the list is empty before deleting.
- Handling lists with only one node.
- Ensuring the program doesn't crash if an invalid position is given.

## 🚀 How to Run
1. Make sure you have Python installed.
2. Run the script containing the `SinglyLinkedList` class.
3. You can create an instance and chain methods (if implemented) or call them sequentially.

```python
my_list = SinglyLinkedList()
my_list.add_to_front("Data")
my_list.add_to_back("Structures")
my_list.print_values()