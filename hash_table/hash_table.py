class HashTable:

    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)] 
    
    def get_hash(self, key):
        hash_value = 0
        for el in key:
            hash_value += ord(el)
        
        return hash_value % self.MAX


    def __setitem__(self, key, value):
        hash = self.get_hash(key)

        self.arr[hash] = value
    
    def __getitem__(self, key):
        hash = self.get_hash(key)
        return self.arr[hash]

    def __delitem__(self, key):
        hash = self.get_hash()
        self.arr[hash] = None


if __name__ == '__main__':
    ht = HashTable()
    ht['Apple'] = 323
    ht['Mango'] = 442
    ht['Banana'] = 11
    ht['Peach'] = 2
    print(f"The value for key Apple is: {ht['Apple']}")
    print(f"The value for key Mango is: {ht['Mango']}")
    print(f"The value for key Banana is: {ht['Banana']}")
    print(f"The value for key Peach is: {ht['Peach']}")