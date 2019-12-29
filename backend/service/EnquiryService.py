from Exceptions.CustomerDoesNotExists import CustomerDoesNotExists
from Exceptions.EmployeeDosentHaveRight import EmployeeDosentHaveRight
from Exceptions.NotLoggedIn import NotLoggedIn
from dao.CustomerDAO import CustomerDAO
from dao.EmployeeDAO import EmployeeDAO
from dao.EnquiryDAO import EnquiryDAO
from service.CustomerService import CustomerService
from service.EmployeeService import EmployeeService


class EnquiryService:
    employeeService = EmployeeService()
    customerService = CustomerService()
    customerDAO = CustomerDAO()
    employeeDAO = EmployeeDAO()
    enquiryDAO = EnquiryDAO()

    @classmethod
    def createEnquiry(cls, headers, data):

        if cls.employeeService.checkIfEmployeeLoggedIn(headers.get('session_id')):

            employee = cls.employeeDAO.getEmployeeFromSessionId(headers.get('session_id'))
            if cls.employeeService.checkIfEmployeeHasARole(employee['employee_id'], 4):

                if cls.customerService.checkIfCustomerExist(data.get('customer_id')):
                    print(3)
                    customer = cls.customerDAO.getCustomerFromCustomerId(data.get('customer_id'))
                    enquiry = cls.enquiryDAO.createEnquiry(employee['employee_id'], customer['customer_id'],
                                                           data.get('enquiry_detail'),
                                                           data.get('enquiry_type'),
                                                           data.get('required_days'),
                                                           data.get('required_nights'),
                                                           data.get('required_country'))
                else:
                    raise CustomerDoesNotExists
            else:
                raise EmployeeDosentHaveRight
        else:
            raise NotLoggedIn

        return enquiry
