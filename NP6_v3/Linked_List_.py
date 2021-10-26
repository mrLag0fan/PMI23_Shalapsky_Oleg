from Node import Node
from random import randint
import validdata
from abc import ABC, abstractmethod
from Observer import Observer


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, n, a, b, data):
        pass

class IterEnterGen(Strategy):
    def do_algorithm(self, n, a, b, data):
        for i in range(1, n):
            yield Node(validdata.enter_int(f"Enter {i} element"))

class IterRandomGen(Strategy):
    def do_algorithm(self, n, a, b, data):
        for i in range(1, n):
            yield Node(randint(a, b))

class FromFile(Strategy):
    def do_algorithm(self, n, a, b, data):
        for i in range(1, len(data)):
            yield Node(data[i])

class LinkedList:

    observers = []
    observers.append(Observer())

    def __init__(self, strategy: Strategy=None, node=None):
        self.head = node
        self.strategy = strategy


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.previous

    def __str__(self):
        res = ""
        for i in self:
            res += f"{i.data}->"
        res += "None"
        return res

    def genetor(self, m, a, b, data):
        return self.strategy.do_algorithm(m, a, b, data)

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, node):
        self.__head = node

    @property
    def strategy(self) -> Strategy:
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self.__strategy = strategy

    def add_observer(self, o: Observer):
        LinkedList.observers.append(o)

    def remove_observer(self, o: Observer):
        LinkedList.observers.remove(o)

    def motify_observers(self, msg, l_o, l_n):
        for i in range(len(LinkedList.observers)):
            LinkedList.observers[i].update(msg, l_o, l_n)


    def length(self, node,  len):
        while node.previous != None:
            len += 1
            return self.length(node.previous, len)
        return len

    def is_position_valid(self, k):
        if k >= self.length(self.head, 1)+1 or k < 0:
            print("Position isn't valid")
            return False
        else:
            return True

    def move_around(self, node, k, i):
        while i < k:
            i+=1
            return self.move_around(node.previous, k, i)
        return node

    def add_elem_to_end(self, data_):
        last = self.to_end(self.head)
        last.previous = Node(data_)

    def add_element(self, date_, k):
        temp = self.move_around(self.head, k-1, 0).previous
        self.move_around(self.head, k-1, 0). previous = Node(date_)
        self.move_around(self.head, k-1, 0).previous.previous = temp

    def del_elem(self, k):
        if k != 0:
            temp = self.move_around(self.head, k+1, 0)
            self.move_around(self.head, k-1, 0).previous = temp
        else:
            self.head = self.head.previous

    def del_from_a_to_b(self, a, b):
        if a != 0:
            temp = self.move_around(self.head, b+1, 0)
            self.move_around(self.head, a-1, 0).previous = temp
        else:
            self.head = self.move_around(self.head, b+1, 0)

    def to_end(self, node):
        if node.previous == None:
            return node
        return self.to_end(node.previous)

    def random_linked_list(self, n, a, b):
        self.head = Node(randint(a, b))
        for i in range(n-1):
            self.add_elem_to_end(randint(a, b))

    def enter_list(self, n):
        self.head = Node(validdata.enter_int("Enter 1 element"))
        for i in range(n-1):
            self.add_elem_to_end(validdata.enter_int(f"Enter {i+2} element"))

    def move(self, k):
        for i in range(k):
            self.to_end(self.head).previous = Node(self.head.data)
            self.head = self.head.previous

