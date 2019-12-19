import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


#last in first out 
class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?

        #Answer: Memory, for a queue we have to add and remove from the front and the back
        #and since we are using a doublylinked list it is good to keep using one for consistency
        self.storage = DoublyLinkedList()

    def push(self, value):
        #add item to tail
        # self.add_to_tail(value)
        # self.storage.add_to_tail(value)
        self.storage.add_to_head(value)

        self.size+= 1
       

    def pop(self):
        #remove last item in
        # self.remove_from_tail()
        if self.size > 0:
            self.size -= 1
            # return self.storage.remove_from_tail()
            return self.storage.remove_from_head()

        else:
            return None
        

    def len(self):
        # self.size = self.length
        return self.size