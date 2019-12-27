from dao.AdminDAO import AdminDAO


class AdminService:
    adminDAO = AdminDAO()

    @classmethod
    def adminlogin(cls, headers, data):
        responseData = cls.adminDAO.adminlogin(data.get('username'), data.get('password'))

        if responseData is not None:
            print(cls.adminDAO.updateAdminSessionToken(responseData['employee_id']))
        return responseData
