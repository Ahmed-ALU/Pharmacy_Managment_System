
from Employee import employee
from Customer import customer
from Products import products
from Sell import sell




employee = employee()
customer = customer()
product = products()
sell = sell()

def menu():

    print("WELCOME TO THE PHARMACY SYSTEM")
    print("------------------------------")

    while True:
        try:
            login_choice = int(input("Enter - 1 to log in | 2 to exit: "))
        except ValueError:
            print("Invalid input. Try again: ")
        else:
            break

    if login_choice == 1:

        employee.log_in()
        
        repeat = True
        while repeat:
            print("Choose operations [choice]")
            print("-------------------------")

            print("Customers                Products                Employees                  Selling")
            print("--------------------------------------------------------------------------------------------")
            print("Add customer[1]          Add Product[5]          Add employee[10]           Sell product[12]")
            print("Delete customer[2]       Delete Product [6]      Delete employee[11]                        ")
            print("Edit customer[3]         Edit product[7]                                                    ")
            print("Show customer[4]         Order product[8]                                                   ")
            print("                         Availability[9]                                                    ")
            print("-------------------------------------------------------------------------------------------")
            print("LOG OUT [0]")

            while True:
                try:
                    op_choice = int(input("Enter operation [Option]: "))
                except ValueError:
                    print("Invalid input. Try again: ")
                else:
                    break
            if op_choice == 1:
                customer.add_customer()
            elif op_choice == 2:
                customer.delete_customer()
            elif op_choice == 3:
                customer.edit_customer()
            elif op_choice == 4:
                customer.show_customers()
            elif op_choice == 5:
                product.add_pro()
            elif op_choice == 6:
                product.delete_pro()
            elif op_choice == 7:
                product.edit_pro()
            elif op_choice == 8:
                product.order_pro()
            elif op_choice == 9:
                product.show_avilability()
            elif op_choice == 10:
                employee.add_emp()
            elif op_choice == 11:
                employee.delete_emp()
            elif op_choice == 12:
                sell.cus_identify()
                sell.buy()
                sell.pay()
                sell.feedback()
            elif op_choice == 0:
                employee.log_out()

            while True:
                try:
                    choice = int(input("Do you want to do an operation again? press 1 for yes and 2 to exit: "))

                except ValueError:
                    print("Invalid input. Try again: ")
                else:
                    break

            if choice == 1:
                repeat = True  # if he wants to keep using he sets repeat to to True so that the while loop continues
            elif choice == 2:
                menu()


    else:
        exit()




menu()