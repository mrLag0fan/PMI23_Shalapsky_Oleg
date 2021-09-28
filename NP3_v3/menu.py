from Linked_List_ import LinkedList
from Node import Node
import random

def exit_comand():
    ext = str(input("Stop program? Y/N "))
    if (ext.upper() == "Y"):
       exit()
    elif ext.upper() == "N":
        return
    else:
        return exit_comand()

def enter_int(mesg):
    try:
        return abs(int(input(mesg)))
    except ValueError:
        print("Your velue isn't valid")
        return enter_int(mesg)

def enter_or_rand(linked_list):
    comand = str(input("Enter array from keybord or random array? RANDOM/ENTER"))
    if (comand.upper() == "RANDOM"):
        linked_list.head = Node(random.randint(0, 100))
        linked_list.random_linked_list()
    elif (comand.upper() == "ENTER"):
        linked_list.head = Node(input("Enter head element"))
        linked_list.enter_list()
    else:
        return enter_or_rand(linked_list)

def menu(linked_list):
    while True:
        exit_comand()
        k = enter_int("Enter k: ")
        enter_or_rand(linked_list)
        linked_list.move(k)
