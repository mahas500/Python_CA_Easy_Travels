from app import app
from service import EmployeeService
from flask import jsonify
from flask import flash, request

from service.EmployeeService import EmployeeService

employeeService = EmployeeService()


@app.route('/employeeLogin', methods=['POST'])
def employeeLogin():

    responseData = employeeService.employeeLogin(request.headers, request.json)
    return responseData
