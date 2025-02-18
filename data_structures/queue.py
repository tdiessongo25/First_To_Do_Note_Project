class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the end of the queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the first item in the queue"""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Dequeue from empty queue")
    
    def front(self):
        """Return the first item without removing it"""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Front of empty queue")
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the queue"""
        return len(self.items) 