from dao.CustomerDAO import CustomerDAO


class CustomerService:

    customerDAO = CustomerDAO()

    @classmethod
    def customerCreate(cls, headers, data):
        responseData = cls.CustomerDAO.employeeLogin(data.get('username'), data.get('password'))

        if responseData is not None:
            responseData = cls.CustomerDAO.updateEmployeeSessionToken(responseData['employee_id'])

        return responseData