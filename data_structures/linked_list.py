class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add a new node with data to the end of the list"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
            
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        """Add a new node with data to the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        """Delete the first occurrence of data in the linked list"""
        if self.head is None:
            return
            
        if self.head.data == data:
            self.head = self.head.next
            return
            
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def display(self):
        """Print all elements in the linked list"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "->".join(elements) 