from dao.AdminDAO import AdminDAO


class AdminService:
    adminDAO = AdminDAO()

    @classmethod
    def adminlogin(cls, headers, data):
        responseData = cls.adminDAO.adminlogin(data.get('username'), data.get('password'))
        return responseData
