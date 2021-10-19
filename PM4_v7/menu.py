from Option import Options
from Vaccination_Request_database import Vaccination_Request_datebase
from Vaccination_Requst import Vaccination_Request

menu_options = {
    1: "Add element",
    2: "Delete element",
    3: "Edit",
    4: "Sort",
    5: "Print",
    6: "Find",
    7: "Exit"
}

def print_menu(options):
    for key in options.keys():
        print (key, '--', options[key] )

def options(option, linked_list):
    function = Options(linked_list)
    return {
        "1": function.option1,
        "2": function.option2,
        "3": function.option3,
        "4": function.option4,
        "5": function.option5,
        "6": function.option6,
        "7": function.option7
    }.get(option)

def start(method, db):
    if method:
        return method()
    else:
        print("Choose correct option")
        menu(db)

def menu(db):
    print_menu(menu_options)
    option = input(f"Enter option between 1 and {len(menu_options)}: ")
    method = options(option, db)
    start(method, db)
    menu(db)