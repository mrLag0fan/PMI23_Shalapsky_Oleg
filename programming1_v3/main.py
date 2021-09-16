import random

def enter_size():
    print("Enter array size:")
    size = enter_elem()
    return size

def rand_arr(arr):
    for i in range(enter_size()):
        arr.append(random.randrange(0, 100))

def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()

def enter_elem():
    try:
        val = int(input())
    except ValueError:
        print("Taht was no valid value")
        return enter_elem()
    return val

def enter_arr(arr):
    for i in range(enter_size()):
        print(f"Enter {i+1} number:")
        arr.append(enter_elem())

def move(arr, k):
    for i in range(k):
        arr.append(arr.pop(0))



array = []
#enter_arr(array)
rand_arr(array)
print_arr(array)
move(array, 5)
print_arr(array)



