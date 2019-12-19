from doubly_linked_list import DoublyLinkedList

#doublyLinkedList gives a node order:
#self.head
#self.tail

#ListNode:
#self.value
#self.prev
#self.next

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = dict() #cant use dict to track order, the order can change and dictionaries are orderless
        self.order = DoublyLinkedList() #
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #pull the value out of the dict using the key
        if key in self.storage:
            node = self.storage[key]#create a new reference to self.storage[key] just to make it clear what is happening
            print(node.value, "inside the node is a value with a key/value pair")
            #could just do "self.order.move_to_end(self.storage[key]"
            self.order.move_to_end(node)
            return node.value[1] #access a tuple just like an array indice
        else:
            return None #if key value pair does not exist in the dict

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """


    def set(self, key, value):
        #If already exist, overwrite value
        if key in self.storage:
           node = self.storage[key]
           node.value = (key, value) #create a new tuple
           self.order.move_to_front(node)
           return
        #If at max capacity, dump oldest - remove from tail of DLL
        if self.size == self.limit:
            #dump the oldest
            # remove from linked list
            # remove from dict
            del self.storage[self.order.head.value[0]]#the value is in the first index of the tuple
            self.order.remove_from_head()
            self.size -= 1
        #add the pair to the cache - add to dict and add it to the nodes in DLL
        #Defining tail as most recent and head as oldest
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1

        

    def get_dictionary(self):
        for key, value in self.storage.items():
            print(f"key: {key}, value: {value.value}")

    
    def get_dictionary2(self):
        for value in self.storage.values():
            print(f"value: {value.value}")

    def get_dict(self):
        for item in self.storage:
            print(item)

    def get_size(self):
        return self.size

            

   



c = LRUCache()
c.set('item1',1)
c.set('item2',2)
c.set('item3',3)
c.set('item4',4)
c.set('item5',5)
c.set('item6',6)
c.set('item7',7)
c.set('item8',8)
c.set('item9',9)
c.set('item10',10)
c.set('item11',11)
c.set('item12',12)
c.get_dictionary()
c.get_dictionary2()
c.get_dict()
c.order.get_cache()
