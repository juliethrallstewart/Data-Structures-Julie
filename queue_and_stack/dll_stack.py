import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list2 import DoublyLinkedList


#last in first out 
class Stack(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        #add item to head 
        self.add_to_head(value)
        self.size+= 1
       

    def pop(self):
        #remove item from head
        self.remove_from_head()
        self.size-=1
        

    def len(self):
        return self.size

  

     

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.len())
s.pop()
print(s.len())

print(s.get_max())