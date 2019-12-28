from wsgiref import headers

from dao.CustomerDAO import CustomerDAO
from dao.EmployeeDAO import EmployeeDAO
from service.EmployeeService import EmployeeService


class CustomerService:
    customerDAO = CustomerDAO()
    employeeService = EmployeeService()
    employeeDAO = EmployeeDAO()

    @classmethod
    def customerCreate(cls, headers, data):
        if cls.employeeService.checkIfEmployeeLoggedIn(headers.get('sessionId')):
            employee = cls.employeeDAO.getEmployeeFromSessionId(headers.get('sessionId'))
            if cls.employeeService.checkIfEmployeeHasARole(employee['employee_id'], 4):
                customer = cls.customerDAO.customerCreate(data.get('name'),
                                                              data.get('username'), data.get('password'),
                                                              data.get('email'), data.get('contact_no'))

        return customer;


    @classmethod
    def enquiryCreate(cls, headers, data):

        if cls.employeeService.checkIfEmployeeLoggedIn(headers.get('employee_sessionId')):
            employee = cls.employeeDAO.getEmployeeFromSessionId(headers.get('employee_sessionId'))
            if cls.employeeService.checkIfEmployeeHasARole(employee['employee_id'], 4):
                 if cls.checkIfCustomerExist(headers.get('customer_sessionId')):
                    customer = cls.customerDAO.getCustomerFromCustomersessionId(headers.get('customer_sessionId'))
                    enquiry = cls.customerDAO.customerEnquiryCreation(employee['employee_id'],customer['customer_id'],
                                                                            data.get('enquiry_detail'),data.get('enquiry_type'),
                                                                            data.get('required_days'),data.get('required_nights'),
                                                                            data.get('required_country'))


        return enquiry;


    @classmethod
    def checkIfCustomerExist(cls, sessionId):
        responseData = cls.customerDAO.getCustomerFromCustomersessionId(sessionId)
        if responseData is not None:
            return True
        else:
            return False

