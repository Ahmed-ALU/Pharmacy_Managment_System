from Config import *
import random
import os


class employee():

    def __init__(self):
        self.emp_name = None
        self.emp_national_id = None
        self.emp_id = None
        self.emp_rank = None
        self.emp_sex = None
        self.emp_username = None
################################################

    def add_emp(self):
        while True:
            global emp_rank_list, sex_list

            # The info input process is as the following
            x = int()
            y = int()
            self.emp_id = int()
            print(
                "Please use the employer official information from the official documents \n")

            while True:
                try:
                    self.emp_name = input(
                        "Please input the employee's full name: ")
                except ValueError:
                    print("Invalid input. Try again: ")
                else:
                    break

            while True:
                try:
                    self.emp_national_id = input(
                        "Please input the employee's national id: ")
                except ValueError:
                    print("Invalid input. Try again: ")
                else:
                    break

            # self.emp_id += 1
            for i in emp_rank_list[0:7]:
                y += 1
                print(f"{y}) {i}")

            while True:
                try:
                    self.emp_rank = int(
                        input("Please input the choice number: "))
                except ValueError:
                    print("Invalid input. Try again: ")
                else:
                    break
            self.emp_rank = str(emp_rank_list[self.emp_rank])
            y = 0
            for i in sex_list:
                y += 1
                print(f"{y}) {i}")

            while True:
                try:
                    self.emp_sex = int(
                        input("Please input the choice number: "))
                except ValueError:
                    print("Invalid input. Try again: ")
                else:
                    break

            self.emp_sex = str(sex_list[self.emp_sex-1])
            self.emp_username = str(
                f"{self.emp_name[0:6]}{random.randint(1000, 9999)}")
            # We finished taking the employer info from the hr manager by now

            # Now we store the used IDs (The emp_id variable) in a different file so that we make sure we give a new...
            # ... id everytime we add someone
            id_file = open(
                f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_employers_id.txt", "a")
            with open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_employers_id.txt", "r") as f:
                last_line = int()
                for line in f:
                    last_line = line
                new_id = int(last_line) + 1
            id_file.write(f"{new_id}\n")
            self.emp_id = new_id

            # Now we add that employee to the attendence file so that we can record his attendence depending on his id:
            log_file = open(
                f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_employers_attendence.txt", "a")
            log_file.write(f"{self.emp_id}\n{0}\n\n")

            # Now we will store all those info in a file so that we can come back to it
            emp_file = open(
                f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_employers.txt", "a")
            content = str(
                f"#ID#{self.emp_id}\n{self.emp_name}\n{self.emp_national_id}\n{self.emp_rank}\n{self.emp_sex}\n{self.emp_username}\n")
            emp_file.write(f"{content}\n")
            emp_file.close()

            # Now we are going to show the new employer info and welcome him to the system
            print(
                f"The employer with the name {self.emp_name} has been added succefully with a user name of {self.emp_username} ")
            return self.emp_name
#########################################################

    def delete_emp(self):
        # In order to delete an employee from our local database,
        #  we decided to only mark it as "retired" in the rank, because we are not
        # using an online database and deleting data may cause some interuption

        # Getting the id of the intended employee
        emp_file_r = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_employers.txt", "r")
        while True:
            try:
                self.emp_id = int(
                    input("Please enter the id of the user/employee you want to delete:  "))
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break

        # Write the Retired word in its right place in the file
        list_of_lines = emp_file_r.readlines()
        if self.emp_id == 1:
            list_of_lines[3] = f"{emp_rank_list[7]}\n"
        else:
            list_of_lines[3+((self.emp_id-1)*7)] = f"{emp_rank_list[7]}\n"
        # print(list_of_lines)
        emp_file_w = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_employers.txt", "w")
        emp_file_w.writelines(list_of_lines)
        emp_file_w.close()
        print("employee deleted succefully")
        return list_of_lines[3+((self.emp_id-1)*7)]
###########################################################

    def log_in(self):


        log_file_r = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_employers_attendence.txt", "r")
        emp_file_r = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_employers.txt", "r")

        # Here we get an input of the username of the employer
        while True:
            try:
                self.emp_username = input("Please enter your user name:  ")
            except ValueError:
                print("Invalid input. Try again: ")
            else:
                break

        # getting the id of the employee with the same username so that we can use it in the operations
        x = int()
        y = int()
        list_of_lines = emp_file_r.readlines()

        for line01 in list_of_lines:
            x += 1
            if self.emp_username == line01[:-1]:
                break
        self.emp_id = list_of_lines[x-6]
        self.emp_id = self.emp_id[4]
        id = int(self.emp_id)

        # Here we will add the record of the log in operation in the log files as a workday.

        list_of_lines02 = log_file_r.readlines()

        try:
            days = list_of_lines02[2+(3*(id))-1]
            days = days[:-1]
            days = int(days)
            list_of_lines02[2 + (3 * (id)) - 1] = f"{days + 1}\n"
            # write on the file after changing the logs and add the day.
            log_file_w = open(
                f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_employers_attendence.txt", "w")
            log_file_w.writelines(list_of_lines02)
            log_file_w.close()
            log_file_r.close()
        except IndexError:
            print("Incorrect username!")
            self.log_in()
        except UnboundLocalError:
            print("Incorrect username!")
            self.log_in()

####################################################

    def log_out(self):
        loop = True
        while loop:
            print(
                f"Are you sure you want to log out ? ")
            c_list = ["1. Yes", "2. No"]
            for i in c_list:
                print(i)
            c = input("please enter your choice here: ")
            if ("y" in c) or ("y" in c) or ("1" in c):
                print("Logging out...")
                print("Please log in again: ")
                self.log_in()
                loop = False
                pass
            elif ("n" in c) or ("N" in c) or ("2" in c):
                loop = False
                pass
            else:
                print("Please enter a right choice: ")



