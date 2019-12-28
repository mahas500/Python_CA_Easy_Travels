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

    @classmethod
    def getAllPackages(cls, headers):
        responseData = cls.packageDAO.getAllPackages()

        packageList = []
        for i in responseData:

            packageList.append(cls.getPackageWithIternaryDetailsFromPackageId(i.get('package_id')))
        return packageList

    @classmethod
    def createIternaryForPackage(cls, headers, iternaryList):

        if cls.employeeService.checkIfEmployeeLoggedIn(headers.get('sessionId')):
            employee = cls.employeeDAO.getEmployeeFromSessionId(headers.get('sessionId'))
            if cls.employeeService.checkIfEmployeeHasARole(employee['employee_id'], 2):
                if cls.checkIfPackageExist(headers.get('packageId')):
                    for i in iternaryList:
                        iternary_id = str(uuid.uuid4())

                        cls.packageDAO.createIternaryForPackage(iternary_id, headers.get('packageId'),
                                                                i.get('day_number'),
                                                                i.get('day_date'),
                                                                i.get('day_details'))

        return None

    @classmethod
    def checkIfPackageExist(cls, packageId):

        package = cls.packageDAO.getPackageFromPackgaeId(packageId)
        if package is not None:
            return True
        else:
            return False

    @classmethod
    def getPackageWithIternaryDetailsFromPackageId(cls, packageId):
        packageDetails = {'package': cls.packageDAO.getPackageFromPackgaeId(packageId),
                          'iternary': cls.packageDAO.getIternariesDetailsOfPackage(packageId)}

        return packageDetails
