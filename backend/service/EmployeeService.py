import uuid

from Exceptions.EmployeeDosentHaveRight import EmployeeDosentHaveRight
from Exceptions.NotLoggedIn import NotLoggedIn
from Exceptions.WrongCredentials import WrongCredentialsError
from dao.EmployeeDAO import EmployeeDAO


class EmployeeService:
    employeeDAO = EmployeeDAO()

    @classmethod
    def employeeLogin(cls, headers, data):
        responseData = cls.employeeDAO.employeeLogin(data.get('username'), data.get('password'))

        if responseData is not None:
            responseData = cls.employeeDAO.updateEmployeeSessionToken(responseData['employee_id'])
            return responseData
        else:
            raise WrongCredentialsError

    @classmethod
    def assignRoleToEmployee(cls, headers, data):

        if cls.checkIfEmployeeLoggedIn(headers.get('sessionId')):

            employee = cls.employeeDAO.getEmployeeFromSessionId(headers.get('sessionId'))

            if cls.checkIfEmployeeHasARole(employee['employee_id'], 3):

                cls.employeeDAO.assignRoleToEmployee(data.get('employeeId'), data.get('roleId'))
            else:
                raise EmployeeDosentHaveRight
        else:
            raise NotLoggedIn
        return None

    @classmethod
    def checkIfEmployeeLoggedIn(cls, sessionId):
        responseData = cls.employeeDAO.getEmployeeFromSessionId(sessionId)
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def checkIfEmployeeHasARole(cls, employeeId, roleId):
        responseData = cls.employeeDAO.checkIfEmployeeHasARole(employeeId, roleId)
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def getAllEmployees(cls):
        responseData = cls.employeeDAO.getAllEmployees()

        return responseData

    @classmethod
    def createEmployee(cls, header, data):
        if cls.checkIfEmployeeLoggedIn(header.get('sessionId')):

            employee = cls.employeeDAO.getEmployeeFromSessionId(header.get('sessionId'))

            if cls.checkIfEmployeeHasARole(employee['employee_id'], 3):
                employee_id = str(uuid.uuid4())
                cls.employeeDAO.createEmployee(employee_id, data.get('name'), data.get('username'),
                                               data.get('password'), data.get('email'), data.get('contact_no'))

            else:
                raise EmployeeDosentHaveRight
        else:
            raise NotLoggedIn

    @classmethod
    def searchEmployee(cls, searchText):
        responseData = cls.employeeDAO.searchEmployee(searchText)

        return responseData
