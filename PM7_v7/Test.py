from Option import Options
from Vaccination_Request_database import Vaccination_Request_datebase
from Vaccination_Requst import Vaccination_Request
import unittest
import copy

class TestVaccination_Request(unittest.TestCase):

    vr1 = ['1', 'Oleg', '1234567890', '0', '2020-12-30', '19:20', '20:20']
    vr2 = ['4', 'Ben', '1234567890', '1', '2020-03-11', '17:01', '20:30']
    vr3 = ['6', 'Anna', '9876543210', '2', '2021-06-4', '00:23', '00:40']

    def setUp(self) -> None:
        self.test_empty_lst = Vaccination_Request_datebase()
        self.data = copy.deepcopy(Vaccination_Request_datebase())
        self.data.fill_datebase()

    def test_add_elem(self):
        self.test_empty_lst.add_elem(TestVaccination_Request.vr1)
        a = self.test_empty_lst.database[0]
        self.assertEqual(self.test_empty_lst.database, [a])
        with self.assertRaises(TypeError):
            self.test_empty_lst.add_elem(Vaccination_Request())

    def test_find_by_id(self):
        self.assertFalse(self.data.find_by_id(-1))
        self.assertTrue(self.data.find_by_id(6))

    def test_find_all_F(self):
        self.assertFalse(self.data.find_all('2022'))
        self.assertTrue(self.data.find_all('2020'))

    def test_sort_date(self):
            a = [self.data.database[0], self.data.database[2], self.data.database[1]]
            self.data.sort_date(Options.sort(1))
            self.assertEqual(self.data.database, a)


    def test_del(self):
        ex = [self.data.database[1], self.data.database[2]]
        self.data.del_by_ident("1")
        self.assertEqual(self.data.database, ex)

    def test_edit_elem(self):
        self.data.edit_elem('1')
        a = [self.data.database[0], self.data.database[1], self.data.database[2]]
        self.assertEqual(self.data.database, a)

