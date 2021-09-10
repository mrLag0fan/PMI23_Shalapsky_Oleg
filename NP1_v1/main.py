
def enter_n():
    try:
        n = int(input("Enter your n:"))
    except ValueError:
        print("Your n isn't valid")
        return enter_n()
    return n

def serch(n):
    count = 0
    for i in range(2**n):
        if str(bin(i)).find("11") == -1:
            count += 1
    print(f"Numbers with contains 11: {count}")

n = enter_n()
serch(n)