import unittest
import Config
import Employee
import Customer
import os
# import Main_menu


#Our application is mainly based on storing data on files and calling it again, 
# So we decided to make our application a way to check if those data are stored correctly or not
# And this will happen by testing the specific portions of codes (individually) that are responsible for 
# storing and calling the data before we use it in our classes and methods.
   
 ########################################################################
 # Class 02 testes
 # #######################################################################   


# import Class02

def add_customer(cus_id, cus_name, cus_national_id, cus_health, cus_sex, cus_age):
    #Make the test file empty
    delete = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "w")
    delete.write("")

    emp_file = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "a")
    content = str(f"#ID#{cus_id}\n{cus_name}\n{cus_national_id}\n{cus_health}\n{cus_sex}\n{cus_age}\n")
    emp_file.write(f"{content}\n")
    emp_file.close()
    emp_file_r = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "r")
    emp_list = emp_file_r.readlines()
    return emp_list

def delete_customer():

    #Make the test file empty
    delete = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "w")
    delete.write("")

    #Write the customer that we want to delete
    emp_file = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "a")
    content = f"#ID#1\nAbraham\n00000000000000\nNone\nfemale\n22\n"
    emp_file.write(f"{content}\n")
    emp_file.close()

    #write The NoNeS instead of the customer deatils
    emp_file_r = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "r")
    list_of_lines = emp_file_r.readlines()

    n = int()
    for i in range(5):
        list_of_lines[1+n] = "None\n"
        n += 1
    
    #print the list agian in the file after editing it...
    cus_file_w = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_test.txt", "w")
    cus_file_w.writelines(list_of_lines)
    cus_file_w.close()

    print("The customer has been dleted suceffully...")
    return list_of_lines


class second_class_portions(unittest.TestCase):
    def test_add_cus(self):
        self.assertEqual(add_customer(1, "Abraham", "00000000000000", "None", "female", 22 ), ["#ID#1\n", "Abraham\n", "00000000000000\n", "None\n", "female\n", "22\n", "\n"])
    def test_delete_cus(self):
        self.assertEqual(delete_customer(), ["#ID#1\n", "None\n", "None\n", "None\n", "None\n", "None\n", "\n"])

class second_class_methods(unittest.TestCase):
    def test_show_customers(self):
        cus_file_r = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_customers.txt", "r")
        list_of_lines = cus_file_r.readlines()
        self.assertEqual(list_of_lines, Customer.test.show_customers())
    def test_add_customer(self):
        name = input("Please enter the name of the customer you will test addition on (keep it in mind cause you will write it again): ") #Put the name you will add here...
        name = f"{name}\n"
        #Make sure the name variable is the same as the name you will enter in the method...
        self.assertIn(name, Customer.test.add_customer())
    def test_delete(self):
        self.assertEqual("None\n", Customer.test.delete_customer())
    
if __name__ == "__main__" :
    unittest.main()
 