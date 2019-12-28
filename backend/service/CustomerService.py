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
                responseData = cls.customerDAO.customerCreate(data.get('name'),
                                                              data.get('username'), data.get('password'),
                                                              data.get('email'), data.get('contact_no'))

        return None;


