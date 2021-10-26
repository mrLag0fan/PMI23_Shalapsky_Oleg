from abc import ABC, abstractmethod

class Logger:
    @staticmethod
    def log(msg, l_o, l_n):
        file_w = open("out", "a+")
        file_w.writelines(msg + ': [' + str(l_o) + '], [' + str(l_n) + ']')
        print(msg + ': [' + str(l_o) + '], [' + str(l_n))
        file_w.writelines('\n')
        file_w.close()

class ObserverInter(ABC):
    def update(self, msg, l_o, l_n):
        pass

class Observer(ObserverInter):
    def update(self, msg, l_o, l_n):
        Logger.log(msg, l_o, l_n)

class Event:
    def __init__(self, name, old, new):
        self.__name = name
        self.__old = old
        self.__new = new

    @property
    def name(self):
        return self.__name
    @property
    def old(self):
        return self.__old
    @property
    def new(self):
        return self.__new