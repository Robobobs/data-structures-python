class Node:
    '''class representing individual node within a singly linked list'''
    def __init__(self, data=None):
        self.data = data
        self.next = None # Pointer --->


class SinglyLinkedList:
    '''class containing functionality for generating/modifying a singly linked list'''
    def __init__(self):
        self.head = Node()

    def append(self, data):
        '''add node to the end of the list'''
        new_node = Node(data)
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def get(self, index):
        '''returns data from specified index'''
        list_length = self.length()
        current_index = 0
        current_node = self.head

        if index in range(0, list_length):
            while True:
                current_node = current_node.next
                if current_index == index:
                    return current_node.data
                else:
                    current_index += 1
        else:
            print('ERROR: (get) index out of range!')
            return None

    def insert(self, data, index):
        '''inserts new node at specied index'''
        new_node = Node(data)
        current_node = self.head
        list_length = self.length()
        current_index = 0

        if index in range(0, list_length):
            while True:
                last_node = current_node
                current_node = current_node.next
                if current_index == index:
                    new_node.next = current_node
                    last_node.next = new_node
                    print(f"New node inserted at index {index}...")
                    return
                else:
                    current_index += 1
        else:
            print('ERROR: (insert) index out of range!')
            return

    def update(self, data, index):
        '''updates existing nodes data at specified index'''
        list_length = self.length()
        current_index = 0
        current_node = self.head

        if index in range(0, list_length):
            while True:
                current_node = current_node.next
                if index == current_index:
                    current_node.data = data
                    print(f"Data at index {index} updated...")
                    return
                else:
                    current_index += 1
        else:
            print('ERROR: (update) index out of range')
            return

    def delete(self, index):
        '''deletes node at specified index'''
        list_length = self.length()
        current_index = 0
        current_node = self.head

        if index in range(0, list_length):
            while True:
                last_node = current_node
                current_node = current_node.next
                if current_index == index:
                    last_node.next = current_node.next
                    print(f"Node at index {index} deleted...")
                    return
                else:
                    current_index += 1
        else:
            print('ERROR: (delete) index out of range!')
            return

    def length(self):
        '''returns the length of the linked list'''
        counter = 0
        current_node = self.head

        while current_node.next != None:
            counter += 1
            current_node = current_node.next
        return counter

    def display(self):
        '''displays all data elements within the linked list'''
        elements = []
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)
        return(elements)




# ------------------------------- TEST CASE --------------------------------- #
test_list = SinglyLinkedList()

print(f"List length: {test_list.length()}")

                                #Index
test_list.append('Tony')        #0
test_list.append('Montana')     #1
test_list.append(12)            #2
test_list.append(True)          #3

test_list.display()

print(f"List length: {test_list.length()}")
print(f"Element at index 0: {test_list.get(0)}")
print(f"Element at index 4: {test_list.get(4)}")

test_list.delete(5)
test_list.display()

test_list.delete(2)
test_list.display()

test_list.insert('Test data inserted', 1)
test_list.display()

test_list.insert('Another insert', 3)
test_list.display()

test_list.update('Changed to this', 0)
test_list.display()

test_list.update('Out of range', 5)
test_list.display()



'''
# --------------------------------- NOTES ----------------------------------- #


Linked list has no linier order. The order of the elements is controlled by the
data structure and is unidirectional.

Each node has a pointer which links to the next node in the list.

Variations: Singly linked list / Doubly linked list.

Worst case O(n) to retrieve information or delete the last element. Other than that,
O(1) - meaning this is an efficient way of storing and retrieving data.

Memory allocation is dynamic and maximum size of list depends on heap stack.

Data can only be accessed sequentially, not by direct index location such as in a normal array/list.

'''
