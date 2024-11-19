class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        node = Node(value, self.head)
        self.head = node

    def display(self):
        if self.head is None:
            print("Linked list is empty. ")
            return
        
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " -> "
            itr = itr.next
        print(llstr)


    def insert_at_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(value, None)


    def insert_values(self, values):
        self.head = None

        for value in values:
            self.insert_at_end(value)


    def get_length(self):
        count = 0

        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print("Invalid index.")
            return

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr and count < index - 1:
            itr = itr.next
            count += 1

        if not itr or not itr.next:
            print("Index out of range.")
            return

        itr.next = itr.next.next


    def insert_at(self, index, value):
        if index <0 or index >= self.get_length():
            print("Invalid index.")
            return
        
        if index == 0:
            self.insert_at_beginning(value)
            return
        
        count = 0
        iter = self.head
        while iter and count < index - 1:
            iter = iter.next
            count += 1
        
        new_node = Node(value, iter.next)
        iter.next = new_node



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(21)
    ll.insert_at_end(678)
    ll.insert_at_beginning(233)
    ll.insert_at_end(4)

    ll.insert_values(["Apple", "Banana", "Mandarin", "Orange", "Pineapple"])
    print(f"The number of elements in the linked list is: {ll.get_length()}")


    ll.display()
    ll.remove_at(3)
    ll.display()
    ll.insert_at(3, "Grape")
    ll.display()