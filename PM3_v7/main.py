import menu

while True:
    menu.exit_comand()
    db = menu.Vaccination_Request_datebase()
    db.fill_datebase()
    menu.menu(db)

