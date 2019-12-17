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
        #add item to tail
        self.add_to_tail(value)
        # self.size+= 1
       

    def pop(self):
        #remove last item in
        self.remove_from_tail()
        # self.size-=1
        

    def len(self):
        self.size = self.length
        return self.size

  

     

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.get_max())
print(s.len(), "length")
s.pop()
print(s.len(), "length")

print(s.get_max())
s.pop()
s.pop()
s.pop()

print(s.len(), "length")


