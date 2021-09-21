

def exit_comand():
    ext = str(input("Stop program? Y/N "))
    if (ext == "Y"):
       exit()

def enter_int(mesg):
    try:
        n = int(input(mesg))
    except ValueError:
        print("Your velue isn't valid")
        return enter_int(mesg)
    return n


def enter_row_elem(par_i, m):
    row = []

    for i in  range(m):
        row.append(enter_int(f"Enter [{par_i}][{i}] element"))
    return row

def add_rows(culumns, rows, matr1):
    for i in range(rows):
        matr1.append(enter_row_elem(i, culumns))

def suma(matr1, columns, i_, j_):
    sum = 0
    i = columns-1
    while i >= 0:
        if (matr1[i][j_] > 0 and i <= i_):
            sum += matr1[i][j_]
        i -= 1
    return sum


def create_B(matr1, matr2, row, columns):
    for i in range(row):
        matr2.append([])
        for j in range(columns):
            matr2[i].append(suma(matr1, matr2, row, columns, i, j))

def menu():
    while True:
        exit_comand()
        matr1 = []
        matr2 = []
        rows = enter_int("Enter rows count then push \"Enter\": ")
        culmns = enter_int("Enter columns count then push \"Enter\": ")
        add_rows(culmns, rows, matr1)
        print(matr1)
        create_B(matr1, matr2, rows, culmns)
        print(matr2)
menu()