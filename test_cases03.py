import unittest
from Config import *
import os
# import Main_menu


# Our application is mainly based on storing data on files and calling it again,
# So we decided to make our application a way to check if those data are stored correctly or not
# And this will happen by testing the specific portions of codes (individually) that are responsible for
# storing and calling the data before we use it in our classes and methods.

########################################################################
# Class 03 testes
# #######################################################################

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
###########################################


def delete_pro():
    # Make the test file empty
    delete = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "w")
    delete.write("")

    add_pro("1", "Ahmed", "1000", "1500", "20")
    test_file = open(
        f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "r")
    test_list = test_file.readlines()
    # write The NoNeS instead of the product deatils
    n = int()
    for i in range(4):
        test_list[1+n] = "None\n"
        n += 1

    # print the list agian in the file after editing it...
    pro_file_w = open(
        f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "w")
    pro_file_w.writelines(test_list)
    pro_file_w.close()
    return test_list
#################################################


def edit():
    # Make the test file empty
    delete = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "w")
    delete.write("")

    add_pro("1", "Ahmed", "1000", "1500", "20")
    test_file = open(
        f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "r")
    test_list = test_file.readlines()

    edit_choice = int()
    while edit_choice != 5:
        # choose which line to edit...
        print("Please choose which piece of info you want to edit...")
        q = int()
        for i in pro_edit_list:
            q += 1
            print(f"{q}. {i}")
        edit_choice = int(input("Please enter the choice number here: "))

        if edit_choice == 1:
            # edit name
            while True:
                try:
                    pro_name = input("Please input the product's new name ")
                except ValueError:
                    print("Invalid input. Try again: ")
                else:
                    break
            test_list[int(edit_choice)] = (f"{pro_name}\n")
            print("name has been updated succefully")
            print("What else you want to edit?...")
        elif edit_choice == 2:
            # edit original price
            while True:
                try:
                    pro_price = int(
                        input("Please input the products's new price "))
                except ValueError:
                    print("Invalid input. Try again: ")
                else:
                    break
            test_list[int(edit_choice)] = (f"{pro_price}\n")
            print("price has been updted succefully")
            print("What else you want to edit?...")

        elif edit_choice == 3:
            # edit availability
            while True:
                try:
                    pro_availability = input(
                        "Please input the product's new amount ")
                except ValueError:
                    print("Invalid input. Try again: ")
                else:
                    break
            test_list[int(edit_choice)] = (f"{pro_availability}\n")
            print("amount has been updated succefully")
            print("What else you want to edit?...")

        elif edit_choice == 4:
            # edit selling price
            while True:
                try:
                    pro_selling_price = input(
                        "Please input the products's new price ")
                except ValueError:
                    print("Invalid input. Try again: ")
                else:
                    break
            test_list[int(edit_choice)] = (f"{pro_selling_price}\n")
            print("selling price has been updted succefully")
            print("What else you want to edit?...")
    else:
        pass

    test_file.close()
    return test_list[1:4]
###############################################


def show_availability():
    add_pro("1", "Ahmed", "1000", "1500", "20")
    test_file = open(
        f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "r")
    test_list = test_file.readlines()
    # Loop in the lis of product name and amount and add it to the list so that we can print the report,
    n1 = int()
    n2 = int()
    x = str()
    for i in range(1):
        if (test_list[n2+4][:-1]) == '0':
            print(
                f"The product {test_list[n1+1][:-1].strip()} is not available and need to be ordered")
            x = "Done"

        elif (test_list[n2+4][:-1]) == 'None':
            print(
                f"The product {test_list[n1+1][:-1].strip()} is not in our system")
            x = "Done"
        else:
            x = "Done"
            print(
                f"The product {test_list[n1+1][:-1].strip()} is available with an amount of {test_list[n2+4][:-1].strip()}")
        return x
################################################


def order_pro(amount):
    # Make the test file empty
    delete = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "w")
    delete.write("")

    # while True:
    #     try:
    #         amount = int(input("Please enter the amount that you want to order: "))
    #     except ValueError:
    #         print("Invalid input. Try again: ")
    #     else:
    #         break
    add_pro("1", "Ahmed", "1000", "1500", "20")
    # Create the editing list...
    pro_file_r = open(
        f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "r")
    list_of_lines = pro_file_r.readlines()

    # Add the new products in the list first and prepare it to be in the files records.
    amount = int(amount)

    pro_availability = list_of_lines[2+2]

    pro_availability = int(pro_availability)

    list_of_lines[2+2] = (f"{amount + pro_availability}\n")

    # Write the list in the files records...
    cus_file_w = open(
        f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "w")
    cus_file_w.writelines(list_of_lines)
    cus_file_w.close()

    print("Product has been updated succeffully")

    x = f"{amount + pro_availability}"
    return x
################################################


class test_portions3(unittest.TestCase):
    def test_add_product(self):
        # Make the test file empty
        delete = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "w")
        delete.write("")
        self.assertEqual(add_pro("1", "Ahmed", "1000", "1500", "20"), [
                         "#ID#1\n", "Ahmed\n", "1000\n", "1500\n", "20\n", "\n"])

    def test_delete(self):
        self.assertEqual(delete_pro()[1], "None\n")
        self.assertEqual(delete_pro()[2], "None\n")
        self.assertEqual(delete_pro()[3], "None\n")
        self.assertEqual(delete_pro()[4], "None\n")

    def test_edit(self):
        the_edit = input(
            "Please put the new word or number that you will replace here: ")
        self.assertIn(f"{the_edit}\n", edit())

    def test_show_avaliability(self):
        self.assertEqual(show_availability(), "Done")

    def test_order(self):
        self.assertEqual(order_pro(5), "25")


if __name__ == "__main__":
    unittest.main()
