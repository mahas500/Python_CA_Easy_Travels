from app import app
from service import EmployeeService
from flask import jsonify
from flask import flash, request

from service.CustomerService import CustomerService

customerService = CustomerService()



@app.route('/customerAdd', methods=['POST'])
def customerCreate():

    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = customerService.customerCreate(request.headers, request.json)
    wsResponse['resultSet'] = responseData
    #print(responseData)
    wsResponse['operationStatus'] = 1
    return wsResponse

@app.route('/enquiryAdd', methods=['POST'])
def enquiryCreate():

    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = customerService.enquiryCreate(request.headers, request.json)
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return wsResponse