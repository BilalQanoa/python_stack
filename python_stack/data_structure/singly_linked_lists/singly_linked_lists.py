class Node:
    def __init__(self, value):
        self.value = value

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_to_back(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_values(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def remove_from_front(self):
        if not self.head:
            return
        self.head = self.head.next

    def remove_from_back(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def remove_value(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def insert_at_position(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if not current:
                return
            current = current.next
        if not current:
            return
        new_node.next = current.next
        current.next = new_node