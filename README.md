# Python_CA_Easy_Travels
We have designed and implemented backend for a travelling management system for a travel company named as “Easy Travels Web Portal”. This portal provide a variety of services related to a travel package booking for our customers. Also, the services of handling the enquiries given by the customers. We have employees in the organization with each employee having a unique role such as sales, operation, admin, operation head, HR. Each employee is having a unique role and the same role can have multiple employees. An Employee with a role sales can create and handle enquiries for the customers, an employee with role operation can create packages. Once a package is created by an employee with a role operation it is approved by operation head employee before releasing.  
Customer can visit our website and ask us for registering themselves in the portal. Once registration is done then a customer can login into the portal and then select from the variety of packages from the book and book it. Customer can also contact us in case of any issue. All of the information of the employees and customers are stored in the database. Hence all the CURD ( create, update, retrieve, delete) are done on it.

This System is designed for a Tour packages management company

# Functional Requirements:
1: Employees and customers should be able to login to the system, and their session should be maintained.
2: Employee with role admin should be able to create other employees and assign roles to them.
3: There should be provision for employees to change password with the OTP and otp should be sent to the registered email id.
4: Employees with role operation should be able to create holiday/tour packages.
5: Employees should be able to update package details
6: There should be functionality to search through itinerary of the packages.
7: There should be functionality for searching through all the customers.
8: There should be functionality for searching through Employee.
9: Employee with role sales should be able to create and handle enquires asked by the customers.
10: Employee with role sales should be able to register a new customer.
11: On Deletion of Customer entry, all the enquiries associated with that customer will be deleted. 
12: Customer should be able to book their desired packages.
13: There should be a functionality to get all customers, all enquires raised, all packages (for showing on website )created.
14: While retrieving, all the entries should be sorted by the latest creation.
