# ⚕️ PHARMACY MANAGEMENT SYSTEM ⚕️ 

**Pair Project**

Welcome to our application...

as we indicated earlier, our applicatoin is a pharmacy managment application that, 
our catalog will take you through how to use our application and give a brief about our module..

First: The main Application.....

A- In order to start the application, you have to only RUN the Main_menu.py file

B- Once you run the Main_menu.py file, you will be sent to the main screen where 
you can log in with your user name or exit the application

C- Your user_name is .......  Binush2060 ....... And your ID is (3)....

D- Once you type your user name, you will log in 
(and a day of attendence will be recorded under your id in employers_attendence.txt)
 Then you will be sent to the operations page where you can choose any operation to do.

E- Once you finish your operation, you will be able to choose to do another one or to log out then you can stay in the 
main page or exit the application.

NOTE THAT 01: 
You have to keep all the uploaded files (including the txt files) in the same repositry when you start the application because it contains the default 
and the log-in DATA

NOTE THAT 02:
All the operations that calls the products or customers are help using their ids not name. This is to facilitate the process and avoid errors
in addition to simulate the barcode process......


####################################################

SECOND: The Operations....

The fisrt section: Customers..

A- Add customer[1]: in this operation, you will be able to add a customer to the files with new id and new details, once you finish adding it
the customers details will be recorded in the customers.txt file in the next shape:

#ID#{customer id}
name
national id
cronic disease if exists
gender
age

and in the same time the programme will read the last used id in customer_id.txt file and then add 1 to it and 
then give the answer as an id to the new customer as a new id, then store that answer in the same file as the last used id again.


B- Delete customer[2]: ..... 
When you delete a customer it doesn't delete him from the file, but instead it turns all of his data into Nones as the following: 

#ID#{customer id}
None
None
None
None
None

C- Edit customer[3]: .........
You can choose to edit any specifc detail about any customer by indicating his id.

D- Show customer[4]: ...........
You can show all the customers in your database so that you know their details or for any perpose....

We have three default customers with the application:

#ID#1
Myra Luguiri
31843589735
Diabetes
female
19

#ID#2
Samuel Musenza
725349857932
None
male
21

#ID#3
Ednah Aktoh
29238798765
None
female
22

************************************************************

The second section: Employees...


A- Add Employee[10]: in this operation, you will be able to add an Employee to the files with new id and new details, once you finish adding it
the employee's details will be recorded in the employees.txt file in the next shape:

#ID#{employee id}
name
national ID
position
gender
user_name

and in the same time the programme will read the last used id in employees_id.txt file and then add 1 to it and 
then give the answer as an id to the new employee as a new id, then store that answer in the same file as the last used id again.

We have three default employees with the application:

#ID#1
Mohamed Ahmed
30201012671431
cashier
male
Mohame6705

#ID#2
Abraham Direes
439828907772
hr
male
Abraha7878

#ID#3
Binusha Balachandran
110294839321
manager
female
Binush2060


B- Delete Employee[11]: .......

In order to delete an employee, we will just sit his position to retired in order not to loose his data as the following:
#ID#3
Binusha Balachandran
110294839321
retired
female
Binush2060


************************************************************

The third section: products...

A- Add Product[5] - Delete Product [6] - Edit product[7] .....

The same type of operations as indicated in section one and three.\..

The storing of the products is in the following shape:

#ID#{Product id}
product name
product price (before profits)
product selling price (with profits)
quantity

and we have 4 products as default in our database in products.txt file (EACH PRODUCTS HAS 20 as a quantity):

#ID#1
nat b
3000
3500
20

#ID#2
feldene layotabs
6000
7500
20

#ID#3
paracytemol
500
1000
20

#ID#4
curamol
700
1100
20


B- Order product[8]: .........
If a specific product in the pharmacy has finished (the quantity is zero) you can order it 
(any quantity) by this operation from the exporter or the storehouse....

C- Availability[9]: .....
To chek the quantity of each avilable medicine...

**************************************************************
The fourth section: selling...

A- Sell product[12]: ......

And this operation will take you through a bunch of operations that will help you to sell any available product/s to any customer.

### Authors 
    - Ahmed Mohamed
    - Abraham Dires

