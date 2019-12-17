import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list2 import DoublyLinkedList, ListNode

# reference http://www.openbookproject.net/thinkcs/python/english2e/ch18.html


class Queue(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0
         # Why is our DLL a good choice to store our elements?
        self.storage = []

    def enqueue(self, value):
        self.size += 1
        self.add_to_head(value)
        
        
    def dequeue(self):
        self.size -= 1
        self.remove_from_tail()
        

    def len(self):
        return self.size

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.len())

print(q.get_max())

q.dequeue()

print(q.get_max())
#  * Should have the methods: `enqueue`, `dequeue`, and `len`.
#    * `enqueue` should add an item to the back of the queue.
#    * `dequeue` should remove and return an item from the front of the queue.
#    * `len` returns the number of items in the queue.

#    Addition takes place only at the tail, and removal takes place only at the head. 
#    The basic operations are: enqueue(x) : add an item at the tail. dequeue : remove the item at the head.