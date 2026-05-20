class MyCircularQueue: 
    
    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = 0
        self.count = 0 
        self.capacity = k 
    
    def enQueue(self, value: int) -> bool:
        """
        Inserts an element into the circular queue.
        
        Args:
            value (int): The integer value to be added to the queue.
            
        Returns:
            bool: True if the operation is successful (has space), False if the queue is full.
        """
        if self.count == self.capacity:
            return False
        self.queue[(self.head + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Deletes an element from the circular queue.
        
        Returns:
            bool: True if the operation is successful (not empty), False if the queue is empty.
        """
        if self.count == 0:
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True
    
    def Front(self) -> int:
        """
        Gets the front item from the queue without removing it.
        
        Returns:
            int: The value of the front element, or -1 if the queue is empty.
        """
        if self.count == 0:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Gets the last item from the queue without removing it.
        
        Returns:
            int: The value of the rear element, or -1 if the queue is empty.
        """
        if self.count == 0:
            return -1
        return self.queue[(self.head + self.count - 1) % self.capacity]
    
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.count == 0  
    
    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        
        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return self.count == self.capacity
    


obj = MyCircularQueue(3)
print(obj.enQueue(1))
print(obj.deQueue())
print(obj.Front())
print(obj.Rear())
print(obj.isEmpty())
print(obj.isFull())
