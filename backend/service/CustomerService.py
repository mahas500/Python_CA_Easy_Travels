from dao.CustomerDAO import CustomerDAO
from dao.EmployeeDAO import EmployeeDAO
from service.EmployeeService import EmployeeService


class CustomerService:
    customerDAO = CustomerDAO()
    employeeService = EmployeeService()
    employeeDAO = EmployeeDAO()

    @classmethod
    def customerCreate(cls, headers, data):
        print(headers.get('sessionId'))
        if cls.employeeService.checkIfEmployeeLoggedIn(headers.get('sessionId')):
            employee = cls.employeeDAO.getEmployeeFromSessionId(headers.get('sessionId'))
            if cls.employeeService.checkIfEmployeeHasARole(employee['employee_id'], 4):
                print(employee['employee_id'])
                customer = cls.customerDAO.customerCreate(data.get('name'),
                                                              data.get('username'), data.get('password'),
                                                              data.get('email'), data.get('contact_no'))
                print("hi 1")
                print(customer['customer_id'])
                print(customer)
                print("hi 2")
        return customer;


    @classmethod
    def enquiryCreate(cls, headers, data):
       # print(headers.get('sessionId'))
        if cls.employeeService.checkIfEmployeeLoggedIn(headers.get('sessionId')):
            employee = cls.employeeDAO.getEmployeeFromSessionId(headers.get('sessionId'))
            if cls.employeeService.checkIfEmployeeHasARole(employee['employee_id'], 4):
                print(employee['employee_id'])
                customer1 = cls.customerDAO.customerCreate(data.get('name'),
                                                              data.get('username'), data.get('password'),
                                                              data.get('email'), data.get('contact_no'))

                print(customer1)
                print("hi 1")
                print(customer1['customer_id'])
                print(customer1)

                if (cls.checkIfCustomerExist(customer1['customer_id'])):
                    print("hello")
                    enquiry = cls.customerDAO.customerEnquiryCreation(employee['employee_id'],customer1['customer_id'],
                                                                            data.get('enquiry_detail'),data.get('enquiry_type'),
                                                                            data.get('required_days'),data.get('required_nights'),
                                                                            data.get('required_country'))
                print("Hello enquiry")
                print(enquiry['enquiry_id'])

        return None;


    @classmethod
    def checkIfCustomerExist(cls, customer_id):
        responseData = cls.customerDAO.getCustomerFromCustomerId(customer_id)
        print("hello hey")
        print(responseData)
        if responseData is not None:
            return True
        else:
            return False

