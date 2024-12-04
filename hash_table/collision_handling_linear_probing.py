"""Implement hash table where collisions are handled using linear probing.  
Take the hash table implementation that uses chaining and modify methods to use linear probing. 
Keep MAX size of arr in hashtable as 10."""


# Here, linear probing method for collision avoidance is implemented which is inferior to the chaining method as it isn't dynamic

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self, key):
        hash = 0
        for el in key:
            hash += ord(el)
        return hash % self.MAX 

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        temp = h
        slot_or_item_found = False

        while not slot_or_item_found:
            if self.arr[h] == None or self.arr[h][0] == key:
                self.arr[h] = (key, value)
                slot_or_item_found = True
            
            h = (h+1)%self.MAX # linear searching technique which doesn't exceed the MAX value
            if h == temp: # Checking for infinite loop if the program completes a whole circle, it should halt
                return MemoryError("Insufficient storage  !!!!")


    def __getitem__(self, key):
        h = self.get_hash(key)
        temp = h
        slot_or_item_found = False

        while not slot_or_item_found:
            if self.arr[h] == None or self.arr[h][0] == key:
                return self.arr[h][1]
            
            h = (h+1)%self.MAX
            if h == temp:
                return KeyError("No element with such key found  !!!!")
    

    def __delitem__(self, key):
        h = self.get_hash(key)
        temp = h
        slot_or_item_found = False

        while not slot_or_item_found:
            if self.arr[h] == None or self.arr[h][0] == key:
                self.arr[h] = None
                slot_or_item_found = True
            
            h = (h+1)%self.MAX
            if h == temp:
                return KeyError("No element with such key found  !!!!")


if __name__ == "__main__":
    t = HashTable()
    t['march 6'] = 122
    t['march 6'] = 68
    t['march 8'] = 2
    t['march 4'] = 78
    t['march 17'] = 344
    print(t.arr)
    print(t['march 6'])
    print(t['march 17'])
    del t['march 17']
    print(t.arr)
    del t['march 8']
    print(t.arr)
    del t['march 89']
    print(t.arr)
