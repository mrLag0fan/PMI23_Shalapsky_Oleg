import menu
import copy
from Vaccination_Request_database import Vaccination_Request_datebase
from  validdate import *

db = Vaccination_Request_datebase()
db.fill_datebase()
print(db)
menu.menu(db, [copy.deepcopy(db)])


