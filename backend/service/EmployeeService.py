from dao.EmployeeDAO import EmployeeDAO


class EmployeeService:
    employeeDAO = EmployeeDAO()

    @classmethod
    def employeeLogin(cls, headers, data):
        responseData = cls.employeeDAO.employeeLogin(data.get('username'), data.get('password'))

        if responseData is not None:
            responseData = cls.employeeDAO.updateEmployeeSessionToken(responseData['employee_id'])
        return responseData
