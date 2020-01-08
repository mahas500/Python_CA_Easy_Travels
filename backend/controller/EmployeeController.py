from CustomUtils import CustomUtils

from Exceptions.EmployeeDosentHaveRight import EmployeeDosentHaveRight
from Exceptions.EmployeeWithEmailNotExist import EmployeeWithEmailNotExist
from Exceptions.MailNotSent import MailNotSent
from Exceptions.NotLoggedIn import NotLoggedIn
from Exceptions.WrongCredentials import WrongCredentialsError
from app import app
from service import EmployeeService
from flask import jsonify
from flask import flash, request

from service.EmployeeService import EmployeeService

employeeService = EmployeeService()


@app.route('/employeeLogin', methods=['POST'])
def employeeLogin():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = employeeService.employeeLogin(request.headers, request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = CustomUtils.SUCCESSFULL
    except WrongCredentialsError:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.WRONG_CREDENTIALS
    except Exception:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG

    return wsResponse


@app.route('/assignRoleToEmployee', methods=['POST'])
def assignRoleToEmployee():
    wsResponse = {"resultSet": None, "operationStatus": None}

    try:
        responseData = employeeService.assignRoleToEmployee(request.headers, request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = CustomUtils.SUCCESSFULL
    except EmployeeDosentHaveRight:
        responseData = None
        wsResponse['operationStatus'] = CustomUtils.EMPLOYEE_DOSENT_HAS_RIGHT
    except NotLoggedIn:
        responseData = None
        wsResponse['operationStatus'] = CustomUtils.EMPLOYEE_NOT_LOGGED_IN
    except Exception:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG

    return wsResponse


@app.route('/getAllEmployees', methods=['POST'])
def getAllEmployees():
    wsResponse = {"resultSet": None, "operationStatus": None}

    try:
        responseData = employeeService.getAllEmployees()

        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = CustomUtils.SUCCESSFULL
    except:

        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG

    return wsResponse


@app.route('/createEmployee', methods=['POST'])
def createEmployee():
    wsResponse = {"resultSet": None, "operationStatus": None}

    try:
        responseData = employeeService.createEmployee(request.headers, request.json)

        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = CustomUtils.SUCCESSFULL
    except EmployeeDosentHaveRight:

        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.EMPLOYEE_DOSENT_HAS_RIGHT
    except NotLoggedIn:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.EMPLOYEE_NOT_LOGGED_IN
    except Exception as e:
        print(e)
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG
    return wsResponse


@app.route('/searchEmployee', methods=['POST'])
def searchEmployee():
    wsResponse = {"resultSet": None, "operationStatus": None}

    try:
        responseData = employeeService.searchEmployee(request.json.get("searchText"))

        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = CustomUtils.SUCCESSFULL
    except:

        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG

    return wsResponse


@app.route('/forgotPassword', methods=['POST'])
def forgotPassword():
    wsResponse = {"resultSet": None, "operationStatus": None}

    try:
        responseData = employeeService.forgotPassword(request.json)

        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = CustomUtils.SUCCESSFULL

    except MailNotSent:
        wsResponse['operationStatus'] = CustomUtils.EMAIL_SENDING_FAILED
    except EmployeeWithEmailNotExist:
        wsResponse['operationStatus'] = CustomUtils.EMPLOYEE_WITH_EMAIL_NOT_EXIST
    except Exception:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG

    return wsResponse


@app.route('/changePassword', methods=['POST'])
def changePassword():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = employeeService.changePassword(request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = CustomUtils.SUCCESSFULL
    except Exception:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG

    return wsResponse