from wsgiref import headers

from Exceptions.EmployeeDosentHaveRight import EmployeeDosentHaveRight
from Exceptions.NotLoggedIn import NotLoggedIn
from dao.CustomerDAO import CustomerDAO
from dao.EmployeeDAO import EmployeeDAO
from service.EmployeeService import EmployeeService


class CustomerService:
    customerDAO = CustomerDAO()
    employeeService = EmployeeService()
    employeeDAO = EmployeeDAO()

    @classmethod
    def createCustomer(cls, header, data):
        if cls.employeeService.checkIfEmployeeLoggedIn(header.get('sessionId')):
            employee = cls.employeeDAO.getEmployeeFromSessionId(header.get('sessionId'))
            if cls.employeeService.checkIfEmployeeHasARole(employee['employee_id'], 4):
                customer = cls.customerDAO.customerCreate(data.get('name'),
                                                          data.get('username'), data.get('password'),
                                                          data.get('email'), data.get('contact_no'))
            else:
                raise EmployeeDosentHaveRight
        else:
            raise NotLoggedIn

        return customer

    @classmethod
    def checkIfCustomerExist(cls, customerId):
        responseData = cls.customerDAO.getCustomerFromCustomerId(customerId)
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def getAllCustomersService(cls):
        responseData = cls.customerDAO.getAllCustomersfromDB()
        return responseData

    @classmethod
    def deleteCustomerService(cls, data):
        cls.customerDAO.deleteCustomerfromDB(data.get('customer_id'))
        return "Record deleted Successfully"
