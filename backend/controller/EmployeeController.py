from app import app
from service import EmployeeService
from flask import jsonify
from flask import flash, request

from service.EmployeeService import EmployeeService

employeeService = EmployeeService()


@app.route('/employeeLogin', methods=['POST'])
def employeeLogin():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = employeeService.employeeLogin(request.headers, request.json)

    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1

    return wsResponse


@app.route('/assignRoleToEmployee', methods=['POST'])
def assignRoleToEmployee():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = employeeService.assignRoleToEmployee(request.headers, request.json)

    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1

    return wsResponse
