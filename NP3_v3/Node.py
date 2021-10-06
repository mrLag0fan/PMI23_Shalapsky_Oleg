
class Node:

    def __init__(self, data_ = 0, node = None):
        self.data = data_
        self.previous = node
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data_):
        self.__data = data_

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, node):
        self.__previous = node
