import unittest

from Config import *
import os
# import Main_menu


# Our application is mainly based on storing data on files and calling it again,
# So we decided to make our application a way to check if those data are stored correctly or not
# And this will happen by testing the specific portions of codes (individually) that are responsible for
# storing and calling the data before we use it in our classes and methods.

########################################################################
# Class 04 testes
# #######################################################################

# 3
def add_pro(pro_id, pro_name, pro_price, pro_selling_price, pro_availability):
    # Make the test file empty
    delete = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "w")
    delete.write("")

    # Now we will store all those info in a file so that we can come back to it
    pro_file = open(
        f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "a")
    content = str(
        f"#ID#{pro_id}\n{pro_name}\n{pro_price}\n{pro_selling_price}\n{pro_availability}\n")
    pro_file.write(f"{content}\n")
    pro_file.close()
    test_file = open(
        f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "r")
    test_list = test_file.readlines()
    test_file.close()
    return test_list

#########################


def cus_identify(cus_id):

    # Here we should look for the customer who is a part of the selling operation so that we can
    # record the operation with his name in the system, and if he is not in the system we add him first.

    add_pro("1", "Ahmed", "1000", "1500", "20")

    new_list_of_lines = [1, 2, 3]
    # See if the customer is a new one or not...

    # cus_id = input("Please input the Id of the current buyer/customer: ")
    if cus_id not in new_list_of_lines[:]:
        print("The id you entered is not in our system......repeating the process.....")
        pass
    else:
        customer_id = cus_id
        return customer_id
########################################


order_list = list()


def buy_list():
    while True:
        try:
            pro_id = int(
                input("Please enter the id of the product you want to buy: "))
        except ValueError:
            print("Invalid input. Try again: ")
        else:
            break
    while True:
        try:
            order_amount = int(
                input("Please enter the quantity you want to order: "))
        except ValueError:
            print("Invalid input. Try again: ")
        else:
            break
    order_list.append(pro_id)
    order_list.append(order_amount)

    choice = input("Do you want to buy sth else?(yes/no) ")
    if "y" in choice or "Y" in choice:
        buy_list()
    elif "n" in choice or "N" in choice:
        return order_list
    return order_list
##########################################


def pay(buy_price, t_profit):
    profits_file_a = open(
        f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "a")
    income_file_a = open(
        f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "a")

    profits_file_a.write(f"{t_profit}\n")
    income_file_a.write(f"{buy_price}\n")
    print("Paid Succefully")
    orders_file_r = open(
        f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "r")
    file_r_list = orders_file_r.readlines()

    return file_r_list
###########################################


def feedback(feed):
    while True:
        try:
            if 0 <= feed <= 5:
                pass
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Try again: ")
            feed = "failed"
            break
        else:
            break
    return feed
##########################################


class test_portions3(unittest.TestCase):
    def test_customer_identify(self):
        self.assertIn(cus_identify(1), [1, 2, 3])

    def test_buy_list(self):
        self.assertEqual(buy_list(), [1, 2, 3, 4])

    def test_paid(self):
        self.assertIn("1000\n", pay(1000, 100))
        self.assertIn("100\n", pay(1000, 100))

    def test_feedback01(self):
        self.assertEqual(feedback(1), 1)
        self.assertEqual(feedback(1.42), 1.42)
        self.assertEqual(feedback(0), 0)

    def test_feedback02(self):
        self.assertEqual(feedback(6), "failed")
        self.assertEqual(feedback(-1), "failed")


if __name__ == "__main__":
    unittest.main()
