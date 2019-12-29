from CustomUtils import CustomUtils
from Exceptions.EmployeeDosentHaveRight import EmployeeDosentHaveRight
from Exceptions.NotLoggedIn import NotLoggedIn
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


@app.route('/getAllCustomers', methods=['GET'])
def getAllCustomers():
    wsResponse = {"resultSet": None, "operationStatus": None}

    try:
        responseData = customerService.getAllCustomers()
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except Exception:
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG
    return responseData


@app.route('/deleteCustomer', methods=['POST'])
def deleteCustomer():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = customerService.deleteCustomerService(request.json)
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return responseData
