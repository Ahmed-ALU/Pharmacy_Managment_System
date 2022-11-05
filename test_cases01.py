import unittest
import Config
import Employee
import Customer
import os

# Note that:
# The unittesting was used in order to help us fixing the bugs in our code and make sure it is ok
# We tested it one by one, so you may face some errors and hardships in runing the whole code together
# because it wasn't made for that, it can work (and we made sure it works), but we can't expect what
# would happen with you as a person who didn't see our code before..... Codes are not trusted....


# Our application is mainly based on storing data on files and calling it again,
# So we decided to make our application a way to check if those data are stored correctly or not
# And this will happen by testing the specific portions of codes (individually) that are responsible for
# storing and calling the data before we use it in our classes and methods.

def add_id():
    # Make the test file empty
    delete = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "w")
    delete.write("")

    # add ID to the empty file
    id_file_a = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "a")
    with open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "r") as f:
        last_line = int()
        for line in f:
            last_line = line
        new_id = int(last_line) + 1
    id_file_a.write(f"{new_id}\n")
    emp_id = new_id
    id_file_r = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "r")
    id_list = id_file_r.readlines()
    return emp_id
################################

def id_to_file():
    # Make the test file empty
    delete = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "w")
    delete.write("")

    add_id()
    # add ID to the empty file
    id_file_a = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "a")
    with open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "r") as f:
        last_line = int()
        for line in f:
            last_line = line
        new_id = int(last_line) + 1
    id_file_a.write(f"{new_id}\n")
    emp_id = new_id
    id_file_r = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "r")
    id_list = id_file_r.readlines()
    return id_list
#################################

def add_emp(emp_id, emp_name, emp_national_id, emp_rank, emp_sex, emp_username):
    # Make the test file empty
    delete = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "w")
    delete.write("")

    emp_file = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "a")
    content = str(
        f"#ID#{emp_id}\n{emp_name}\n{emp_national_id}\n{emp_rank}\n{emp_sex}\n{emp_username}\n")
    emp_file.write(f"{content}\n")
    emp_file.close()
    emp_file_r = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "r")
    emp_list = emp_file_r.readlines()
    return emp_list
###################################

def delete_emp(emp_id):
    # Make the test file empty
    delete = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "w")
    delete.write("")

    # Write the employee that we want to delete
    emp_file = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "a")
    content = f"#ID#1\nAhmed\n00000000000000\npharmacist\nmale\nAhm123\n"
    emp_file.write(f"{content}\n")
    emp_file.close()

    # Delete The employee (by turning his rank into "retired")
    emp_file = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "r")
    list_of_lines = emp_file.readlines()
    if emp_id == 1:
        list_of_lines[3] = f"{Config.emp_rank_list[7]}\n"
    else:
        list_of_lines[3+((emp_id-1)*7)] = f"{Config.emp_rank_list[7]}\n"
    # print(list_of_lines)
    emp_file_w = open(
        f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_employers.txt", "w")
    emp_file_w.writelines(list_of_lines)
    emp_file_w.close()
    print("employee deleted succefully")
    return list_of_lines[3]
####################################

def log_out():

    c = "yes"
    # c = input("please enter your choice here")
    if "y" in c or "y" in c or "1" in c:
        return "Call The main menue here"
        loop == False
        pass
    elif ("n" in c) or ("N" in c) or ("2" in c):
        # loop == False
        pass
    else:
        print("Please enter a right choice")


class first_class_portions(unittest.TestCase):

    def test_add_id(self):
        self.assertEqual(add_id(), 1)

    def test_id_to_file(self):
        add_id()
        self.assertEqual(id_to_file(), ["1\n"])

    def test_add_emp(self):
        self.assertEqual(add_emp("1", "Ahmed", "00000000000000", "pharmacist", "male", "Ahm123"), [
                         "#ID#1\n", "Ahmed\n", "00000000000000\n", "pharmacist\n", "male\n", "Ahm123\n", "\n"])

    def test_delete_emp(self):
        self.assertEqual(delete_emp(1), "retired\n")

    def test_log_out(self):
        self.assertEqual(log_out(), "Call The main menue here")


class first_class_methods(unittest.TestCase):
    def test_delete(self):
        self.assertIn("retired\n", Employee.test.delete_emp())


if __name__ == "__main__":
    unittest.main()
