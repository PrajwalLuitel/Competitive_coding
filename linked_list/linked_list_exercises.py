class Node:
    def __init__(self, value=None, next=None):
        self.value = value
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
            llstr += str(itr.value) + " -> "
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


    # Exercise 1:
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            print("The linked list is empty!!")
            return

        iter = self.head
        while iter.value:
            if iter.value == data_after:
                new_node = Node(data_to_insert, iter.next)
                iter.next = new_node
                break
            if iter.next is None:
                print("The value is not in the linked list!!!")
                break
            iter = iter.next



    # Exercise 2
    # Remove first node that contains data
    def remove_by_value(self, data):
        if self.head is None:
            print("Linked list is empty!!")
            return
        
        if self.head.value == data:
            self.head = self.head.next
            return
        
        iter = self.head
        while iter:
            if iter.next is not None and iter.next.value == data:
                iter.next = iter.next.next
                break
            iter = iter.next

        if iter is None:
            print("The value is not in the linked list!!!")
            return




class DoubleNode:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next



class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None



    def insert_at_beginning(self, value):
        new_node = DoubleNode(value, None, self.head)

        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node

        self.head = new_node
    
    def insert_at_end(self,value):
        new_node = DoubleNode(value, self.tail, None)

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        if not self.head:
            print("The linked list is empty!!")
            return

        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        
    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        if not self.tail:
            print("The linked list is empty!!")
            return
        
        current_node = self.tail
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.prev



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
    ll.insert_after_value("Banana", "Kiwi")
    ll.display()

    ll.remove_by_value("Grape")
    ll.display()
    ll.remove_by_value("Grapezzz")
    ll.display()

    print("\n\nDouble Linked List:\n\n")
    dll = DoubleLinkedList()
    dll.insert_at_beginning(2)
    dll.insert_at_beginning(21)
    dll.insert_at_end(678)
    dll.insert_at_end(777)

    print("Forward printing: ")
    dll.print_forward()
    print("\nBackward printing: ")
    dll.print_backward()
