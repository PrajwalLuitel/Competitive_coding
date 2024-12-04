class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        if len(self.arr[h]) == 1:
            return self.arr[h][0][0]
        else:
            for el in self.arr[h]:
                if el[0]==key: return el[-1]
    
    def __setitem__(self,key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        
        if not found:
            self.arr[h].append((key,value))


    def __delitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] != []:
            for el in self.arr[h]:
                if el[0] == key:
                    self.arr[h].remove(el)
                    return


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
