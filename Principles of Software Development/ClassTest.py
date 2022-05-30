import unittest
from User import User
from Activity import Activity
from Bill import Bill
import datetime

class ClassTest(unittest.TestCase):

    def test_User(self):
        user = User("Arthur", "1234")
        self.assertEqual(user.getUser(), "Arthur")
        self.assertEqual(user.getPassword(), "1234")
        self.assertEqual(user.summary(), ["Arthur", "1234"])

        user.setUser("John")
        self.assertEqual(user.getUser(), "John")
        self.assertEqual(user.summary(), ["John", "1234"])
        user.setPassword("4321")
        self.assertEqual(user.getPassword(), "4321")
        self.assertEqual(user.summary(), ["John", "4321"])

    def test_Activity(self):
        activity = Activity("Dinner", "with friends", ["Arthur", "John"])
        self.assertEqual(activity.getTitle(), "Dinner")
        self.assertEqual(activity.getDescription(), "with friends")
        self.assertEqual(activity.getUserList(), ["Arthur", "John"])
        self.assertEqual(activity.summary(), ["Dinner", "with friends", ["Arthur", "John"]])

        activity.setTitle("Lunch")
        self.assertEqual(activity.getTitle(), "Lunch")
        self.assertEqual(activity.summary(), ["Lunch", "with friends", ["Arthur", "John"]])
        activity.setDescription("with family")
        self.assertEqual(activity.getDescription(), "with family")
        self.assertEqual(activity.summary(), ["Lunch", "with family", ["Arthur", "John"]])
        activity.setUserList(["Arthur", "John", "Paul"])
        self.assertEqual(activity.getUserList(), ["Arthur", "John", "Paul"])
        self.assertEqual(activity.summary(), ["Lunch", "with family", ["Arthur", "John", "Paul"]])

    def test_Bill(self):
        bill = Bill("Pizza", 7, "Arthur", datetime.date(2022, 3, 16), ["Arthur", "John"])
        self.assertEqual(bill.getTitle(), "Pizza")
        self.assertEqual(bill.getExpense(), 7)
        self.assertEqual(bill.getPayerUser(), "Arthur")
        self.assertEqual(bill.getDate(), datetime.date(2022, 3, 16))
        self.assertEqual(bill.getUserList(), ["Arthur", "John"])
        self.assertEqual(bill.summary(), ["Pizza", 7, "Arthur", datetime.date(2022, 3, 16), ["Arthur", "John"]])

        bill.setTitle("Salad")
        self.assertEqual(bill.getTitle(), "Salad")
        self.assertEqual(bill.summary(), ["Salad", 7, "Arthur", datetime.date(2022, 3, 16), ["Arthur", "John"]])
        bill.setExpense(10)
        self.assertEqual(bill.getExpense(), 10)
        self.assertEqual(bill.summary(), ["Salad", 10, "Arthur", datetime.date(2022, 3, 16), ["Arthur", "John"]])
        bill.setPayerUser("John")
        self.assertEqual(bill.getPayerUser(), "John")
        self.assertEqual(bill.summary(), ["Salad", 10, "John", datetime.date(2022, 3, 16), ["Arthur", "John"]])
        bill.setDate(datetime.date(2022, 3, 17))
        self.assertEqual(bill.getDate(), datetime.date(2022, 3, 17))
        self.assertEqual(bill.summary(), ["Salad", 10, "John", datetime.date(2022, 3, 17), ["Arthur", "John"]])
        bill.setUserList(["Arthur", "John", "Paul"])
        self.assertEqual(bill.getUserList(), ["Arthur", "John", "Paul"])
        self.assertEqual(bill.summary(), ["Salad", 10, "John", datetime.date(2022, 3, 17), ["Arthur", "John", "Paul"]])




