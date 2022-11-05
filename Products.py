from random import choice
from Config import *
from time import *
import os


class products():

    def __init__(self):
        self.pro_name = None
        self.pro_availability = None
        self.pro_price = None
        self.pro_id = None
        self.pro_selling_price = None

########################################################
    def add_pro(self):

        # The info input process is as the following

        # The product name
        while True:
            try:
                self.pro_name = input("Please enter the product name ")
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break
        self.pro_name = self.pro_name.strip().lower()

        # The product price ((The original/pure price is in RWF))
        while True:
            try:
                self.pro_price = int(input(
                    "please input the original pure price of the product in ((RWF)) and in ((numbers only)): "))
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break
        # The product total price ((The price + profit margine together (selling price) in RWF))
        while True:
            try:
                self.pro_selling_price = int(input(
                    "please input the selling price of the product in ((RWF)) and in ((numbers only)): "))
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break
        # The product availability...

        while True:
            try:
                self.pro_availability = int(
                    input("Please enter the existing amount of the product in numbers: "))
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break

        # Now we store the used IDs (The emp_id variable) in a different file so that we make sure we give a new...
        # ... id everytime we add a product
        id_file = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products_id.txt", "a")
        with open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products_id.txt", "r") as f:
            last_line = int()
            for line in f:
                last_line = line
            new_id = int(last_line) + 1
        id_file.write(f"{new_id}\n")
        self.pro_id = new_id

        # Now we will store all those info in a file so that we can come back to it
        pro_file = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products.txt", "a")
        content = str(
            f"#ID#{self.pro_id}\n{self.pro_name}\n{self.pro_price}\n{self.pro_selling_price}\n{self.pro_availability}\n")
        pro_file.write(f"{content}\n")
        pro_file.close()

        # Now we are going to show the new product info and welcome him to the system
        print(f"The product with the name {self.pro_name}\
has been added succefully with a amount of {self.pro_availability}")

        test_file = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products.txt", "r")
        test_list = test_file.readlines()
        return test_list
########################################################################

    def delete_pro(self):
        # In order to delete a customer, and because we prefere to keep his place/lines in the file so that we
        # don't have any disturptions in the lines number and make it easy for ourselves, we decided to delete ..
        # customers by setting the places/lines of their info in the file as "NONE".

        # Create the list from the file...
        pro_file_r = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products.txt", "r")
        while True:
            try:
                self.pro_id = int(
                    input("Please enter the id of the product you want to delete: "))
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break
        list_of_lines = pro_file_r.readlines()

        # Define the line number of the id
        line_number = int(0)
        temp_id = int()
        for line in list_of_lines:
            line_number += 1
            if line.startswith("#"):
                temp_id = line[4]
                temp_id = int(temp_id)
                if temp_id == self.pro_id:
                    break
        # write The NoNeS instead of the product deatils
        n = int()
        for i in range(4):
            list_of_lines[line_number+n] = "None\n"
            n += 1

        # print the list agian in the file after editing it...
        pro_file_w = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products.txt", "w")
        pro_file_w.writelines(list_of_lines)
        pro_file_w.close()

        print("The product has been dleted suceffully...")
