from CustomUtils import CustomUtils
from Exceptions import WrongCredentials
from Exceptions.EmployeeDosentHaveRight import EmployeeDosentHaveRight
from Exceptions.NotLoggedIn import NotLoggedIn
from Exceptions.WrongCredentials import WrongCredentialsError
from app import app
from service import EmployeeService
from flask import jsonify
from flask import flash, request

from service.CustomerService import CustomerService

customerService = CustomerService()


@app.route('/createCustomer', methods=['POST'])
def createCustomer():
    wsResponse = {"resultSet": None, "operationStatus": None}

    try:
        responseData = customerService.createCustomer(request.headers, request.json)
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


@app.route('/customerLogin', methods=['POST'])
def customerLogin():
    wsResponse = {"resultSet": None, "operationStatus": None}

    try:
        responseData = customerService.customerLogin(request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except WrongCredentialsError:
        wsResponse['operationStatus'] = CustomUtils.WRONG_CREDENTIALS
    except Exception:
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG
    return wsResponse


@app.route('/getAllCustomers', methods=['GET'])
def getAllCustomers():
    wsResponse = {"resultSet": None, "operationStatus": None}

    try:
        responseData = customerService.getAllCustomers()
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except Exception:
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG
    return wsResponse


@app.route('/deleteCustomer', methods=['POST'])
def deleteCustomer():
    wsResponse = {"resultSet": None, "operationStatus": None}

    try:
        responseData = customerService.deleteCustomer(request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except Exception:
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG
    return wsResponse


@app.route('/searchCustomer', methods=['POST'])
def searchCustomer():
    wsResponse = {"resultSet": None, "operationStatus": None}

    try:
        responseData = customerService.searchCustomer(request.json.get('searchText'))
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except Exception as e:
        print(e)
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG
    return wsResponse
