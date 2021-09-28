from Node import Node
from random import randint
import menu

class LinkedList:

    def __init__(self, node=None):
        self.head = node

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, node):
        self.__head = node

    def print(self, node):
        print(node.data, end='->')
        if node.previous == None:
            print("None")
            return
        self.print(node.previous)

    def add_elem(self, data_):
        last = self.to_end(self.head)
        last.previous = Node(data_)

    def to_end(self, node):
        if node.previous == None:
            return node
        return self.to_end(node.previous)

    def random_linked_list(self):
        for i in range(20):
            self.add_elem(randint(0, 100))

    def enter_list(self):
        for i in range(menu.enter_int("Enter count of elements")):
            self.add_elem(menu.enter_int("Enter count of elements"))

    def move(self, k):
        for i in range(k):
            self.to_end(self.head).previous = Node(self.head.data)
            self.head = self.head.previous
            self.print(self.head)

