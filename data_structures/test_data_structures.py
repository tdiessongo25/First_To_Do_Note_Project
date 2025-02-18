import unittest
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.linked_list import LinkedList
from data_structures.doubly_linked_list import DoublyLinkedList
from data_structures.cyclic_linked_list import CyclicLinkedList

class TestDataStructures(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.size(), 2)

    def test_queue(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.front(), 1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.size(), 2)

    def test_linked_list(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        
        self.assertEqual(ll.display(), "1->2->3")
        
        ll.prepend(0)
        self.assertEqual(ll.display(), "0->1->2->3")
        
        ll.delete(2)
        self.assertEqual(ll.display(), "0->1->3")

    def test_doubly_linked_list(self):
        dll = DoublyLinkedList()
        
        # Test append
        dll.append(1)
        dll.append(2)
        dll.append(3)
        self.assertEqual(dll.display_forward(), "1<->2<->3")
        self.assertEqual(dll.display_backward(), "3<->2<->1")
        
        # Test prepend
        dll.prepend(0)
        self.assertEqual(dll.display_forward(), "0<->1<->2<->3")
        
        # Test delete
        dll.delete(2)
        self.assertEqual(dll.display_forward(), "0<->1<->3")
        
        # Test delete head
        dll.delete(0)
        self.assertEqual(dll.display_forward(), "1<->3")
        
        # Test delete tail
        dll.delete(3)
        self.assertEqual(dll.display_forward(), "1")

    def test_cyclic_linked_list(self):
        cll = CyclicLinkedList()
        
        # Test append
        cll.append(1)
        cll.append(2)
        cll.append(3)
        self.assertEqual(cll.display(), "1->2->3->(head)")
        
        # Test prepend
        cll.prepend(0)
        self.assertEqual(cll.display(), "0->1->2->3->(head)")
        
        # Test delete
        cll.delete(2)
        self.assertEqual(cll.display(), "0->1->3->(head)")
        
        # Test delete head
        cll.delete(0)
        self.assertEqual(cll.display(), "1->3->(head)")
        
        # Test delete last remaining elements
        cll.delete(1)
        cll.delete(3)
        self.assertEqual(cll.display(), "")

if __name__ == '__main__':
    unittest.main() 