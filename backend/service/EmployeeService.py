import uuid
from random import randint

from Exceptions.EmployeeDosentHaveRight import EmployeeDosentHaveRight
from Exceptions.EmployeeWithEmailNotExist import EmployeeWithEmailNotExist
from Exceptions.MailNotSent import MailNotSent
from Exceptions.NotLoggedIn import NotLoggedIn
from Exceptions.WrongCredentials import WrongCredentialsError
from dao.EmployeeDAO import EmployeeDAO
from service.EmailService import EmailService


class EmployeeService:
    employeeDAO = EmployeeDAO()
    emailService = EmailService()

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

    @classmethod
    def forgotPassword(cls, data):
        if cls.checkIfEmployeeExistWithEmailId(data.get('email')):
            responseData = cls.employeeDAO.checkIfEmployeeExistWithEmailId(data.get('email'))

            OTP = randint(100000, 999999)
            message = "One time password = " + str(OTP)
            if cls.emailService.sendEmail(data.get('email'), message):
                cls.employeeDAO.updateOTP(responseData.get('employee_id'), OTP)
                return None
            else:
                raise MailNotSent
        else:
            raise EmployeeWithEmailNotExist

    @classmethod
    def checkIfEmployeeExistWithEmailId(cls, emailId):
        responseData = cls.employeeDAO.checkIfEmployeeExistWithEmailId(emailId)
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def changePassword(cls, data):
        cls.employeeDAO.changePassword(data.get('email_id'), data.get('otp'), data.get('password'))
        return None
