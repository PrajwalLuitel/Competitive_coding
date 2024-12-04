"""poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
You have to read this file in python and print every word and its count as show below. 
Think about the best data structure that you can use to solve this problem and figure out why you selected 
that specific data structure."""


# The data structure selected here is a modified hash table which makes it easier to count by just adding the item into the class object and easy deletion and retrieval as well

class WordCount:
    def __init__(self):
        self.MAX = 50
        self.arr = [[] for i in range(self.MAX)]
    

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for el in self.arr[h]:
            if el[0]==key: return el[1]
    
    def add(self,key):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key, element[1]+1)
                found = True
                break
        if not found:
            self.arr[h].append((key,1))


    def __delitem__(self, key):
        h = self.get_hash(key)

        if self.arr[h] != []:
            for el in self.arr[h]:
                if el[0] == key:
                    if el[1] == 1:
                        self.arr[h].remove(el)
                        return
                    else:
                        el = (el[0], el[1]-1)
                


if __name__ == "__main__":
    file = open('hash_table/poem.txt', 'r')
    characters = file.read()

    cleaned_text = ""
    for char in characters:
        if ord(char.lower()) in range(97, 123) or char == " ":
            cleaned_text+= char.lower()

    words = cleaned_text.split(' ')

    counter = WordCount()
    for word in words:
        counter.add(word)


    done = []
    for word in words:    
        if word not in done:
            print(f"Count of {word}: {counter[word]}")
            done.append(word)

    
