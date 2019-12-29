from CustomUtils import CustomUtils
from Exceptions.CustomerDoesNotExists import CustomerDoesNotExists
from Exceptions.EmployeeDosentHaveRight import EmployeeDosentHaveRight
from Exceptions.NotLoggedIn import NotLoggedIn
from app import app
from service import EmployeeService
from flask import jsonify
from flask import flash, request

from service.EnquiryService import EnquiryService

enquiryService = EnquiryService()


@app.route('/createEnquiry', methods=['POST'])
def createEnquiry():
    wsResponse = {"resultSet": None, "operationStatus": None}

    try:
        responseData = enquiryService.createEnquiry(request.headers, request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except EmployeeDosentHaveRight:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.EMPLOYEE_DOSENT_HAS_RIGHT
    except NotLoggedIn:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.EMPLOYEE_NOT_LOGGED_IN
    except CustomerDoesNotExists:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.CUSTOMER_DOES_NOT_EXIST
    except Exception:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG

    return wsResponse
