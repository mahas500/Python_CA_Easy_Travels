from CustomUtils import CustomUtils

from Exceptions.EmployeeDosentHaveRight import EmployeeDosentHaveRight
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
