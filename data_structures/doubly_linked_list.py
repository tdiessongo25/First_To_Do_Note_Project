class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        """Add a new node with data to the end of the list"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
            
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    
    def prepend(self, data):
        """Add a new node with data to the beginning of the list"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
            
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def delete(self, data):
        """Delete the first occurrence of data in the list"""
        current = self.head
        
        # If list is empty
        if current is None:
            return
            
        # If head node contains data
        if current.data == data:
            self.head = current.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return
            
        # Search for the node to delete
        while current:
            if current.data == data:
                # If it's the last node
                if current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
    
    def display_forward(self):
        """Display elements from head to tail"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "<->".join(elements)
    
    def display_backward(self):
        """Display elements from tail to head"""
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        return "<->".join(elements) 