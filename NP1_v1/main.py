def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()

def gener_bayte(arr, n):
    arr.append("0")
    arr.append("1")
    if n == 1:
        return
    i = 0
    while i < 2**n:
        if(i >= len(arr)):
            i = 0
        temp = arr[i]
        arr[i] += "0"
        arr.insert(i+1, temp + "1")
        i += 2

def get_n():
    print("Enter N:")
    n = int(input())
    return n

def search_11(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i].find("11") != -1:
            count += 1
    return count

arr = []
n = get_n()
gener_bayte(arr, n)
print_arr(arr)
count = search_11(arr)
print(count)