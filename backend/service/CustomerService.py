from wsgiref import headers

from Exceptions import WrongCredentials
from Exceptions.EmployeeDosentHaveRight import EmployeeDosentHaveRight
from Exceptions.NotLoggedIn import NotLoggedIn
from Exceptions.WrongCredentials import WrongCredentialsError
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
    def getAllCustomers(cls):
        responseData = cls.customerDAO.getAllCustomersfromDB()
        return responseData

    @classmethod
    def deleteCustomer(cls, data):
        cls.customerDAO.deleteCustomer(data.get('customer_id'))
        return None

    @classmethod
    def customerLogin(cls, data):
        customer = cls.customerDAO.customerLogin(data.get('username'), data.get('password'))
        if customer is not None:
            return customer
        else:
            raise WrongCredentialsError

    @classmethod
    def searchCustomer(cls, searchText):
        responseData = cls.customerDAO.searchCustomer(searchText)

    def getCustomerIDfromCustomerSessionID(cls, header):
        responseData = cls.customerDAO.getCustomerfromCustomerSessionID(header.get('session_id'))
        print(responseData)

        return responseData
