#1a worst case: log2(102400) = 17 steps
#1b worst case: log2(480000) = 19 steps


#2:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

liste = LinkedList()
node1 = Node("A")
node2 = Node("B")
liste.head = node1
node1.next = node2
liste.print_list()

#3
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)


def reverse_list(liste):
    stack = Stack()
    for i in liste:
        stack.push(i)
    return stack.items[::-1]

my_list = [1,2,3,4,5]
print(reverse_list(my_list))
