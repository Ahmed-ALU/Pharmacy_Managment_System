from Config import *
from Customer import *
from Products import *
import os
customer_id = int()
# x = int()
temp_price = int()


class sell(customer, products):

    def __init__(self):
        customer.__init__(self)
        products.__init__(self)
        self.order_amount = None
        self.order_id = None
        self.buy_price = None
        self.t_profit = None
        self.x = int(0)
        self.order_list = None
        self.feed = None
#################################################################

    def cus_identify(self):

        # Here we should look for the customer who is a part of the selling operation so that we can
        # record the operation with his name in the system, and if he is not in the system we add him first.

        # Create the list for customer_IDs ...
        pro_file_r = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_customers_id.txt", "r")
        list_of_lines = pro_file_r.readlines()

        new_list_of_lines = list()
        for i in list_of_lines:
            new_list_of_lines.append(i[:-1])

        # See if the customer is a new one or not...
        while True:
            in_sys = input(
                "Is this the customer's first opertaion in our pharmacy? (Yes/No) : ")
            if "n" in in_sys or "N" in in_sys:
                self.cus_id = input(
                    "Please input the Id of the current buyer/customer: ")
                if self.cus_id not in new_list_of_lines[:][:-1]:
                    print(
                        "The id you entered is not in our system......repeating the process.....")
                    pass
                else:
                    customer_id = self.cus_id
                    return customer_id, self.cus_id
            elif "y" in in_sys or "Y" in in_sys:
                customer.add_customer(self)
                break
        return self.cus_id
