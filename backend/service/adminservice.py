from dao.AdminDAO import AdminDAO


class AdminService:
    adminDAO = AdminDAO()

    @classmethod
    def employeeLogin(cls, headers, data):
        responseData = cls.adminDAO.employeeLogin(data.get('username'), data.get('password'))

        if responseData is not None:
            responseData = cls.adminDAO.updateEmployeeSessionToken(responseData['employee_id'])
        return responseData
