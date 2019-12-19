import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list2 import DoublyLinkedList, ListNode

# reference http://www.openbookproject.net/thinkcs/python/english2e/ch18.html


class Queue:
    def __init__(self):
        self.size = 0
         # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None
        

    def len(self):
        return self.size

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# print(q.len())

# print(q.get_max())

# q.dequeue()

# print(q.get_max())
#  * Should have the methods: `enqueue`, `dequeue`, and `len`.
#    * `enqueue` should add an item to the back of the queue.
#    * `dequeue` should remove and return an item from the front of the queue.
#    * `len` returns the number of items in the queue.

#    Addition takes place only at the tail, and removal takes place only at the head. 
#    The basic operations are: enqueue(x) : add an item at the tail. dequeue : remove the item at the head.