from Config import *
import os


class customer():

    def __init__(self):
        self.cus_name = None  # Input
        self.cus_national_id = None  # Input
        self.cus_age = None  # Input
        self.cus_id = None  # auto generated
        self.cus_health = None  # Input from list
        self.cus_sex = None  # Input from list
##########################################################

    def add_customer(self):
        global cus_health_list, sex_list

        # The info input process is as the following

        # First ### The Normal input info
        x = int()
        y = int()
        self.cus_id = int()
        print("Please use the customer official information from the official documents \n")
        while True:
            try:
                self.cus_name = input(
                    "Please input the customer's full name: ")
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break

        while True:
            try:
                self.cus_national_id = input(
                    "Please input the customer's national id: ")
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break

        while True:
            try:
                self.cus_age = int(input("Please input the customer's age: "))
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break

        # Second ### The input from list info
        print(
            "Do you have any chronic diseases from the following that you should tell us ?")
        for i in cus_health_list[0:16]:
            y += 1
            print(f"{y}) {i}")

        while True:
            try:
                self.cus_health = int(
                    input("Please enter the choice number: "))
            except ValueError:
                print("Invalid input. Try again: ")
            except IndexError:
                print("Invalid input. Try again: ")
            else:
                break

        self.cus_health = cus_health_list[self.cus_health - 1]

        x = 0
        for i in sex_list:
            x += 1
            print(f"{x}) {i}")

        while True:
            try:
                self.cus_sex = int(input("Please input the choice number: "))
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break

        self.cus_sex = sex_list[int(self.cus_sex)-1]

        # Now we store the used IDs (The emp_id variable) in a different file so that we make sure we give a new...
        # ... id everytime we add someone
        id_file = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_customers_id.txt", "a")
        with open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_customers_id.txt", "r") as f:
            last_line = int()
            for line in f:
                last_line = line
            new_id = int(last_line) + 1
        id_file.write(f"{new_id}\n")
        self.cus_id = new_id

        # Now we will store all those info in a file so that we can come back to it
        cus_file = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_customers.txt", "a")
        content = str(
            f"#ID#{self.cus_id}\n{self.cus_name}\n{self.cus_national_id}\n{self.cus_health}\n{self.cus_sex}\n{self.cus_age}\n")
        cus_file.write(f"{content}\n")
        cus_file.close()

        # Now we shall print the "Added suceffullly message"
        print(
            f"The customer with name {self.cus_name} and ID {self.cus_id} has been added succefully")

        # for the testing
        file_read = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_customers.txt", "r")
        list_of_lines = file_read.readlines()

        return list_of_lines
################################################################

    def delete_customer(self):

        # In order to delete a customer, and because we prefere to keep his place/lines in the file so that we
        # don't have any disturptions in the lines number and make it easy for ourselves, we decided to delete ..
        # customers by setting the places/lines of their info in the file as "NONE".

        # Create the list...
        cus_file_r = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_customers.txt", "r")

        while True:
            try:
                self.cus_id = int(
                    input("Please enter the id of the customer you want to delete:  "))
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break

        list_of_lines = cus_file_r.readlines()

        # Define the line number of the id
        line_number = int(0)
        temp_id = int()
        for line in list_of_lines:
            line_number += 1
            if line.startswith("#"):

                temp_id = line[4]
                temp_id = int(temp_id)
                if temp_id == self.cus_id:
                    # z = z-1
                    break
        # write The NoNeS instead of the customer deatils
        n = int()
        for i in range(5):
            list_of_lines[line_number+n] = "None\n"
            n += 1

        # print the list agian in the file after editing it...
        cus_file_w = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_customers.txt", "w")
        cus_file_w.writelines(list_of_lines)
        cus_file_w.close()

        print("The customer has been dleted suceffully...")
        cus_file_r = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_customers.txt", "r")
        list_of = cus_file_r.readlines()
        return list_of[int(self.cus_id)*7-3]
#####################################################################

    def edit_customer(self):

        # Create the list...
        cus_file_r = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_customers.txt", "r")
        list_of_lines = cus_file_r.readlines()

        # Define the line number of the id
        while True:
            try:
                self.cus_id = int(
                    input("Please enter the id of the customer you want to edit: "))
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
                if temp_id == self.cus_id:
                    # z = z-1
                    break

        # What to edit
        edit_choice = int()
        while edit_choice != 5:
            # choose which line to edit...
            print("Please choose which piece of info you want to edit...")
            q = int()
            for i in cus_edit_list:
                q += 1
                print(f"{q}. {i}")
            edit_choice = int(input("Please enter the choice number here: "))

            if edit_choice == 1:
                # edit name
                while True:
                    try:
                        self.cus_name = input(
                            "Please input the customer's new name ")
                    except ValueError:
                        print("Invalid input. Try again: ")
                    else:
                        break
                list_of_lines[line_number] = (f"{self.cus_name}\n")
                print("name has been added succefully")
                print("What else you want to edit?...")
            elif edit_choice == 2:
                # edit national id
                while True:
                    try:
                        self.cus_national_id = input(
                            "Please input the customer's new age ")
                    except ValueError:
                        print("Invalid input. Try again: ")
                    else:
                        break

                list_of_lines[line_number+1] = (f"{self.cus_national_id}\n")
                print("national has been added succefully")
                print("What else you want to edit?...")
            elif edit_choice == 3:
                # edit health
                b = int()
                for i in cus_health_list[0:15]:
                    b += 1
                    print(f"{b}) {i}")

                while True:
                    try:
                        self.cus_health = int(
                            input("Please enter the new health status choice number: "))
                    except ValueError:
                        print("Invalid input. Try again: ")
                    else:
                        break
                self.cus_health = cus_health_list[self.cus_health]
                list_of_lines[line_number+2] = (f"{self.cus_health}\n")
                print("health status has been added succefully")
                print("What else you want to edit?...")

            elif edit_choice == 4:
                # edit age
                self.cus_age = input("Please input the customer's new age ")
                list_of_lines[line_number+4] = (f"{self.cus_age}\n")
                print("Age has been added succefully")
                print("What else you want to edit?...")
        else:
            pass

        # print the list agian in the file after editing it...
        cus_file_w = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_customers.txt", "w")
        cus_file_w.writelines(list_of_lines)
        cus_file_w.close()
####################################################

    def show_customers(self):

        # Create the list...
        cus_file_r = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_customers.txt", "r")
        list_of_lines = cus_file_r.readlines()

        c = int(1)
        for lin in list_of_lines:
            c += 1

        l = int(1)
        for i in range(999):
            c2 = int()
            c2 += 1
            print(f"Customer Number {c2}")
            for line in list_of_lines:
                print(line)
                l += 1
            if l == c:
                break
        return list_of_lines



