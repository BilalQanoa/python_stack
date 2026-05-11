class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue."""
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if len(self.queue) != 0:
            return self.queue[0]
        else:
            raise IndexError("Queue is empty")


        return len(self.queue)