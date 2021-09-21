import random


def rand_arr(arr):
    a = enter_elem("Enter low bound")
    b = enter_elem("Enter top bound")
    if a > b:
        c = a
        a = b
        b = c
    for i in range(enter_size()):
        arr.append(random.randrange(a, b))


def exit_comand():
    ext = str(input("Stop program? Y/N "))
    if (ext == "Y"):
       exit()

def enter_or_rand(arr):
    comand = str(input("Enter array from keybord or random array? Random/Enter"))
    if (comand == "Random"):
        rand_arr(arr)
    elif (comand == "Enter"):
        enter_arr(arr)
    else:
        return enter_or_rand(arr)



def enter_size():
    size = enter_elem("Enter array size:")
    return size


def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()


def enter_elem(msg):
    try:
        val = int(input(msg))
    except ValueError:
        print("Taht was no valid value")
        return enter_elem()
    return val


def enter_arr(arr):
    for i in range(enter_size()):
        arr.append(enter_elem(f"Enter {i + 1} number:"))

def merg_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merg_sort(left)
        merg_sort(right)

        i = k = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1




def menu():
    while True:
        exit_comand()
        arr = []
        enter_or_rand(arr)
        print_arr(arr)
        merg_sort(arr)
        print_arr(arr)
menu()