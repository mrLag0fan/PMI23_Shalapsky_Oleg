
import menu

class Options():

    def __init__(self, linked_list):
        self.__linked_list = linked_list

    def option1(self):
        n = menu.enter_int("Enter count of elements")
        if n <= 0:
            return -1
        self.__linked_list.enter_list(n)

    def option2(self):
        n = menu.enter_int("Enter count of elements")
        if n <= 0:
            return -1
        a = menu.enter_int("Enter low bound")
        b = menu.enter_int("Enter top bound")
        if a > b:
            a, b = b, a
        self.__linked_list.random_linked_list(n, a, b)

    def option3(self):
        k = menu.enter_int("Enter pos")
        if not self.__linked_list.is_position_valid(k):
            return
        self.__linked_list.add_element(menu.enter_int("Enter date: "), k)

    def option4(self):
        k = menu.enter_int("Enter pos")
        if not self.__linked_list.is_position_valid(k):
            return
        self.__linked_list.del_elem(k)

    def option5(self):
        self.__linked_list.move(menu.enter_int("Enter k"))

    def option6(self):
        self.__linked_list.print(self.__linked_list.head)

    def option7(self):
        exit()

    def option8(self):
        return -1
