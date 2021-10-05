# create class for node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None # Pointer --->

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def length(self):
        counter = 0
        current_node = self.head
        while current_node.next != None:
            counter += 1
            current_node = current_node.next
        return counter

    def content(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    #def delete(self):



# ------------------------------- TEST CASE --------------------------------- #
test_list = LinkedList()
print(f"List length: {test_list.length()}")

test_list.append('Tony')
test_list.append('Montana')
test_list.append(12)
test_list.append(True)

test_list.content()
print(f"List length: {test_list.length()}")




'''
Linked list has no liniar order. The order of the elements is controlled by the
data structure.

Each node has a pointer which links the next node in the list.

Variations: Singily linked list / Doubly linked list.

Worst case O(n) to retrieve information or delete the last element. Other than that,
O(1) - meaning this is an efficient way of storing and retrieving data.

Memory allocation is dynamic and maximum size of list depends on heap stack.

Can only be accessed sequentially, not by direct index location such as a list.
'''
