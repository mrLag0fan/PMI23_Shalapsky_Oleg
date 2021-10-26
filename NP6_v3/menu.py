
from Options import Options




input_options = {
    1: "Enter from keyboard",
    2: "Random list",
    3: "From file",
    4: "Exit"
}

menu_options = {
    1: "Add element",
    2: "Delete element",
    3: "Move",
    4: "Print",
    5: "Delete form a to b",
    6: "Return"
}

def print_menu(options):
    for key in options.keys():
        print (key, '--', options[key] )

def input_type(option, linked_list):
    function = Options(linked_list)
    return {
        "1": function.option1,
        "2": function.option2,
        "3": function.option9,
        "4": function.option7
    }.get(option)

def options(option, linked_list):
    function = Options(linked_list)
    return {
        "1": function.option3,
        "2": function.option4,
        "3": function.option5,
        "4": function.option6,
        "5": function.option10,
        "6": function.option8
    }.get(option)

def start(method, linked_list):
    if method:
        return method()
    else:
        print("Choose correct option")
        menu(linked_list)



def menu(linked_list):
    print_menu(input_options)
    input_type_ = input(f"Enter option between 1 and {len(input_options)}: ")
    input_ = input_type(input_type_, linked_list)
    if start(input_, linked_list) == -1:
        print("Your value isn't valid")
        menu(linked_list)
    while True:
        print_menu(menu_options)
        option = input(f"Enter option between 1 and {len(menu_options)}: ")
        method = options(option, linked_list)
        if start(method, linked_list) == -1:
            break
    linked_list.print(linked_list.head)
    menu(linked_list)
