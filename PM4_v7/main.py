import menu
from Vaccination_Request_database import Vaccination_Request_datebase
from  validdate import *

db = Vaccination_Request_datebase()
db.fill_datebase()
menu.menu(db)


