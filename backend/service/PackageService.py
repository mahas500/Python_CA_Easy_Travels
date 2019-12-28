import uuid

from dao.EmployeeDAO import EmployeeDAO
from dao.PackageDAO import PackageDAO
from service.EmployeeService import EmployeeService


class PackageService:
    packageDAO = PackageDAO()
    employeeService = EmployeeService()
    employeeDAO = EmployeeDAO()

    @classmethod
    def createPackage(cls, headers, data):
        if cls.employeeService.checkIfEmployeeLoggedIn(headers.get('sessionId')):
            employee = cls.employeeDAO.getEmployeeFromSessionId(headers.get('sessionId'))
            if cls.employeeService.checkIfEmployeeHasARole(employee['employee_id'], 2):
                packageId = str(uuid.uuid4())
                cls.packageDAO.createPackage(packageId, employee.get('employee_id'), data.get('package_display_name'),
                                             data.get('unique_url_name'), data.get('days'),
                                             data.get('night'), data.get('charges'), data.get('country'),
                                             data.get('city'), data.get('valid'))

        return None
