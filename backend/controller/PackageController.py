from CustomUtils import CustomUtils
from Exceptions import WrongCredentials
from Exceptions.EmployeeDosentHaveRight import EmployeeDosentHaveRight
from Exceptions.NotLoggedIn import NotLoggedIn
from Exceptions.PackageDoesNotExist import PackageDoesNotExist
from app import app

from flask import flash, request

from service.PackageService import PackageService

packageService = PackageService()


@app.route('/createPackage', methods=['POST'])
def createPackage():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = packageService.createPackage(request.headers, request.json)

        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except EmployeeDosentHaveRight:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.EMPLOYEE_DOSENT_HAS_RIGHT
    except NotLoggedIn:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.EMPLOYEE_NOT_LOGGED_IN
    except Exception:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG

    return wsResponse


@app.route('/getAllPackages', methods=['POST'])
def getAllPackages():
    wsResponse = {"resultSet": None, "operationStatus": None}

    try:
        responseData = packageService.getAllPackages(request.headers)

        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG

    return wsResponse


@app.route('/createIternaryForPackage', methods=['POST'])
def createIternaryForPackage():
    wsResponse = {"resultSet": None, "operationStatus": None}


    try:
        responseData = packageService.createIternaryForPackage(request.headers, request.json.get('iternary'))
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except EmployeeDosentHaveRight:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.EMPLOYEE_DOSENT_HAS_RIGHT
    except NotLoggedIn:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.EMPLOYEE_NOT_LOGGED_IN
    except PackageDoesNotExist:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.PACKAGE_DOES_NOT_EXIST
    except Exception:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG

    return wsResponse


@app.route('/getPackageWithIternaryDetailsFromPackageId', methods=['POST'])
def getPackageWithIternaryDetailsFromPackageId():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = packageService.getPackageWithIternaryDetailsFromPackageId(request.json.get('package_id'))

        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except:

        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG

    return wsResponse


@app.route('/packageBooking', methods=['POST'])
def packageBooking():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = packageService.packageBookingService(request.headers,request.json)

        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1


    except PackageDoesNotExist:

        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.PACKAGE_DOES_NOT_EXIST

    return wsResponse
