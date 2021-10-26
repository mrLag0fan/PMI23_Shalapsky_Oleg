from Linked_List_ import LinkedList, IterEnterGen, Strategy, IterRandomGen, FromFile
import validdata
from Node import Node
import random
from copy import deepcopy


class Options:

    def __init__(self, linked_list: LinkedList):
        self.__linked_list = linked_list

    @property
    def linked_list(self):
        return self.__linked_list

    def option1(self):
        try:
            self.linked_list.strategy = IterEnterGen()
            n = validdata.enter_int("Enter count of elements")
            if n <= 0:
                return -1
            gen_iter = self.__linked_list.genetor(n, 0, 0, 0)
            self.__linked_list.head = Node(validdata.enter_int("Enter 0 element"))
            for i in range(n):
                self.__linked_list.add_elem_to_end(next(gen_iter))
        except StopIteration:
            return

    def option2(self):
        n = validdata.enter_int("Enter count of elements")
        if n <= 0:
            return -1
        a = validdata.enter_int("Enter low bound")
        b = validdata.enter_int("Enter top bound")
        if a > b:
            a, b = b, a
        try:
            self.linked_list.strategy = IterRandomGen()
            gen_iter = self.__linked_list.genetor(n, a, b, 0)
            self.__linked_list.head = Node(random.randint(a, b))
            for i in range(n):
                self.__linked_list.add_elem_to_end(next(gen_iter))
        except StopIteration:
            return

    def option3(self):
        k = validdata.enter_int("Enter pos")
        if not self.__linked_list.is_position_valid(k):
            return
        l_o = deepcopy(self.__linked_list)
        self.__linked_list.add_element(validdata.enter_int("Enter date: "), k)
        l_n = deepcopy(self.__linked_list)
        self.__linked_list.motify_observers('Add', l_o, l_n)


    def option4(self):
        k = validdata.enter_int("Enter pos")
        if not self.__linked_list.is_position_valid(k):
            return
        l_o = deepcopy(self.__linked_list)
        self.__linked_list.del_elem(k)
        l_n = deepcopy(self.__linked_list)
        self.__linked_list.motify_observers('Delete', l_o, l_n)

    def option5(self):
        self.__linked_list.move(validdata.enter_int("Enter k"))

    def option6(self):
        print(self.__linked_list)

    def option7(self):
        exit()

    def option8(self):
        return -1

    def option9(self):
        try:
            self.linked_list.strategy = FromFile()
            file = open("in", "r")
            data = file.read().split(" ")
            gen_iter = self.__linked_list.genetor(len(data), 0, 0, data)
            self.__linked_list.head = Node(data[0])
            for i in range(len(data)):
                self.__linked_list.add_elem_to_end(next(gen_iter))
        except StopIteration:
            return

    def option10(self):
        a = validdata.enter_int("Enter low bound")
        b = validdata.enter_int("Enter top bound")
        if a > b:
            a, b = b, a
        l_o = deepcopy(self.__linked_list)
        self.__linked_list.del_from_a_to_b(a, b)
        l_n = deepcopy(self.__linked_list)
        self.__linked_list.motify_observers("Remove in range", l_o, l_n)