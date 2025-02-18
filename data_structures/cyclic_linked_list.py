class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CyclicLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add a new node with data to the end of the list"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
            
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
    
    def prepend(self, data):
        """Add a new node with data to the beginning of the list"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
            
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
        self.head = new_node
    
    def delete(self, data):
        """Delete the first occurrence of data in the list"""
        if self.head is None:
            return
            
        # If head node contains data
        if self.head.data == data:
            if self.head.next == self.head:
                self.head = None
                return
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return
            
        # Search for the node to delete
        current = self.head
        while current.next != self.head:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def display(self):
        """Display all elements in the list"""
        if self.head is None:
            return ""
            
        elements = []
        current = self.head
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return "->".join(elements) + "->(head)" 