#################################################################################

    def edit_pro(self):
        global pro_edit_list

        # Create the list...
        pro_file_r = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products.txt", "r")
        list_of_lines = pro_file_r.readlines()

        # Define the line number of the id
        while True:
            try:
                self.pro_id = int(
                    input("Please enter the id of the product you want to edit: "))
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break
        line_number = int(0)
        temp_id = int()
        for line in list_of_lines:
            line_number += 1
            if line.startswith("#"):
                temp_id = line[4]
                temp_id = int(temp_id)
                if temp_id == self.pro_id:
                    break

        edit_choice = int()
        while edit_choice != 5:
            # choose which line to edit...
            print("Please choose which piece of info you want to edit...")
            q = int()
            for i in pro_edit_list[:]:
                q += 1
                print(f"{q}. {i}")
            while True:
                try:
                    edit_choice = int(input("Please enter the choice number here: "))
                except ValueError:
                    print("incorrect input. Try again: ")
                else:
                    break
            if edit_choice == 1:
                # edit name
                while True:
                    try:
                        self.pro_name = input(
                            "Please input the product's new name ")
                    except ValueError:
                        print("Invalid input. Try again: ")
                    else:
                        break
                list_of_lines[line_number] = (f"{self.pro_name}\n")
                print("name has been updated succefully")
                print("What else you want to edit?...")
            elif edit_choice == 2:
                # edit original price
                while True:
                    try:
                        self.pro_price = int(
                            input("Please input the products's new price "))
                    except ValueError:
                        print("Invalid input. Try again: ")
                    else:
                        break
                list_of_lines[line_number+1] = (f"{self.pro_price}\n")
                print("price has been updted succefully")
                print("What else you want to edit?...")

            elif edit_choice == 3:
                # edit availability
                while True:
                    try:
                        self.pro_availability = input(
                            "Please input the product's new amount ")
                    except ValueError:
                        print("Invalid input. Try again: ")
                    else:
                        break
                list_of_lines[line_number+2] = (f"{self.pro_availability}\n")
                print("amount has been updated succefully")
                print("What else you want to edit?...")

            elif edit_choice == 4:
                # edit selling price
                while True:
                    try:
                        self.pro_selling_price = input(
                            "Please input the products's new price ")
                    except ValueError:
                        print("Invalid input. Try again: ")
                    else:
                        break
                list_of_lines[line_number+1] = (f"{self.pro_selling_price}\n")
                print("selling price has been updated succefully")
                print("What else you want to edit?...")

        else:
            pass

        # print the list agian in the file after editing it...
        cus_file_w = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products.txt", "w")
        cus_file_w.writelines(list_of_lines)
        cus_file_w.close()

#########################################################################
    def order_pro(self):

        # in order to order a product (which the pharmacy has no more left in the stocks),
        # we have to identify what we want to order (the product) and the amount we want
        # to order, then we wait for some time until t has been ordered.

        # First thing we ask, which product you want to order...
        while True:
            try:
                self.pro_id = int(
                    input("Please enter the ID of the product you want to order: "))
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break

        while True:
            try:
                self.amount = int(
                    input("Please enter the amount that you want to order: "))
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break

         # Create the editing list...
        pro_file_r = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products.txt", "r")
        list_of_lines = pro_file_r.readlines()

        # Define the line number of the id
        line_number = int(0)
        temp_id = int()
        for line in list_of_lines:
            line_number += 1
            if line.startswith("#"):
                temp_id = line[4]
                temp_id = int(temp_id)
                if temp_id == self.pro_id:
                    # z = z-1
                    break

        # Add the new products in the list first and prepare it to be in the files records.

        self.amount = int(self.amount)
        self.pro_availability = list_of_lines[line_number+2]

        self.pro_availability = int(self.pro_availability)

        list_of_lines[line_number +2] = (f"{self.amount + self.pro_availability}\n")

        # wait sometime for the order
        print("Please wait a few moments untill we recieve the order")
        sleep(10)

        # Write the list in the files records...
        cus_file_w = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products.txt", "w")
        cus_file_w.writelines(list_of_lines)
        cus_file_w.close()

        print("Product has been updated succeffully")
###################################################################

    def show_avilability(self):

        # Create the list / Read the file...
        pro_file_r = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products.txt", "r")
        list_of_lines = pro_file_r.readlines()

        # count the number of lines so that we know how many products we have to loop in
        x = int()
        for i in list_of_lines:
            x += 1
        x = int(x/6)

        # Loop in the lis of product name and amount and add it to the list so that we can print the report,
        n1 = int()
        n2 = int()
        for i in range(x):
            if (list_of_lines[n2+4][:-1]) == '0':
                print(
                    f"The product {list_of_lines[n1+1][:-1].strip()} is not available and need to be ordered")
                n1 += 6
                n2 += 6
            elif (list_of_lines[n2+4][:-1]) == 'None':
                n1 += 6
                n2 += 6
                pass
            else:
                print(
                    f"The product {list_of_lines[n1+1][:-1].strip()} is available with an amount of {list_of_lines[n2+4][:-1].strip()}")
                n1 += 6
                n2 += 6


##############################################
