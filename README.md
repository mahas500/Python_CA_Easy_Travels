# Python_CA_Easy_Travels
We have designed and implemented backend for a travelling management system for a travel company named as “Easy Travels Web Portal”. This portal provide a variety of services related to a travel package booking for our customers. Also, the services of handling the enquiries given by the customers. We have employees in the organization with each employee having a unique role such as sales, operation, admin, operation head, HR. Each employee is having a unique role and the same role can have multiple employees. An Employee with a role sales can create and handle enquiries for the customers, an employee with role operation can create packages. Once a package is created by an employee with a role operation it is approved by operation head employee before releasing.  
Customer can visit our website and ask us for registering themselves in the portal. Once registration is done then a customer can login into the portal and then select from the variety of packages from the book and book it. Customer can also contact us in case of any issue. All of the information of the employees and customers are stored in the database. Hence all the CURD ( create, update, retrieve, delete) are done on it.

This System is designed for a Tour packages management company

# Functional Requirements:
1: Employees and customers should be able to login to the system, and their session should be maintained.<br />
2: Employee with role admin should be able to create other employees and assign roles to them.<br />
3: There should be provision for employees to change password with the OTP and otp should be sent to the registered email id.<br />
4: Employees with role operation should be able to create holiday/tour packages.<br />
5: Employees should be able to update package details<br />
6: There should be functionality to search through itinerary of the packages. <br />
7: There should be functionality for searching through all the customers. <br />
8: There should be functionality for searching through Employee. <br />
9: Employee with role sales should be able to create and handle enquires asked by the customers. <br />
10: Employee with role sales should be able to register a new customer. <br />
11: On Deletion of Customer entry, all the enquiries associated with that customer will be deleted. <br />
12: Customer should be able to book their desired packages. <br />
13: There should be a functionality to get all customers, all enquires raised, all packages (for showing on website )created.<br />
14: While retrieving, all the entries should be sorted by the latest creation. <br />

# Users of the Information systems
Following are the two major users of the information systems:<br />
1. Employees <br />
Employees act as an actor or user of the easy travels web portal information systems by managing the web portal. They are the one responsible for handling requests which comes from the clients to the server. Request such as enquiry creation, customer creation, customer deletion, package creation etc. are handled by the employees. <br />
2. Customers <br />
Customers also act as a user of the system by interacting with the employees. They send requests to the server by acting as a client. Request such as enquiry creation, new package creation, getting the booking details etc are raised by the customers. These requests are handled by the employees at the server end. <br />

