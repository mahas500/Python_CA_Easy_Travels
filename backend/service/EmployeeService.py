from dao.EmployeeDAO import EmployeeDAO


class EmployeeService:

    employeeDAO = EmployeeDAO()

    @classmethod
    def employeeLogin(cls, headers, data):
        responseData = cls.employeeDAO.employeeLogin(data.get('username'), data.get('password'))

        if responseData is not None:
            responseData = cls.employeeDAO.updateEmployeeSessionToken(responseData['employee_id'])

        return responseData

    @classmethod
    def assignRoleToEmployee(cls, headers, data):

        if cls.checkIfEmployeeLoggedIn(headers.get('sessionId')):

            employee = cls.employeeDAO.getEmployeeFromSessionId(headers.get('sessionId'))
            if cls.checkIfEmployeeHasARole(employee['employee_id'], 3):

                cls.employeeDAO.assignRoleToEmployee(data.get('employeeId'), data.get('roleId'))
            else:
                exit()
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
