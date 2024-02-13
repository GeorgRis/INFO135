#1 Bruker laveste og går fra venstre til høyre(Kunne brukt høysete og gått fra høyre til venstre)
#[ 1502, 1560, 1600, 1540, 100, 1660, 1700, 2024 ]
#pass 1 [ 100, 1560, 1600, 1540, 1502, 1660, 1700, 2024 ]
#pass 2 [ 100, 1502, 1600, 1540, 1560, 1660, 1700, 2024 ]
#pass 3 [ 100, 1502, 1540, 1600, 1560, 1660, 1700, 2024 ]

#2
#[ 400, 10, 210, 160, 70, 220, 280, 380, 180, 260, 540 ]
#pass 1[ 10, 210, 160, 70, 220, 280, 380, 180, 260, 400, 540 ]
#pass 2[ 10, 160, 70, 210, 220, 280, 180, 260, 380, 400, 540 ]
#pass 3[ 10, 70, 160, 210, 220, 180, 260, 280, 380, 400, 540 ]

#3
def sort_and_rem_dup(arr):
    lr = []
    for i in bubble_sort(arr):
        if i not in lr:
            lr.append(i)
    return lr


def bubble_sort(arr):
    size = len(arr)
    for i in range(size):
        for j in range(0,size - i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

my_list = [5, 4, 3, 2, 1, 2, 3, 4, 5]
new_list = sort_and_rem_dup(my_list)
print(new_list)

#4
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)


class Queue:
    def __init__(self):
        self.items = []

    def enqueque(self, item):
        self.items.append(item)


def check_palindrome(word):
    stack = Stack()
    queue = Queue()
    for i in word:
        stack.push(i)
        queue.enqueque(i)
    #sjekke om palindrom(GJør om alt til lower om skal ha med store at store og små bokstaver samme)
    if stack.items[::-1] == queue.items:
        return f'Palidrome'
    else: return f'Not Palidrome'


print(check_palindrome('hello'))
print(check_palindrome('civic'))

