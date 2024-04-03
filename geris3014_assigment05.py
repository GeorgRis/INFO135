#1
# Full binary er når det enten er 0 eller 2 kanter.
# Alle trær er Full binary trees.

#2
# Ikke III og IIII siden ingen peker på seg selv.
# Det er II siden C peker bare på d

#3 list of lists binary tree
def binarty_tree(r):
    return [r, [], []]


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


def insert_left_child(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right_child(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root

my_tree = binarty_tree('1')

insert_left_child(my_tree, '2')
insert_right_child(my_tree, '3')

insert_left_child(get_left_child(my_tree), '4')
insert_left_child(get_right_child(my_tree), '5')
insert_right_child(get_right_child(my_tree), '6')

print(my_tree)

#4
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.graph:
            self.graph[from_vertex] = []
        self.graph[from_vertex].append(to_vertex)
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)


    def dfs(self, start):
        visited = []
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                for x in self.graph.get(vertex, []):
                    if x not in visited:
                        stack.append(x)
        return visited


def build_my_graph2():
    graph = Graph()
    vertices = ['a','b','c','d','e']
    for vertex in vertices:
        graph.add_vertex(vertex)
    edges = [
        ('a', 'c'), ('a', 'd'),
        ('b', 'a'),
        ('c', 'b'),
        ('d', 'e'),
        ('e', 'a')
    ]
    for from_vertex, to_vertex in edges:
        graph.add_edge(from_vertex,to_vertex)

    return graph.dfs('b')

print(build_my_graph2())

#5
class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        if self.value is not None:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        else:
            self.left_child = None
            self.right_child = None

    def is_empty(self):
        return self.value is None

    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        elif value < self.value:
            self.left_child.insert(value)
        elif value > self.value:
            self.right_child.insert(value)

    def compute_sum(self):
        if self.is_empty():
            return 0
        else:
            return self.value + self.left_child.compute_sum() + self.right_child.compute_sum()

    def compute_count(self):
        if self.is_empty():
            return 0
        else:
            return 1 + self.left_child.compute_count() + self.right_child.compute_count()

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)
my_tree.insert(10)
my_tree.insert(12)
print('sum:', my_tree.compute_sum())
print('number of nodes:', my_tree.compute_count())