#################################################################

    def buy(self):

        global customer_id, temp_price
        order_list = list()

        def get_id():
            global customer_id, temp_price
            new_id = int()

            # putting the product id, THe product the customer want to buy.....
            while True:
                try:
                    self.pro_id = int(
                        input("Please enter the id of the product you want to buy: "))
                except ValueError:
                    print("Invalid input. Try again: ")
                else:
                    break

            # Files COdes....................
            products_file = open(
                f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products.txt", "r")
            product_file_list = products_file.readlines()
            product_id_file = open(
                f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products_id.txt", "r")
            product_id_file_list = product_id_file.readlines()
            orders_id_file_r = open(
                f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_orders_id.txt", "r")
            orders_id_file_r_list = orders_id_file_r.readlines()
            orders_id_file_a = open(
                f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_orders_id.txt", "a")
            orders_file_r = open(
                f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_orders.txt", "r")
            orders_file_a = open(
                f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_orders.txt", "a")
            orders_file_r_list = orders_file_r.readlines()

            # HEre we check if the product we have indicated up there exists or not or what..........
            if f"{self.pro_id}\n" not in product_id_file_list or product_file_list[self.pro_id * 6 - 4] == "None\n":
                print("The product you have chose is not on our system")
                choice = input("Do you want to buy sth else?(yes/no) ")
                if "y" in choice or "Y" in choice:
                    get_id()
                elif "n" in choice or "N" in choice:
                    return choice

            elif product_file_list[(self.pro_id * 6) - 2] == '0\n':
                print(
                    "The product you have chose is not available, please order it and repeate the process")
                choice = input("Do you want to buy sth else?(yes/no) ")
                if "y" in choice or "Y" in choice:
                    get_id()
                elif "n" in choice or "N" in choice:
                    return choice

            # If the product is ok and exists, we proceed with asking the customer about the amount he want to get......
            else:
                while True:
                    try:
                        self.order_amount = int(
                            input("Please enter the quantity you want to order: "))
                    except ValueError:
                        print("Invalid input. Try again: ")
                    else:
                        break

                # Here we chek if the amount the customer chose to buy is available or not........
                if self.order_amount > int(product_file_list[(self.pro_id * 6) - 2][:-1]):
                    print(
                        f"The amount you have entered is too much, the maximum is {product_file_list[(self.pro_id * 6) - 2][:-1]}")
                    print("Please reenter the product Id...")
                    get_id()

                # Here we start writing the first ordered product on the temperorary list......
                self.x += 1
                order_list.append(f"{self.pro_id}\n")
                order_list.append(f"{self.order_amount}\n")
                temp_price01 = int(product_file_list[int(order_list[self.x * 2 - 2][:-1]) * 6 - 3]) * int(
                    order_list[self.x * 2 - 1])
                temp_price = temp_price + temp_price01
                # Show the total price after choosing each product
                print(f"Current Price: {temp_price}RWF")

                # If the customer want to buy multible products he can idicate that here,
                # Once he indicate that, the app will loop the last choosing process...
                choice = input("Do you want to buy sth else?(yes/no) ")
                if "y" in choice or "Y" in choice:
                    get_id()  # Looping the choice process
                # If he chose no here, that means that this is the last process and we should start storing the
                # order details in a file.........
                if "n" in choice or "N" in choice:
                    last_line = int()
                    for line in orders_id_file_r_list:
                        last_line = line
                        new_id = int(last_line[:-1]) + 1
                    orders_id_file_a.write(f"{new_id}\n")
                    self.order_id = new_id
                    p_content = order_list
                    order_list.insert(0, f"#ID#{self.order_id}\n")
                    content = order_list
                    # return choice, content

                    # Then we delete what has been bought from the product list
                    products_file_w = open(
                        f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products.txt", "w")
                    product_file_list[self.pro_id * 6 - 2] = int(
                        product_file_list[self.pro_id * 6 - 2][:-1]) - self.order_amount
                    product_file_list[self.pro_id * 6 -
                                      2] = f"{product_file_list[self.pro_id * 6 - 2]}\n"

            # THis is the last storing pieaces of code
            if "n" in choice or "N" in choice:
                orders_file_a.writelines(content)
                orders_file_a.write(f"{self.cus_id}\n")
                orders_file_a.write("\n")
                products_file_w.writelines(product_file_list)
                # print(content)

                print(
                    "Order has been placed succefully, please proceed with printing the recipt....")

                # This code will calculate the total price of all the products that has been bought/chosen......
                v = int(len(p_content) - 1)
                v2 = int()
                p = int()
                for i in range(self.x):
                    self.buy_price = int(product_file_list[int(p_content[v2 + 1][:-1]) * 6 - 3]) * int(
                        p_content[v2 + 2])
                    p = p + self.buy_price
                self.buy_price = p
                p2 = int()
                for i in range(self.x):
                    self.t_profit = int(product_file_list[int(
                        p_content[v2 + 1][:-1]) * 6 - 4]) * int(p_content[v2 + 2])
                    p2 = p2 + self.t_profit
                self.t_profit = p2
                self.t_profit = int(self.buy_price) - int(self.t_profit)

                print(f"This order has a total price of {self.buy_price}RWF")

        self.order_list = order_list
        get_id()
##########################################################

# In this method, we will be able to store the paid amount of money once the customer pay for his order
# In addition to store the pure amount of profits......
    def pay(self):

        # Files operations codes.....
        profits_file_a = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_profits.txt", "a")
        income_file_a = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_income.txt", "a")
        # orders_file_w = open(f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_orders.txt", "w")
        orders_file_r = open(
            f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_orders.txt", "r")
        orders_file_r_list = orders_file_r.readlines()

        # Here we check if the customer is willing to take/pay the order or not
        choice = input(
            "Did the customer paid the price of this order? (yes/no)")
        if "y" in choice or "Y" in choice:
            profits_file_a.write(f"{self.t_profit}\n")
            income_file_a.write(f"{self.buy_price}\n")
            print("Paid Succefully")

        elif "n" in choice or "N" in choice:

            ###### Here we will convert the order to NONEs... #######

            # orders_file_r_list[self.order_id]
            line_number = int(0)
            temp_id = int()
            for line in orders_file_r_list:
                line_number += 1
                if line.startswith("#"):
                    temp_id = line[4:-1]
                    temp_id = int(temp_id)
                    if temp_id == self.order_id:
                        break

            n = int()
            for i in range(self.x * 2):
                orders_file_r_list[line_number + n] = "None\n"
                n += 1
            orders_file_w = open(
                f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_orders.txt", "w")
            orders_file_w.writelines(orders_file_r_list)

            ##### Here we will put the quantities back ######
            products_file = open(
                f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products.txt", "r")
            product_file_list = products_file.readlines()

            v1 = int(1)
            v2 = int(2)
            for i in range(self.x):
                self.pro_id = (self.order_list[v1][:-1])
                self.amount = (self.order_list[v2][:-1])
                product_file_list[int(self.pro_id) * 6 - 2] = int(
                    product_file_list[int(self.pro_id) * 6 - 2][:-1]) + int(self.order_amount)
                product_file_list[int(
                    self.pro_id) * 6 - 2] = f"{product_file_list[int(self.pro_id) * 6 - 2]}\n"
                v1 += 1
                v2 += 1

            products_file_w = open(
                f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_products.txt", "w")
            products_file_w.writelines(product_file_list)

            print("The order has been canclelled succesfully")
#########################################################################

    # Just in case the customer want to give rating, we can take it her and store it.
    def feedback(self):
        choice = input("Do you want to add feedback? (yes/no): ")
        if "n" in choice or "N" in choice:
            pass
        elif "y" in choice or "Y" in choice:

            while True:
                try:
                    self.feed = float(
                        input("Please enter a number between 1 and 5: "))
                    if 0 <= self.feed <= 5:
                        pass
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid input. Try again: ")
                else:
                    break

            feedback_file_a = open(
                f"{os.path.dirname(os.path.abspath(__file__))}\Ahmed_Mohamed_feedback.txt", "a")
            feedback_file_a.write(f"{str(self.feed)}\n")



